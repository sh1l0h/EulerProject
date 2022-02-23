
f = open("numbers.txt", "r")
lines = f.readlines()

numbers = []
for l in lines:
    numbers.append(int(l))

print(sum(numbers))
