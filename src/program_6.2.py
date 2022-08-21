_numbers = str(input("enter numbers seperated by ',': ")).split(",")

cumulative_sum = list()
sum = 0

for i in range(len(_numbers)):
    sum += int(_numbers[i])
    cumulative_sum.append(sum)

print("cumulative sum of numers is: ", cumulative_sum)
