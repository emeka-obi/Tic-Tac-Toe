""" A wonderful game of tic tac toe!"""

def display_board(board):
    print("\n"*100)
    print("   |   |")
    print(" "  + board[7] +  ' | ' +board[8] + " | " + board[9])
    print("   |   |")
    print("_ _ _ _ _ _")
    print("   |   |")
    print(" " + board[4] +   ' | ' +board[5] + " | " + board[6])
    print("   |   |")
    print("_ _ _ _ _ _")
    print("   |   |")
    print(" " +  board[1] +  ' | ' +board[2] + " | "  + board[3])
    print("   |   |")

def player_input():
    """This function returns a tuple
    for example; player 1, player 2 = player_input()"""
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Do you want to be X or O: ").upper()
        if marker == "X":
            # x = input("Are you ready to play yes or no").lower()
            # if x == 'yes':
            return ("X", "O")
        elif marker == "O":
            return ("O", "X")

def place_marker(board, marker, postion):
    board[postion] = marker
    display_board(board)

# place_marker(board, "$", 8)
def win_check(board, marker):
    """ check the rows on the board
        check the columns
        check the two diagonals and compared all of these to the marker to check if  the player 
        won the game or not"""
    return  (board[1] == marker and board[2]==marker and board[3]== marker) or (board[4]== marker and board[5]== marker and board[6]== marker) or (board[7] == marker and board[8] == marker and board[9] == marker) or (board[1]==marker and board[4]== marker and board[7]==marker)or (board[2]== marker and board[5]== marker and board[8]==marker) or (board[3]== marker and board[6]== marker and board[9]==marker) or (board[1]==marker and board[5]== marker and board[9]== marker) or (board[3]== marker and board[5]== marker and board[7] == marker)
test_board = ["#","X","X","X","X","O","X","O","X","X"]

import random

def plays_first():
    
    player_choosing = random.randrange(1 , 3)
    if player_choosing == 1:
        return "Player 1"
    else:
        return "Player 2"

# test_board = ["#","X","X","X","X","O","X","O","X","X"]
def space_check(board, position):
    return board[position] == " "


def full_board(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def next_position(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not  space_check(board,position):
        position = int(input("Choose your position(1-9): "))
    return position 

def play_again():
    x = input("Are you ready to play? Yes or No: ").capitalize()
    return x == "Yes"
def main():
    print("Welcome to Tic Tac Toe!")
    while True:
        board = [" "]*10
        player_1_marker, player_2_marker = player_input()
        print(player_1_marker, player_2_marker)
        turn = plays_first()
        print(turn + " goes first")

        play_game = input("Do you want to play? Yes or No: ").capitalize()
        if play_game == "Yes":
            game_on = True
        elif play_game == "No":
            game_on = False
        
        #play game
        while game_on:
            if turn == "Player 1":
                # Show the board
                display_board(board)
                position  = next_position(board)
                place_marker(board, player_1_marker, position)
                display_board(board)

                if win_check(board,player_1_marker):
                    display_board(board)
                    print("Player one wins")
                    game_on = False
                else:
                    if full_board(board):
                        display_board(board)
                        print("This is a tie")
                        game_on = False
                    else:
                        turn = "Player 2"
            else:
                display_board(board)
                position  = next_position(board)
                place_marker(board,player_2_marker, position)

                if win_check(board,player_2_marker):
                    display_board(board)
                    print("Player two wins")
                    game_on = False
                else:
                    if full_board(board):
                        display_board(board)
                        print("This is a tie")
                        game_on = False
                    else:
                        turn = "Player 1"
        if not (play_again):
            break  



main()

                
            

    



            






 

   












    

# test_board = ["X"]*10
# display_board(test_board)