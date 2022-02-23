def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

result = 0
for n in range(10,101):
    for r in range(1, n+1):
        if factorial(n)/(factorial(r) * factorial(n-r)) > 1000000:
            result += 1

print(result)
