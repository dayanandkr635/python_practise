print("Welcome to the Loan Eligibility Checker!")

salary= float(input("Enter your monthly salary: "))

monthly_emi= float(input("enter your monthly EMI:"))

available_income= salary - monthly_emi

if available_income >=20000:
    print("your are eligible for the loan")
else:
    print("you are not eligible for the loan")
    print("reason: your available income is less than 20000")
    