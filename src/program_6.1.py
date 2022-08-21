_numbers = str(input("enter numbers seperated by ',': ")).split(",")

max = _numbers[0]
min = _numbers[0]

for i in range(len(_numbers)):
    if _numbers[i] > max:
        max = _numbers[i]
    elif _numbers[i] < min:
        min = _numbers[i]
    else:
        continue

print("max number is: ", int(max))
print("min number is: ", int(min))
