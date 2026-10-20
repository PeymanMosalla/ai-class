class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, course, grade):
        if grade < 0 or grade > 20:
            print("Invalid grade")
        else:
            self.grades[course] = grade

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def best_course(self):
        if len(self.grades) == 0:
            return None
        return max(self.grades, key=self.grades.get)

    def failed_courses(self):
        failed = []
        for course, grade in self.grades.items():
            if grade < 10:
                failed.append(course)
        return failed

    def status(self):
        avg = self.average()
        if avg >= 17:
            return "Excellent"
        elif avg >= 14:
            return "Good"
        elif avg >= 12:
            return "Normal"
        else:
            return "Probation"

    def report(self):
        print(f"Student: {self.name} (ID: {self.student_id})")
        for course, grade in self.grades.items():
            print(f"{course}: {grade}")
        print(f"Average: {self.average()}")
        print(f"Best course: {self.best_course()}")
        print(f"Failed courses: {self.failed_courses()}")
        print(f"Status: {self.status()}")


# بخش امتیازی
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def top_student(self):
        if len(self.students) == 0:
            return None
        return max(self.students, key=lambda s: s.average())

    def class_average(self):
        if len(self.students) == 0:
            return 0
        total = 0
        for student in self.students:
            total += student.average()
        return total / len(self.students)


sara = Student("Sara Ahmadi", 40312345)
sara.add_grade("Math", 18)
sara.add_grade("Physics", 9)
sara.add_grade("Programming", 20)
sara.add_grade("English", 15)

ali = Student("Ali Rezaei", 40354321)
ali.add_grade("Math", 12)
ali.add_grade("Physics", 14)
ali.add_grade("Programming", 11)
ali.add_grade("English", 8)

sara.report()
print("-" * 30)
ali.report()
print("-" * 30)

# تست نمره نامعتبر
sara.add_grade("Chemistry", 25)
print("-" * 30)

classroom = Classroom()
classroom.add_student(sara)
classroom.add_student(ali)
print("Top student:", classroom.top_student().name)
print("Class average:", classroom.class_average())
