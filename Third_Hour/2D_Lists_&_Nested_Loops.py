# 2D list is about a list inside a list.

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0])
print(number_grid[3])
print(number_grid[-1])

print(number_grid[0][0])
print(number_grid[2][2])

# Nested loop is a loop inside a loop:

for row in number_grid:
    for col in row:
        print(col)

