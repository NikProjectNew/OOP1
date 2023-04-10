class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                if lecturer in lecturer.grades[course]:
                    lecturer.grades[course][lecturer].append(grade)
                else:
                    lecturer.grades[course][lecturer] = [grade]
            else:
                lecturer.grades[course] = {lecturer: [grade]}
        else:
            return 'Ошибка'
          

      
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    
      
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
      
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
          
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
 
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)

lecturer = Lecturer('John', 'Doe')
lecturer.courses_attached += ['Python']

best_student.rate_lecturer(lecturer, 'Python', 8)
best_student.rate_lecturer(lecturer, 'Python', 9)
best_student.rate_lecturer(lecturer, 'Python', 10)

print(some_reviewer)
