#elif with break keyword
while True:
    student_score = int(input("Enter a number: "))
    
    if student_score >= 90:
        print("Grade: A")
    elif student_score >= 80:
        print("Grade: B")
    elif student_score >= 70:
        print("Grade: C")
    elif student_score >= 60:
        print("Grade: D")
    else:
        print("Grade: E")
    
    break

#elif with pass keyword
student_score = int(input("Enter a number: "))

if student_score >= 90:
    print("Grade: A")
elif student_score >= 80:
    print("Grade: B")
elif student_score >= 70:
    print("Grade: C")
elif student_score >= 60:
    print("Grade: D")
else:
    print("Grade: E")
    pass  # No action needed for Grade E


#elif with continue keyword
while True:
    student_score = int(input("Enter a number: "))

    if student_score < 0 or student_score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        continue

    if student_score >= 90:
        print("Grade: A")
    elif student_score >= 80:
        print("Grade: B")
    elif student_score >= 70:
        print("Grade: C")
    elif student_score >= 60:
        print("Grade: D")
    else:
        print("Grade: E")

    break

