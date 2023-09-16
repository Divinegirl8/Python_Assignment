amount_invested = 1000
annual_rate_of_return = 0.07

amount_after_ten_years = amount_invested * (1 + annual_rate_of_return) ** 10

amount_after_twenty_years = amount_invested * (1 + annual_rate_of_return) ** 20

amount_after_thirty_years = amount_invested * (1 + annual_rate_of_return) ** 30

print(f"Amount on deposit after 10 years is ${amount_after_ten_years:.1f}")
print(f"Amount on deposit after 20 years is ${amount_after_twenty_years:.1f}")
print(f"Amount on deposit after 30 years is ${amount_after_thirty_years:.1f}")
