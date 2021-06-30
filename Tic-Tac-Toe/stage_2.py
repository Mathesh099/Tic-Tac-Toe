inputs = list(input("Enter cells:"))
rows = [[inputs[j] for j in range(i, i + 3)] for i in range(0, len(inputs), 3)]

print('-' * 9)

for i in range(len(rows)):
    for j in range(len(rows)):
        if j == 0:
            print("| ", end = "")
        if j == 2:
            print(rows[i][j] + " |")
        else:
            print(rows[i][j] + " ", end = "")

print('-' * 9)