# NOT COMPLETE YET!


# Minesweeper GAME
# This is simple game played on Python console.
# Simply run it on the command line:
# >>> python MineSweeperGame.py
# Note that no error handling implemented.
#---------------------------------------------
from random import randint

keepplaying=1

while keepplaying:
    board = []    # Game Board
    board_size = []
    guess_row = []
    guess_col = []
    board_size = 9  #9by9 board - fixed
    numMines = 5 #number of mines
    ship_row = [1, 2, 3, 4, 5]
    ship_col = [1, 2, 3, 4, 5]

    
    print '\n Welcome to the Minesweeper Game!'
    print '\n Here is the mine field!'
    print ' I placed %i mines! Let\'s clear them!' % numMines
    print ' '

    # Fill the board with O's:
    for x in range(board_size):
        board.append(["O"] * board_size)


    #Function to print the board on display:
    def print_board(board):
        print '     1 2 3 4 5 6 7 8 9'
        print '     -----------------'
        i=0
        for row in board:
            i +=1
            print ' %i | ' %(i) + " ".join(row)

    print_board(board)


    #Randomly pick 5 locations to place mines:
    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    for i in range(numMines):
        #Pick a random location for the mines
        ship_row[i] = random_row(board)
        ship_col[i] = random_col(board)

    #maximum number of guesses allowed:
    maxg = len(board)*len(board) 

    #Run until maximum number of guesses expire:
    for turn in range(maxg):    
        guess_row = int(raw_input("\n Guess Row:"))
        guess_col = int(raw_input(" Guess Col:"))


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