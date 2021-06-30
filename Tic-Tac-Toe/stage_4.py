inputs = list(input("Enter cells:"))
rows = [[inputs[j] for j in range(i, i + 3)] for i in range(0, len(inputs), 3)]

print(rows)

def game(rows):
    
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

game(rows)

check_1 = 0
check_2 = 0
check_3 = 0
checker = True

while checker == True:
    
    a, b = input("Enter the coordinates:").split()

    try:
        (int(a) or int(b)) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        check_1 = 1
    except:
        print("You should enter number!")
        continue

    if (int(a) or int(b)) not in [1, 2, 3]:
        print("coordinates should be from 1 to 3!")
        continue

    else:
        check_2 = 1
    
    cell = 3 * (int(a) - 1) + (int(b) - 1)
    
    if inputs[cell] != "_":
        print("This cell is occupied! choose another one!")
        continue
    
    else:
        rows[int(a) - 1][int(b) - 1] = 'X'
        check_3 = 1
    
    if check_1 + check_2 + check_3 == 3:
        checker = False
        break

game(rows)