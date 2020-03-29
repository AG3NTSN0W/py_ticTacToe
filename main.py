from IPython.display import clear_output
import random

# Global variables
theBoard = [' '] * 10   # a list of empty spaces
players = [0,'X','O']   # note that players[1] == 'X' and players[-1] == 'O'

def display_board(board):
    for position in [6,3,0]:
        print(f'{board[1+position]} | {board[2+position]} | {board[3+position]}')
        if (position != 0):
            print(9*"-")
        pass    
    pass        
pass

def place_marker(board, marker, position):
    board[position] = marker
pass

def win_check(board, mark):
    winSet = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    winCount = 0
    for value in winSet:
        for subValue in value:
            if board[subValue] != mark:
                winCount = 0
                break
            else:
                winCount += 1
                if winCount == 3:
                    return True
        pass
    pass
    return False

def choose_first():
    return random.choice((-1, 1))


def space_check(board, position):
    if (board[position] == ' '):
        return True
    return False   

def full_board_check(board):
    for space in board:
        if space == ' ':
            return False
    return True    

def player_choice(board, player):
    position = None
    question = f'{player} : Choose your next position: (1-9)'
    while True:
        try:
            position = int(input(question)) 
            if  position in [1,2,3,4,5,6,7,8,9] and space_check(board, position):
                return position            
        except:
            question = f'{player} : Please try again Choose position: (1-9)'
            continue
    pass    

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')     

while True:
    clear_output()
    theBoard[0] = '#'
    print('Welcome to Tic Tac Toe!')

    toggle = choose_first()
    player = players[toggle]
    print('For this round, Player %s will go first!' %(player))

    game_on = True
    input('Hit Enter to continue')

    while game_on:
        display_board(theBoard)
        print(1*'\n')
        position = player_choice(theBoard,player)
        place_marker(theBoard,player,position)

        if win_check(theBoard, player):
            print(2*'\n')
            display_board(theBoard)
            print('Congratulations! Player '+player+' wins!')
            game_on = False
        else:
            if full_board_check(theBoard):
                display_board(theBoard)
                print('The game is a draw!')
                break
            else:
                toggle *= -1
                player = players[toggle]
                clear_output()
        print(2*'\n')        

    # reset the board and available moves list
    theBoard = [' '] * 10        

    if not replay():
        break    