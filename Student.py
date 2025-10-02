import json

class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        
    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.rollno}, Marks: {self.marks}"
    
    def display_marks(self):
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
            
    def calculate_marks(self):
        avg = sum(self.marks.values())/len(self.marks)
        if avg >= 90:
            grade = "A"
        elif avg >=75:
            grade = "B"
        elif avg >=50:
            grade = "C"
        else:
            grade = "F"
        print(f"{self.name}'s Grade is {grade}")
        
class ReportCardSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        
    def view_student(self):
        for std in self.students:
            print(std)
            
    def search_student(self, rollno):
        for std in self.students:
            if std.rollno == rollno:
                print("Student Found")
                print(std)
                return
    
    def export_to_json(self, filename = "std.json"):
        data = [vars(student) for student in self.students] 
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def import_from_json(self):
        with open("std.json", 'r') as f:
            loaded = json.load(f)
            for i in loaded:
                print(f"Name: {i['name']}, Roll No: {i['rollno']}, Marks: {i['marks']}")
                
                
school = ReportCardSystem()

student1 = Student("Arun", 2501, {"Maths": 90, "Science": 85, "English": 88})
student2 = Student("John", 2502, {"Maths": 78, "Science": 82, "English": 80})
student3 = Student("Sara", 2503, {"Maths": 92, "Science": 95, "English": 89})

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

student1.calculate_marks()
student2.calculate_marks()
student3.calculate_marks()

school.export_to_json()
school.import_from_json()