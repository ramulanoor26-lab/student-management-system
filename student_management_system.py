class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def to_string(self):
        return f"{self.student_id},{self.name},{self.course}"

    @staticmethod
    def from_string(data):
        student_id, name, course = data.strip().split(",")
        return Student(student_id, name, course)


class StudentManagementSystem:
    def __init__(self, filename="students.txt"):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    self.students.append(Student.from_string(line))
        except FileNotFoundError:
            pass

    def save_students(self):
        with open(self.filename, "w") as file:
            for student in self.students:
                file.write(student.to_string() + "\n")

    def add_student(self):
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Student Name: ").strip()
        course = input("Enter Course: ").strip()

        if not student_id or not name or not course:
            print("Invalid input. All fields are required.")
            return

        self.students.append(Student(student_id, name, course))
        self.save_students()
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Course: {student.course}")

    def update_student(self):
        student_id = input("Enter Student ID to update: ").strip()
        for student in self.students:
            if student.student_id == student_id:
                student.name = input("Enter new name: ").strip()
                student.course = input("Enter new course: ").strip()
                self.save_students()
                print("Student updated successfully.")
                return
        print("Student not found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ").strip()
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully.")
                return
        print("Student not found.")


def main():
    system = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            system.update_student()
        elif choice == "4":
            system.delete_student()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

