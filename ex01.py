result = 0
for i in range(5000):
    if i % 3 == 0 or i % 5 == 0:
        print(result)
        result += i; 
print(result)
