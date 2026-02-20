import json
import os
from datetime import datetime

FILE_NAME = "students.json"

class Student:
    def __init__(self, student_id, name, grade, timestamp):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade,
            "timestamp": self.timestamp
        }

class StudentManager:
    def __init__(self):
        self.students = {}
        self.load_data()

    # Grade Validation
    def validate_grade(self, grade):
        return grade.upper() in ["A", "B", "C", "D", "E", "F"]

    def add_student(self):
        try:
            student_id = input("Enter Student ID: ")

            if student_id in self.students:
                print("Student ID already exists!")
                return

            name = input("Enter Name: ")
            grade = input("Enter Grade (A-F): ").upper()

            if not self.validate_grade(grade):
                print("Invalid Grade! Only A-F allowed.")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            student = Student(student_id, name, grade, timestamp)
            self.students[student_id] = student
            self.save_data()
            print("Student added successfully!")

        except Exception as e:
            print("Error:", e)

    def update_student(self):
        try:
            student_id = input("Enter Student ID to update: ")

            if student_id not in self.students:
                print("Student not found!")
                return

            name = input("Enter New Name: ")
            grade = input("Enter New Grade (A-F): ").upper()

            if not self.validate_grade(grade):
                print("Invalid Grade! Only A-F allowed.")
                return

            self.students[student_id].name = name
            self.students[student_id].grade = grade
            self.save_data()
            print("Student updated successfully!")

        except Exception as e:
            print("Error:", e)

    def delete_student(self):
        try:
            student_id = input("Enter Student ID to delete: ")

            if student_id in self.students:
                del self.students[student_id]
                self.save_data()
                print("Student deleted successfully!")
            else:
                print("Student not found!")

        except Exception as e:
            print("Error:", e)

    # Proper formatted table output
    def list_students(self):
        if not self.students:
            print("No students available.")
            return

        print("\n{:<10} {:<15} {:<10} {:<20}".format(
            "ID", "Name", "Grade", "Created On"))
        print("-" * 60)

        for student in self.students.values():
            print("{:<10} {:<15} {:<10} {:<20}".format(
                student.student_id,
                student.name,
                student.grade,
                student.timestamp
            ))

    def save_data(self):
        with open(FILE_NAME, "w") as file:
            json.dump({sid: student.to_dict() for sid, student in self.students.items()}, file)

    def load_data(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                for sid, student_data in data.items():
                    self.students[sid] = Student(
                        student_data["student_id"],
                        student_data["name"],
                        student_data["grade"],
                        student_data["timestamp"]
                    )

def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.update_student()
        elif choice == "3":
            manager.delete_student()
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()