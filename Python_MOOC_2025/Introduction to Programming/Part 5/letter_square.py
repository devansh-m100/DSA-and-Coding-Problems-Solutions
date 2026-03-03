layers = int(input("Enter the number of layers"))

size = 2 * layers - 1

for i in range(size):
    row = ""
    for j in range(size):
        distance = min(i, j, size - 1 - i, size - 1 - j)
        letter = chr(ord("A") + layers - 1 - distance)
        row += letter

    print(row)
