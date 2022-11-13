
from sudoku import Sudoku
import random

def validPlacement(board,row,column,num):
    '''
    Takes in board as list
    Takes indexes of the row, column being looked at and number being tested as ints
    
    Checks if placement of number is legal returns True if it is, False if it isn't
    '''
    
    if num in board[row]:
        return False
    col = []
    for i in board:
        col.append(i[column])
    if num in col:
        return False
    x = (row//3) * 3
    y = (column//3) * 3 
    for c in range(y , y + 3):
        for r in range(x , x + 3):
            if num == board[r][c]:
                return False
            else:
                pass
    
    return True

def solver(board,row,column):
    
    #When solver reaches end of puzzle (after completing [8][8], return True)
    if row == 8 and column == 9:
        return True
    #When after getting to end of a row, move to start of next row
    if column == 9:
        row += 1
        column = 0
    #If current position has a number assigned, move to the next column in the same row
    if board[row][column] != None:
        return solver(board, row, column +1)
    
    
    for num in range(1, 10):
        #loops between 1-9 checking if placing the number is valid
        if validPlacement(board, row, column, num):
           
            #If placement is valid, assign number
            board[row][column] = num
 
            # Checking for next space by moving to next column
            if solver(board, row, column + 1):
                return True
            
        #If this point is reached, number assignment was invalid and is changed back to NoneType,
        board[row][column] = None
    return False


while True:
    difficulty = -1
    
    while difficulty <= 0 or difficulty >= 1:
        try:
            difficulty = float(input("Enter a difficulty between 0 and 1 \n"))
            
        except ValueError:
            print("Invalid input\n")
    
    
    randseed = random.randrange(0,1000000)
    unsolvedpuzzle = Sudoku(3, seed=int(randseed)).difficulty(difficulty)
    board = unsolvedpuzzle.board
    unsolvedpuzzle.show_full()
    
    input("Press enter to solve puzzle\n\n")
    
    solvedboard = []
    if (solver(board, 0, 0)):
        for i in board:
            solvedboard.append(i)
    else:
        print("no solution  exists")
    
    solvedpuzzle = Sudoku(3,3,board = solvedboard)
    solvedpuzzle.show_full()
    
    print("Another puzzle?")
    repeat = ''
    
    while repeat != 'Y' and repeat != 'N':
        repeat = input("Y for yes or N for no\n").upper()
    
    if repeat == 'Y':
        pass
    else: break