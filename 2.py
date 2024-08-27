board_size = 3

board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|')*3)
        print(' ',board[i*3], '|',board[1 + i*3], '|', board[2 + i+3], '|')
        print(('_' * 3 + '|')*3)
    
    
   
def game_step(index, char):

    if(index > 9 or index < 1 or board[index-1 ]in ('X', 'O')):
        return False
    

    board[index-1]= char
    return True
    
def check_win():
    win = False

    win2 = (
        (0,1,2),
        (3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),
        (2,4,6)
    )
    for pos in win2: 
        if(board[pos[0]]==  board[pos[1]] and board[pos[1]]==board[pos[2]]):
            win = board[pos[0]]


    return win

   
def start_game():

    player ='X'
 
    draw_board()


while  (check_win() == False):
    index = input("player go" + player + "Choose your number(0 - end)" )

    if(index == '0'):
        break
    if ( game_step(int(index),player)):
        print("Good")

        if (player == 'X'):
            player = 'O'
        else:
            player = 'X'

        draw_board() 
        
    else:
        print("Incorrect Number,repeat")
   
        
        print('Win'+ check_win())        



   

print("Hello")
start_game()