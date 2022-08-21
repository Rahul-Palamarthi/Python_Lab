row, column = str(input("enter the rows and columns seperated by ',': ")).split(",")

for i in range(0, int(row)):
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
