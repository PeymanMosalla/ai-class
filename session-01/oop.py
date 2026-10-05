class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print("-" * 20)

    def change_major(self, new_major):
        self.major = new_major


student1 = Student("Ali", 123, "AI")
student2 = Student("Sara", 456, "Computer")

student1.show_info()
student2.show_info()

student2.change_major("Data Science")
print("After changing Sara's major:")
student2.show_info()
