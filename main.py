class Student:
	def __init__(self, name, surname, gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []
		self.courses_in_progress = []
		self.grades = {}

	def add_courses(self, course_name):

		self.finished_courses.append(course_name)

	def rate_lecturer(self, lecturer, course, grade):
		if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
			if course in lecturer.grades:
				lecturer.grades[course] += [grade]
			else:
				lecturer.grades[course] = [grade]
		else:
			return 'Ошибка'


	def __str__(self):
		return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции:{self.average_grade()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {'()'.join(self.finished_courses)}"

	def average_grade(self):
		grades_per_course = {course: self.grades[course] for course in self.grades}
		return sum(sum(course_grades) / len(course_grades) for course_grades in grades_per_course.values())

class Mentor:
	def __init__(self, name, surname):
			self.name = name
			self.surname = surname
			self.courses_attached = []

class Lecturer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name,surname)
		self.grades = {}

	def __str__(self):
		return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания:{self.average_grade()}'

	def average_grade(self):
		grades_per_course = {course: self.grades[course] for course in self.grades}
		return sum(sum(course_grades) / len(course_grades) for course_grades in grades_per_course.values())

	def __lt__(self, other):
		if isinstance(other, Lecturer):
			return self.average_grade() < other.average_grade()
		return NotImplemented

	def __le__(self, other):
		if isinstance(other, Lecturer):
			return self.average_grade() <= other.average_grade()
		return NotImplemented

	def __gt__(self, other):
		if isinstance(other, Lecturer):
			return self.average_grade() > other.average_grade()
		return NotImplemented

	def __ge__(self, other):
		if isinstance(other, Lecturer):
			return self.average_grade() >= other.average_grade()
		return NotImplemented

	def __eq__(self, other):
		if isinstance(other, Lecturer):
			return self.average_grade() == other.average_grade()
		return NotImplemented

	def __ne__(self, other):
		if isinstance(other, Lecturer):
			return self.average_grade() != other.average_grade()
		return NotImplemented


class Reviewer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name,surname)

	def rate_hw(self, student, course, grade):
			if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
					if course in student.grades:
							student.grades[course] += [grade]
					else:
							student.grades[course] = [grade]
			else:
					return 'Ошибка'

	def __str__(self):
		return f'Имя: {self.name} \nФамилия: {self.surname}'

	def average_grade_homework(self):
		grades_per_course = {course: self.grades[course] for course in self.grades}
		return sum(sum(course_grades) / len(course_grades) for course_grades in grades_per_course.values())

	def __lt__(self, other):
		if isinstance(other, Reviewer):
				return self.average_grade_homework() < other.average_grade_homework()
		return NotImplemented

	def __le__(self, other):
		if isinstance(other, Reviewer):
				return self.average_grade_homework() <= other.average_grade_homework()
		return NotImplemented

	def __gt__(self, other):
		if isinstance(other, Reviewer):
				return self.average_grade_homework() > other.average_grade_homework()
		return NotImplemented

	def __ge__(self, other):
		if isinstance(other, Reviewer):
				return self.average_grade_homework() >= other.average_grade_homework()
		return NotImplemented

	def __eq__(self, other):
		if isinstance(other, Reviewer):
				return self.average_grade_homework() == other.average_grade_homework()
		return NotImplemented

	def __ne__(self, other):
		if isinstance(other, Reviewer):
				return self.average_grade_homework() != other.average_grade_homework()
		return NotImplemented

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_2 = Student('Some', 'Buddy', 'your_gender')
student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Python']
student_1.finished_courses += ['GIT']
student_2.finished_courses += ['Java']
reviewer_1 = Reviewer('Bob', 'Bobson')
reviewer_2 = Reviewer('John', 'Smitt')
reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Python']
lecturer_1 = Lecturer('Boris', 'Johnson')
lecturer_2 = Lecturer('Mike', 'Jackson')
lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 9)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)