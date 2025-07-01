marks = [99, 97, 89, 55, 44, 33, 22, 14]
# if marks < 95:
bonus_marks = [x+5 for x in marks if x < 95]
print(bonus_marks)

passed_students = [x for x in bonus_marks if x >= 40]
print(passed_students)

grade_lst = ["A","B", "C", "F"]
grades = ['A' if x > 75 else 'B' if x > 60  else 'C' if x > 40 else 'F' for x in passed_students]
print(grades)
