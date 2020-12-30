print("Numbers Pattern 1: using a for loop and range function")
rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ")  # print number
    # line after each row to display pattern correctly
    print(" ")

print("Number Pattern 2: Half pyramid pattern with numbers")
rows = 5
for row in range(1, rows+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")

print("Numbers Pattern 3: Inverted Pyramid pattern with numbers")
rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

print("Numbers Pattern 4: Inverted Pyramid pattern with same number")
rows = 5
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

print("Numbers Pattern 5: Display descending order of number")
rows = 5
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

print("Number Pattern 6: Inverted half pyramid pattern with number")
rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")

print("Practice Problem: Display Reverse number pattern")
