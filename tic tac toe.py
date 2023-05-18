#create inital board
def make_board():
    board =[[1,2,3],[4,5,6],[7,8,9]]
    return board

#display current board
def display_board(board):
    for i in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   ", board[i][0],"   |   ", board[i][1],"   |   ", board[i][2], "   |", sep="")
        print("|       |       |       |")

    print("+-------+-------+-------+")
    return

#create a tuple of free fields on the board
def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] != 'X' and board[i][j] != 'O'):
                free_fields.append(board[i][j])

    if(len(free_fields) == 0):
        return None
    else:
        return tuple(free_fields)

#gets the user's move
def enter_move(board):
    move = 0
    while(True):
        try:
            move = int(input("Enter Your move: "))
        except ValueError:
            print("Please input an int")
            continue
        except KeyboardInterrupt:
            exit()
        except:
            print("something went wrong, try again")
            continue
        if(move not in make_list_of_free_fields(board)):
            print("Not a free field")
        else:
            return move

#updates the board with the move
def update_board(board, move, sign):
    dic_pos ={
        1 : (0,0), 2 : (0,1), 3 : (0,2),
        4 : (1,0), 5 : (1,1), 6 : (1,2),
        7 : (2,0), 8 : (2,1), 9 : (2,2),
        }
    board[dic_pos[move][0]][dic_pos[move][1]] = sign
    display_board(board)
    return

#checks for victory condition
def victory_for(board, sign):
    if((board[0][0] == board[1][1] == board[2][2] == sign) or (sign == board[2][0] == board[1][1] == board [0][2])):
        return True
    for i in range(3):
        if (board[i][0] == board [i][1] == board[i][2] == sign):
            return True
        elif (board[0][i] == board [1][i] == board[2][i] == sign):
            return True

    return False

#generates a move for the computer
def draw_move(board):
    from random import randrange
    x = -1
    while(x not in make_list_of_free_fields(board)):
        x = randrange(9)
    return x


#main
board = make_board() #create board
display_board(board) #display initial board
while(make_list_of_free_fields(board) != None): #game loop
    update_board(board, enter_move(board), sign = 'O') #user's move
    if(victory_for(board, sign = 'O')):
        print("You Won!")
        break;
    print("===== Computer's Turn =====")
    update_board(board, draw_move(board), sign = 'X') #comupter's move
    if(victory_for(board, sign = 'X')):
        print("The Computer Won!")
        break;
