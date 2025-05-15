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
        if subject in subjects:
            subjects[subject].append(self.id)
        else:
            subjects[subject] = [self.id]
        
        self.subjects.append(subject)

def printStudentList(subject):
    print(f"Students: {', '.join(str(student) for student in subjects[subject])}")

subjects = {}

israel = Student("Israel", "Irawan", 1234, "Johnson")
israel.enrolClass("Math")
print(israel.subjects)
printStudentList("Math")