import csv

class Student:
    def __init__(self, full_name):
        self.full_name = full_name

student = Student("Петрович паук")
print(student.full_name) 

class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError("ФИО должно начинаться с заглавной буквы и содержать только буквы.")
        instance._name = value

class Student:
    name = NameDescriptor()

    def __init__(self, name):
        self.name = name

student = Student("Петрович паук")
print(student.name)  


class Student:
    def __init__(self, subjects_file):
        self.subjects = self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        subjects = []
        with open(subjects_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                subjects.append(row[0])
        return subjects

student = Student("subjects.csv")
print(student.subjects)  

class Student:
    def __init__(self, subjects_file):
        self.subjects = self.load_subjects(subjects_file)
        self.scores = {subject: [] for subject in self.subjects}
        self.test_results = {subject: [] for subject in self.subjects}

    def add_score(self, subject, score):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет.")
        if score < 2 or score > 5:
            raise ValueError("Недопустимая оценка.")
        self.scores[subject].append(score)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет.")
        if result < 0 or result > 100:
            raise ValueError("Недопустимый результат теста.")
        self.test_results[subject].append(result)

student = Student("subjects.csv")
student.add_score("Math", 4)
student.add_test_result("Math", 80)
print(student.scores)  # Выводит {'Math': [4]}
print(student.test_results)  # Выводит {'Math': [80]}