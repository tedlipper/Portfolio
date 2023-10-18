"""
The number board is as follows
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
"""

# Sets a dictionary to assign a number to each of the nine squares on the board
# This allows me to assign each of the squares an X or an O individually
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
a = '            1 | 2 | 3 '
b = '            4 | 5 | 6 '
c = '            7 | 8 | 9 '


# Prints the board and the number board next to it
def print_board(board):
    print(board['1'] + '  | ' + board['2'] + ' | ' + board['3'] + a)
    print('---+---+---          ---+---+---')
    print(board['4'] + '  | ' + board['5'] + ' | ' + board['6'] + b)
    print('---+---+---          ---+---+---')
    print(board['7'] + '  | ' + board['8'] + ' | ' + board['9'] + c)


# A list of possible moves so the program can handle improper input
possible_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# I named the function this because alex kept giving improper input whenever
# He was about to lose so the program would break
def re_ask_the_question_until_alex_gives_up():
    print("Invalid input")
    move = input("Input must be a number 1 through 9")
    if move in possible_moves:
        return move
    else:
        re_ask_the_question_until_alex_gives_up()


# Starts the game
def game():
    # Setting the variables
    count = 0
    player_turn = 'X'
    # For loop
    for i in range(10):
        # Prints the board
        print_board(theBoard)
        # Says whose turn it is
        print("")
        print("It's your turn " + player_turn + ".")
        # Asks for input
        move = input()
        # Checks if the input is valid
        if move in possible_moves:
            # Checks if the space is unfilled
            if theBoard[move] == ' ':
                # Fills the square if it's available
                theBoard[move] = player_turn
                # Makes the turn counter go up
                count += 1
            # Makes you give another input if the square is taken
            else:
                print("That place is already filled.\nMove to which place?")
                continue
        # If the input is invalid it will make you do it again
        else:
            move = re_ask_the_question_until_alex_gives_up()
            if theBoard[move] == ' ':
                theBoard[move] = player_turn
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue
        # The absurd amount of win conditions
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                # across the top
                print_board(theBoard)
                print("\nGame Over.\n")
                print(" **** " + player_turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                # across the middle
                print_board(theBoard)
                print("\nGame Over.\n")
                print(" **** " + player_turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                # across the bottom
                print_board(theBoard)
                print("\nGame Over.\n")
                print(" **** " + player_turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                # down the left side
                print_board(theBoard)
                print("\nGame Over.\n")
                print(" **** " + player_turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                # down the middle
                print_board(theBoard)
                print("\nGame Over.\n")
                print(" **** " + player_turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                # down the right side
                print_board(theBoard)
                print("\nGame Over.\n")
                print(" **** " + player_turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                # diagonal top right to bottom left
                print_board(theBoard)
                print("\nGame Over.\n")
                print(" **** " + player_turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                # diagonal top left to bottom right
                print_board(theBoard)
                print("\nGame Over.\n")
                print(" **** " + player_turn + " won. ****")
                break

                # If neither X nor O wins and the board is full
                # We'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if player_turn == 'X':
            player_turn = 'O'
        else:
            player_turn = 'X'


game()
