#condiotional statements
#eg:student grading system
student_name=input("enter a name:")
student_marks=int(input("enter student marks:"))
if student_marks>=90:#if condition:execute a block of code if condition is true.
    grade="A"
elif student_marks>=80:#elif condition:used to check another if the initial condition is false.
    grade="B" 
elif student_marks>=70:
    grade="C"
elif student_marks>=60:
    grade="D"
else:#else:used to excute a block of code if all previous conidtions are false.
    grade="F" 
if student_marks>=90:#nested if condition:a statement within a statement.
    if student_marks>=99:
        print("congrautations,you got 99 marks")
    else:
        print("congrats,you got",grade)           
else:
    print("congralutations you grade is",grade,",",student_name)          