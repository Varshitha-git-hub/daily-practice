student_exam_fee=30000
student_pay_amount=20000
if student_exam_fee>=student_pay_amount:
    print("paid amount:",student_pay_amount)
    student_exam_fee-=student_pay_amount
    print("remaining amount to pay:",student_exam_fee)
    if student_exam_fee==0:
        pass
    else:
        print("payment not completed.please pay the remaining amount")
