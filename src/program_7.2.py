start, end = input("enter the range seperated by ',': ").split(",")

print("Numbers greater than zero in the range ", start, "to ", end, "is :\n")
for i in range(int(start), int(end) + 1):
    if i > 0:
        print(i)
