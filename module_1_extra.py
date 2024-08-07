grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted_list = sorted(list(students))
average_grades = list()
for grades_list in grades:
    average_grades.append(sum(grades_list) / len(grades_list))
student_average_grades = dict(zip(students_sorted_list, average_grades))
print(student_average_grades)
