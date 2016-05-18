# BATTLE SHIP GAME
# This is simple game played on Python console.
# Simply run it on the command line:
# >>> python BattleShip.py
# Note that no error handling implemented.
#---------------------------------------------
from random import randint

keepplaying=1

while keepplaying:
    board = []    # Game Board
    board_size = []
    guess_row = []
    guess_col = []
    
    print '\nWelcome to the Battle Ship Game!'
    msj = "How many rows/columns on the board (no more than 10): "
    board_size = int(raw_input(msj))

    for x in range(board_size):
        board.append(["O"] * board_size)

    def print_board(board):
        for row in board:
            print " ".join(row)

    print "\nLet's play Battleship!"
    print "\nHere is the ocean!"
    print_board(board)

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    #Pick a random location for the battleship:
    ship_row = random_row(board)
    ship_col = random_col(board)

    #maximum number of guesses allowed:
    maxg = board_size


    print "\nI picked a battleship location!"
    print "\nYou have %i guesses to find my ship!" % maxg
    print " "


    for turn in range(maxg):    
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))

        if guess_row == ship_row+1 and guess_col == ship_col+1:
            print "Congratulations! You sunk my battleship!"
            board[ship_row][ship_col] = "S"     
            print_board(board)
            break
        else:
            if (guess_row < 1 or guess_row > board_size) or  (guess_col < 1 or guess_col > board_size):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row-1][guess_col-1] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row-1][guess_col-1] = "X"
            
            print 'You used your guess # ' + str(turn+1)
        if turn == maxg-1:
            print "Game Over!"
            board[ship_row][ship_col] = "S"     
            print "\nHere was my ship!"
        print "\n-------------------"
        print_board(board)
			
    #print "\nMy ship was on row %i and on column %i" % (ship_row+1, ship_col+1)
    keepplaying = int(raw_input("Press 1 to play again or Press 0 to exit!\n"))
    
###################################################