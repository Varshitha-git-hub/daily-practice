#if with pass keyword
student_exam_fee = 30000
student_pay_amount = 20000

if student_exam_fee >= student_pay_amount:
    print("Paid amount:", student_pay_amount)
    student_exam_fee -= student_pay_amount
    print("Remaining amount to pay:", student_exam_fee)
else:
    pass  # do nothing

#if with break keyword
# If you want to use the break keyword, you need a loop (like for or while) to break out of.


# Define exam fee and payment amount
student_exam_fee = 30000
student_pay_amount = 20000

while True:
    if student_exam_fee >= student_pay_amount:
        print("Paid amount:", student_pay_amount)
        student_exam_fee -= student_pay_amount
        print("Remaining amount to pay:", student_exam_fee)
    else:
        print("Payment completed.")
        break

#if with continue keyword
# Define exam fee and payment amount
exam_fee = 30000
payment_amount = 20000
attempts = 3

for attempt in range(attempts):
    if exam_fee < payment_amount:
        print("Insufficient funds. Attempt", attempt + 1)
        continue
    
    print("Paid amount:", payment_amount)
    exam_fee -= payment_amount
    print("Remaining amount:", exam_fee)
