#Tic-Tac-Toe


#Draw Game Board

#prints tic tac toe board with elements of given list in correct space
def draw_board(elements):
    size = 3 #mutable; 3 for tic tac toe
    index = 0
    while index < size**2:
        print(size * ' ---')
        count = 1
        while count <= size:
            print('| ' + elements[index], end = ' ')
            count += 1
            index += 1
        print('|')
    print(size * ' ---')


#Gameplay

#ask players 1 and 2 for coordinate input and place x's / o's
#in the right position on the gameboard (list of lists)

gameboard = [['_','_','_'],['_','_','_'],['_','_','_']] #initilaizes empty game board with _'s 
board_elements = ['_','_','_','_','_','_','_','_','_'] #puts elements of game board in one list for ease of coding

#list_elements function replaces '_' in board_elements list when a player makes a move
#game ends when there are no more spots to play
#not really necessary; could count number of plays but I can't be arsed to change my code
#if it ain't broke...
def list_elements(board):
        index = 0   #index in board_elements
        for row in board: #iterates through board
                for element in row: #iterates through list element in board
                        board_elements[index] = element
                        index += 1 #increments each time a '_' is replaced


def gameplay():

        print("\n***Let's play Tic Tac Toe!***")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        p1_name = input('Enter your name, player 1: ').title()
        p2_name = input('Enter your name, player 2: ').title()

        print('\nThis is your gameboard:')
        draw_board(board_elements) 
        print()

        #expects users to input coordinates in specific way
        print("Enter coordinates in x,y format\n")

        #while loop continues until someone wins or all spaces are filled if there is no winner
        while '_' in board_elements:

                #prompts player 1 for input until it is valid then places x and prints the gameboard 
                p1 = input("\nWhere would you like to place an 'x', " + p1_name + ": ")
                while not is_valid(p1):
                        p1 = input("\nWhere would you like to place an 'x', " + p1_name + ": ")
                gameboard[int(p1[0])-1][int(p1[2])-1] = 'x'
                list_elements(gameboard)
                draw_board(board_elements)
                #calls check_winner and breaks loop if player 1 placed winning x
                if check_winner(gameboard):
                        print()
                        print(p1_name, 'wins!\n')
                        break   

                #breaks loop if board is full (9 spaces but 10 plays if loop goes 5 times so break before final player 2 prompt)
                if '_' not in board_elements:
                        break

                #prompts player 2 for input until it is valid then places o and prints the gameboard 
                p2 = input("\nWhere would you like to place an 'o', " + p2_name + ": ")
                while not is_valid(p2):
                        p2 = input("\nWhere would you like to place an 'o', " + p2_name + ": ")
                gameboard[int(p2[0])-1][int(p2[2])-1] = 'o'
                list_elements(gameboard)
                draw_board(board_elements)
                #calls check_winner and breaks loop if player 2 placed winning o
                if check_winner(gameboard):
                        print()
                        print(p2_name, 'wins!\n')
                        break

        if not check_winner(gameboard):
                print('\nNo winner.\n')


#error handling function to check that player's input in valid
def is_valid(play):
        try:
                if int(play[0]) >= 1 and int(play[0]) <= 3:
                        if int(play[2]) >= 1 and int(play[2]) <= 3:
                                if gameboard[int(play[0])-1][int(play[2])-1] == '_':
                                        return True
                                else:
                                        print('Space taken.')
                                        return False
                        else:
                                print('Enter integers from 1 to 3.')
                                return False
                else:
                        print('Enter integers from 1 to 3.')
                        return False
        except:
                print('Enter play in x,y format.')
                return False    


#Check Winner

#returns boolean indicating whether or not there was a winner
#could really be a bunch of or's but that would've been a tad clunky

def check_winner(game_board):

    #checks three on a diagonal from left to right
    if (game_board[0][0] == game_board[1][1] and \
    game_board[0][0] == game_board[2][2] and \
    game_board[0][0] != '_'):
        return True 

    #checks three on a diagonal from right to left
    elif (game_board[0][2] == game_board[1][1] and \
    game_board[0][2] == game_board[2][0] and \
    game_board[0][2] != '_'): 
        return True 

    elif True: #always executes two for loops if previous ifs are False
        for list_ in game_board: 
            #checks three in a row 
            if list_[0] == list_[1] and list_[0]== list_[2] and list_[0] != '_': 
                return True

        for index in range(3): 
            #checks three in a column
            if game_board[0][index] == game_board[1][index] and \
            game_board[0][index] == game_board[2][index] and \
            game_board[0][index] != '_': 
                #print('column')
                return True 
       
    return False


gameplay()  