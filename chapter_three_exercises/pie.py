

pi_estimate = 0.0
for i in range(0,7):
    term = (-1) ** i / (2 * i + 1)
    pi_estimate += term
    result = 4 - pi_estimate
    print(result)
