# Voltage Values
v1 = 4
v2 = 5

# Resistace Values
r1 = 3
r2 = 5
r3 = 4
r4 = 1
r5 = 6
r6 = 8


def calculate_det(d):
    det = (
        (d[0][0] * (d[1][1] * d[2][2] - d[1][2] * d[2][1]))
        - (d[0][1] * (d[1][0] * d[2][2] - d[1][2] * d[2][0]))
        + (d[0][2] * (d[1][0] * d[2][1] - d[1][1] * d[2][0]))
    )
    return det


matrix = [
    [(r1 + r2), -1 * r2, 0],
    [-1 * r2, (r2 + r3 + r4 + r5), -1 * r4],
    [0, -1 * r4, (r4 + r6)],
]
matrix1 = [
    [v1, -1 * r2, 0],
    [0, (r2 + r3 + r4 + r5), -1 * r4],
    [-1 * v2, -1 * r4, (r4 + r6)],
]
matrix2 = [[(r1 + r2), v1, 0], [-1 * r2, 0, -1 * r4], [0, -1 * v2, (r4 + r6)]]
matrix3 = [
    [(r1 + r2), -1 * r2, v1],
    [-1 * r2, (r2 + r3 + r4 + r5), 0],
    [0, -1 * r4, -1 * v2],
]

determinant1 = calculate_det(matrix1)
determinant2 = calculate_det(matrix2)
determinant3 = calculate_det(matrix3)
determinant = calculate_det(matrix)

current1 = determinant1 / determinant
current2 = determinant2 / determinant
current3 = determinant3 / determinant

current_in_resistor_2 = current1 - current2
current_in_resistor_4 = current2 - current3

print("\n\nResult: ")
print("\tcurrent in the 5 ohm resistor is ", round(current_in_resistor_2, 2), " A")
print("\tcurrent in the 1 ohm resistor is ", round(current_in_resistor_4, 2), " A")
