from student import Student
from course_group import CourseGroup

student = Student("Иван", "Петров", "32", "Слесарь")
classmate1 = Student("Василий", "Сидоров", "29", "Слесарь")
classmate2 = Student("Петр", "Васильев", "30", "Слесарь")
classmate3 = Student("Сидор", "Иванов", "31", "Слесарь")
classmate4 = Student("Сергей", "Сергеев", "32", "Слесарь")

course_group = CourseGroup(student, [classmate1,classmate2, classmate3, classmate4])

print(course_group)