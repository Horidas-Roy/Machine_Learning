students = [("Rafi", 89), ("Sumi", 95), ("Hasan", 90), ("Nila", 75), ("Anik", 98)]

# method : 01
# sort_students = sorted(students,key=lambda t: t[1],reverse=True)

# method : 02
student_dic = dict(students)
sort_students = sorted(student_dic.items(),key=lambda t: t[1],reverse=True)

# print(sort_students)

print("Top 3 students:")
for student in sort_students[:3]:
    print(f"{student[0]} - {student[1]}")