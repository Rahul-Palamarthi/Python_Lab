num = int(input("enter the number to be checked: "))

counter = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        counter += 1

if counter > 2:
    print(num, "is not a Prime Number")
else:
    print(num, "is a Prime Number")
