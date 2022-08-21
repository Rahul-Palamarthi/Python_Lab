nth_term = int(input("enter the number of terms: "))

a = 0
b = 1

print(a, b, end="")

while (nth_term - 2) > 0:
    a, b = b, a + b
    print("", b, end="")
    nth_term -= 1
