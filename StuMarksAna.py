from functools import reduce

mark_list =[80, 40, 55, 65, 82, 35, 33, 75]

bonus_marks = list(map(lambda x:x + 5, mark_list))
print(bonus_marks)

passed_students = list(filter(lambda x: x>=40, bonus_marks))
print(passed_students)

# a = (len(passed_students))

total_marks = reduce(lambda x, y: x+y, passed_students)
avg_of_passing_stu = total_marks / len(passed_students)

print(round(avg_of_passing_stu, 2))

failed_stu = list(filter(lambda x: x<40, bonus_marks))
print(failed_stu)