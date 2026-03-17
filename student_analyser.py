import numpy as np


marks = np.array([
    [85, 90, 78, 92],
    [75, 80, 85, 88],
    [95, 92, 90, 94],
    [60, 65, 70, 72],
    [88, 85, 20, 90]
])

students = ["Ram", "Sita", "Lakshaman", "Urmila", "Sumitra"]

subjects = ["English", "Maths", "Physics","Chemistry"]

print("Average marks of the studens are: ")
for i in range(0,len(marks)):
    avg=np.mean(marks[i])
    print(f"{students[i]}-> Average marks is {avg:.2f}")
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    else:
        grade = "C"
    
    print(f"{students[i]} -> Grade: {grade}\n")
    

total_marks = np.sum(marks, axis=1)   
highest = np.argmax(total_marks)

print(f"\nTopper is {students[highest]} with total {total_marks[highest]}\n")
    
                  
passing_marks = 40

for i, student_marks in enumerate(marks):
    failed_subjects = []

    for j, mark in enumerate(student_marks):
        if mark < passing_marks:
            failed_subjects.append(subjects[j])

    if len(failed_subjects) == 0:
        print(f"{students[i]}: Pass")
    else:
        print(f"{students[i]}: Fail in {', '.join(failed_subjects)}")        
               
    
subject_total = np.sum(marks, axis=0)   
highest = np.argmax(subject_total)

print(f"\nHighest Scoring Subject is {subjects[highest]} with total {subject_total[highest]}")




