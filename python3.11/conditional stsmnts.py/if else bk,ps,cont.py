
student_exam_fee = 50000
student_pay_amount = 44000
student_due_amount = (student_exam_fee - student_pay_amount)

if student_exam_fee <= student_pay_amount:
    print("Student exam fee:", student_exam_fee)
else:
    print("Student due amount:", student_due_amount)
    pass  # No action needed when student has due amount
