import os

board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def printBoard():
        print("Here is the board")
        print(board[1] + '|'+ board[2]+'|'+ board[3])
        print('-----')
        print(board[4] + '|'+board[5]+'|' + board[6])
        print('-----')
        print(board[7] + '|'+board[8]+'|' + board[9])
        
       

        

def board_position():
    position='not a digit'
    acceptable_range= range(1,10)
    within_range= False
    # check if the input is a number and between the correct ranges
    while position.isdigit() == False or within_range == False: 
        
            position = input('Please mark your index at the board (1-9): ')
            if position.isdigit() == False: 
                print("Sorry that is not a digit")
            if position.isdigit():
                if int(position) in acceptable_range:
                    within_range = True
                else:
                    print("Sorry that number is out of the accepatable range (1-9)")
                    pass
              
    return int(position)

def choose_player():
    player='invalid'
    while player not in ['X','O']:
        player = input ('choose your marker X or O: ').upper()
        if player not in ['X','O']:
            print("invalid choice, please choose X or O")
    if player == "X" or player == "O":
        return player
    if player =="O":
        print(" O turn")
    else:
        print(" X turn")

def marker(board,position,player):
    user_placement = player
    board[position] = user_placement

    return board

def checkplacement(board,user_placement):
    if board[user_placement] == "X" or board[user_placement] == "O":
        print('this index is already taken!')
        return False
    return True

def checkvictory(board):
    pass
    
    
        
def main():
    global board
    player = choose_player()
    while True: 
        printBoard()
        print(player + "'s turn")
        pos = board_position()
        while not checkplacement(board, pos):
            pos = board_position()
        board = marker(board, pos,player)
        player = 'O' if player == 'X' else 'X'
        clear_terminal() 

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()