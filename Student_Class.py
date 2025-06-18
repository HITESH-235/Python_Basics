#Create a class for adding Students. Add function to display average, total marks. Add function to add, display, students and one to show topper.

class Student:
    def __init__(self,name,roll_num,phy,chem,math):
        self.name = name 
        self.roll_num = roll_num
        self.phy = phy
        self.chem = chem
        self.math = math

    def total_marks(self):
        return (self.phy + self.chem + self.math)

    def average_marks(self):
        return (self.phy+self.chem+self.math)/3
    

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self,Student):
        self.students.append(Student)

        return f"Student: {Student.name}, Roll number: {Student.roll_num}, added successfully"

    def display_all(self):
        print("\nList of students in the class:")
        for student in self.students:
            print(f"Name: {student.name}, Roll No.: {student.roll_num}")

#method_1 for showing topper
    def show_topper_1(self): 
        topper = None
        highest = -1  # since marks can't be -ve
        for x in self.students:
            total = x.total_marks()
            if total > highest:
                highest = total
                topper = x.name
        return topper

#method_2 for showing topper
    def show_topper_2(self):
        highest = max(self.students, key = get_total)  #no need to write () across function
        return f"\nName of topper: {highest.name}"

#Best method: using Lambda:
    def show_topper_best(self):
        highest = max(self.students, key = lambda s: s.total_marks())
        return highest.name


def get_total(s):  #Part of method_2
    return s.total_marks()

class_ = StudentManager()
s1 = Student("Name_1",5,29,89,45)
s2 = Student("Name_2",21,56,67,78)

print(class_.add_student(s1))
print(class_.add_student(s2))

class_.display_all()
print(class_.show_topper_best())
