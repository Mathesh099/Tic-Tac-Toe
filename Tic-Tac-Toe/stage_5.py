inputs = list(" " * 9)
rows = [[inputs[j] for j in range(i, i + 3)] for i in range(0, len(inputs), 3)]

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

element = 0

while " " in inputs:
    
    a, b = input("Enter the coordinates:").split()

    try:
        (int(a) or int(b)) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        check_1 = 1
    except:
        print("You should enter number!")
        continue

    if int(a) not in [1, 2, 3] or int(b) not in [1, 2, 3]:
        print("coordinates should be from 1 to 3!")
        continue
    
    cell = 3 * (int(a) - 1) + (int(b) - 1)
    
    if inputs[cell] != " ":
        print("This cell is occupied! choose another one!")
        continue
    
    else:
        if element == 0:
            inputs[cell] = 'X'
            rows[int(a) - 1][int(b) - 1] = 'X'
            element = 1
        
        elif element == 1:
            inputs[cell] = 'O'
            rows[int(a) - 1][int(b) - 1] = 'O'
            element = 0
    

    game(rows)

    x_wins = False
    o_wins = False
    draw_state = False

    for i in range(len(rows)):
    
        if rows[i][0] == 'X' and rows[i][1] == 'X' and rows[i][2] == 'X':
            x_wins = True
  
        if rows[i][0] == 'O' and rows[i][1] == 'O' and rows[i][2] == 'O':
            o_wins = True

    for i in range(len(rows)):
    
        if rows[0][i] == 'X' and rows[1][i] == 'X' and rows[2][i] == 'X':
            x_wins = True
    
        if rows[0][i] == 'O' and rows[1][i] == 'O' and rows[2][i] == 'O':
            o_wins = True

    if rows[0][0] == 'X' and rows[1][1] == 'X' and rows[2][2] == 'X':
        x_wins =True

    if rows[0][0] == 'O' and rows[1][1] == 'O' and rows[2][2] == 'O':
        o_wins =True

    if rows[0][2] == 'X' and rows[1][1] == 'X' and rows[2][0] == 'X':
        x_wins =True

    if rows[0][2] == 'O' and rows[1][1] == 'O' and rows[2][0] == 'O':
        o_wins =True

    if x_wins == True:
        print("X wins")

    elif o_wins == True:
        print("O wins")
    
    elif not x_wins or not o_wins:
        if inputs.count(" ") == 0:
            print("Draw")