employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked in a week: "))
hourly_pay = float(input("Enter hourly pay rate: "))
federal_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

print()

gross_pay = hours_worked * hourly_pay
federal_income = gross_pay * federal_tax / 100

state_income = gross_pay * state_tax / 100
state_income_a = "{:.2f}".format(state_income)

total_deduction = federal_income + state_income
total_deduction_a = "{:.2f}".format(total_deduction)

net_pay = gross_pay - total_deduction
net_pay_a = "{:.2f}".format(net_pay)

print(f"""
{employee_name} Payroll statement for the month of April
Employee Name: {employee_name}
Hours Worked: {hours_worked}
Pay Rate:     ${hourly_pay}
Gross Pay:    ${gross_pay}

Deductions: 
Federal Withholding: ${federal_income}
State Withholding:   ${state_income_a}
Total Deduction: $ {total_deduction_a}
Net Pay: ${net_pay_a}
""")

<<<<<<< HEAD
print("Employee Name:", employee_name)
print("Hours Worked:", hours_worked)
print("Pay Rate:", "$" + str(hourly_pay))
print("Gross Pay:", "$" + str(gross_pay))
print("Deductions: ")
print("Federal Withholding:", "$" + str(federal_income))
print("State Withholding:", "$" + str(state_income_a))
print("Total Deduction:", "$" + str(total_deduction_a))
print("Net Pay:", "$" + str(net_pay_a))

# refactor to use one print statement.
=======
>>>>>>> be97ece (update)
