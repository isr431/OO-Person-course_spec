import random

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printFullName(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname, id, house):
        super().__init__(fname, lname)
        self.id = id
        self.house = house
        self.subjects = []
        people[id] = self
    
    def enrolClass(self, subject):
        if subject not in subjects:
            addSubject(subject)

        subjects[subject]["students"].append(self.id)
        subjects[subject]["classSize"] += 1
        self.subjects.append(subject)
    
    def displaySubjects(self):
        print("Subjects:")

        for subject in self.subjects:
            print("-", subject)

class Parent(Person):
    def __init__(self, fname, lname, *children: Student):
        super().__init__(fname, lname)
        self.children = list(children)
    
    def displayChildren(self):
        print("Children:")

        for child in self.children:
            print("-", child)

class Teacher(Person):
    def __init__(self, fname, lname, id):
        super().__init__(fname, lname)
        self.id = id
        self.subjects = []
        people[id] = self
    
    def enrolClass(self, subject):
        if subject not in subjects:
            addSubject(subject)
        
        subjects[subject]["teacher"] = id
        self.subjects.append(subject)
    
    def displaySubjects(self):
        print("Subjects:")

        for subject in self.subjects:
            print("-", subject)

def printStudentList(subject):
    print(f"Students: {', '.join(str(student) for student in subjects[subject]["students"])}")

def addSubject(subject):
    subjects[subject] = {
        "teacher": "",
        "students": [],
        "classSize": 0
    }

def createID():
    while True:
        id = random.randint(10000000, 99999999)

        if id not in people:
            return id

subjects = {}
people = {}

israel = Student("Israel", "Irawan", createID(), "Johnson")
israel.enrolClass("Math")
israel.enrolClass("English")
israel.enrolClass("Software Engineering")
israel.enrolClass("Legal Studies")
israel.enrolClass("Enterprise Computing")
israel.enrolClass("Studies of Religion")
israel.displaySubjects()

print(people)
print(subjects)