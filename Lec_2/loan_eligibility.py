print(" Welcome to loan criteria checker")

salary= float(input(" Enter your monthly salary: "))

monthly_emi= float(input(" Enter your monthly EMI: "))

available_income= salary - monthly_emi

minimum_salary= 30000
minimum_available_income= 20000

print("\nYour available income after EMI is: ₹ ", available_income)

if salary >=minimum_salary:
    if available_income >=minimum_available_income:
        print(" Congaturations! Your are eligible for the loan.")
    else:
        print(" Sorry! You are not eligible for the loan. ")
        print("reason: your available income is less than ₹ 20000")
        
else:
    print(" you are not eligible for the loan.")
    print(" Reason: Your salary is below the minimum requarement.")
    
    print("\n Thank you for using Eligibility checker. Have a nice day!")     
        
