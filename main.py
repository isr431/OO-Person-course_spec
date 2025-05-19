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
    
    def displaySubjects(self):
        print("Subjects:")

        for subject in self.subjects:
            print("-", subject)
    
    def run(self):
        while True:
            mode = input("Would you like to display all subjects or enrol in a class (display/enrol/exit): ").lower()

            if mode == "display":
                self.displaySubjects()
            elif mode == "enrol":
                subject = input("Enter subject: ").lower()
                self.enrolClass(subject)
                print(f"Student successfully enrolled in {subject}.")
            elif mode == "exit":
                break
            else:
                print("Invalid mode.")

class Parent(Person):
    def __init__(self, fname, lname, *children: Student):
        super().__init__(fname, lname)
        self.children = list(children)
    
    def displayChildren(self):
        print("Children:")

        for child in self.children:
            print("-", child)

def printStudentList(subject):
    print(f"Students: {', '.join(str(student) for student in subjects[subject])}")

subjects = {}

israel = Student("Israel", "Irawan", 1234, "Johnson")
israel.enrolClass("Math")
israel.enrolClass("English")
israel.enrolClass("Software Engineering")
israel.enrolClass("Legal Studies")
israel.enrolClass("Enterprise Computing")
israel.enrolClass("Studies of Religion")
israel.displaySubjects()