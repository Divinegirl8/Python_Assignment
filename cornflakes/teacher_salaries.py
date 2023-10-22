def salary(periods):
    rate = 20
    result = periods * rate if periods <= 100 else (periods - (periods - 100)) * rate + (periods - 100) * (rate + 5)
    return result


user = input("Enter teacher's name: ")
period = int(input("Enter number of periods: "))

print(f"""
Teacher name: {user}
Number of periods : {period}
Gross Salary: {salary(period)}
""")
