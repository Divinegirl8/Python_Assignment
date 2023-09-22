initial_population = 8_045_311_447
growth_rate = 0.088

print("YEARS\t    POPULATION\t       YEARLY INCREASE")
for years in range(1,101):
    result = initial_population * (1 + growth_rate)**years
    increase = result - initial_population
    print(f"  {years}        {result:.2f}        {increase:.2f}")