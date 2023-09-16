users_age = int(input("Enter your age: "))

maximum_heart_rate = 220 - users_age

target_heartrate_one = 50 * maximum_heart_rate // 100
target_heartrate_two = 85 * maximum_heart_rate // 100

print("The maximum heartrate is", maximum_heart_rate)
print("The target heartrate is", target_heartrate_one, "and", target_heartrate_two)
