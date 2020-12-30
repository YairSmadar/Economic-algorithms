from typing import List


class Department:
    def __init__(self, ID):
        self.candidate_students = []
        self.chosen_students = []
        self.ID = ID


class Student:
    def __init__(self, ID, class_preferences: List[Department], grade):
        self.ID = ID
        self.class_preferences = class_preferences
        self.grade = grade


def clear_classes_from_preferences(students: List[Student], the_one, department: Department):
    for student in students:
        if student.ID == the_one:
            student.class_preferences.clear()
        else:
            if len(student.class_preferences) != 0 and student.class_preferences[0].ID == department.ID:
                student.class_preferences.pop(0)


def check_if_finish(students: List[Student]):
    for student in students:
        if len(student.class_preferences) != 0:
            return True

    return False


def print_chosen_candidates(departments: List[Department]):
    for department in departments:
        print("department " + str(department.ID) + ":", end=" ")
        print(department.chosen_students)


def get_all_candidate_students(students: List[Student], department: Department):
    for student in students:
        if len(student.class_preferences) != 0:
            if student.class_preferences[0].ID == department.ID:
                department.candidate_students.append(student)


def choose_the_best_student(department: Department):
    the_one = -1
    max_grade = -1
    for student in department.candidate_students:
        if max_grade < student.grade:
            max_grade = student.grade
            the_one = student.ID
    if the_one != -1 and len(department.chosen_students) == 0:
        department.chosen_students.append(the_one)
    department.candidate_students.clear()

    return the_one


def GaleAndShapleyAlgo(students: List[Student], departments: List[Department]):
    """
    >>> d1 = Department(1)
    >>> d2 = Department(2)
    >>> d3 = Department(3)
    >>> s1 = Student(1, [d1, d2], 90)
    >>> s2 = Student(2, [d1, d3], 85)
    >>> s3 = Student(3, [d2, d3], 100)
    >>> s4 = Student(4, [d1], 75)
    >>> s5 = Student(5, [d1, d2, d3], 89)
    >>> deps = [d1, d2, d3]
    >>> studs = [s1, s2, s3, s4, s5]
    >>> GaleAndShapleyAlgo(studs, deps)
    department 1: [1]
    department 2: [3]
    department 3: [5]

    >>> d1.chosen_students.clear()
    >>> d2.chosen_students.clear()
    >>> d3.chosen_students.clear()
    >>> s1 = Student(1, [d3], 90)
    >>> s2 = Student(2, [d2], 85)
    >>> s3 = Student(3, [d1, d2], 100)
    >>> s4 = Student(4, [d3], 75)
    >>> s5 = Student(5, [d1, d2, d3], 89)
    >>> deps = [d1, d2, d3]
    >>> studs = [s1, s2, s3, s4, s5]
    >>> GaleAndShapleyAlgo(studs, deps)
    department 1: [3]
    department 2: [5]
    department 3: [1]
    >>> d1.chosen_students.clear()
    >>> d2.chosen_students.clear()
    >>> d3.chosen_students.clear()
    >>> s1 = Student(1, [d3], 90)
    >>> s2 = Student(2, [d2], 85)
    >>> s3 = Student(3, [d1, d2], 100)
    >>> s4 = Student(4, [d3], 75)
    >>> s5 = Student(5, [d2, d1], 20)
    >>> s6 = Student(6, [d2, d1], 59)
    >>> s7 = Student(7, [d3, d2, d1], 70)
    >>> s8 = Student(8, [d2, d3, d1], 99)
    >>> s9 = Student(9, [d3, d1], 87)
    >>> deps = [d1, d2, d3]
    >>> studs = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
    >>> GaleAndShapleyAlgo(studs, deps)
    department 1: [3]
    department 2: [8]
    department 3: [1]
    """

    while (check_if_finish(students)):

        for department in departments:
            get_all_candidate_students(students, department)
            the_one = choose_the_best_student(department)
            clear_classes_from_preferences(students, the_one, department)

    print_chosen_candidates(departments)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
