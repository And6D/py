# Tic-Tac-Toe
# Plays the game of tic-tac-toe against a human opponent
# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
 """Display game instructions."""
 print(
 """
 Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
 This will be a showdown between your human brain and my silicon processor.
 You will make your move known by entering a number, 0 - 8. The number
 will correspond to the board position as illustrated:
                         0 | 1 | 2
                         ---------
                         3 | 4 | 5
                         ---------
                         6 | 7 | 8
     
 Prepare yourself, human. The ultimate battle is about to begin. \n
 """
 )