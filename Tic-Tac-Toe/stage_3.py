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

x_wins = False
o_wins = False
finished_state = True
draw_state = False
x_count = 0
o_count = 0
possible_state = True

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

if not x_wins or not o_wins:
    for i in rows:
        if '_' in i:
            finished_state =False

if not finished_state and not x_wins or not o_wins:
    draw_state = True

for i in range(len(rows)):
    x_count += rows[i].count('X')
    o_count += rows[i].count('O')

if x_wins and o_wins:
    possible_state = False
    x_wins = False
    o_wins = False

if x_count > o_count + 1 or o_count > x_count + 1:
    possible_state = False
    x_wins = False
    o_wins = False

if x_wins == True:
    print("X wins")
    finished_state = True
    draw_state =False

if o_wins == True:
    print("O wins")
    finished_state = True
    draw_state =False

if finished_state == False:
    print("Game not finished")
    draw_state = False

if possible_state == False:
    print("Impossible")
    draw_state = False

if draw_state == True:
    print("Draw")
