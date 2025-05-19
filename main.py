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
    
    def enrolClass(self, subject):
        if subject not in subjects:
            addSubject(subject)

        subjects[subject]["students"].append(self.id)
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

subjects = {}

israel = Student("Israel", "Irawan", 1234, "Johnson")
israel.enrolClass("Math")
israel.enrolClass("English")
israel.enrolClass("Software Engineering")
israel.enrolClass("Legal Studies")
israel.enrolClass("Enterprise Computing")
israel.enrolClass("Studies of Religion")
israel.displaySubjects()