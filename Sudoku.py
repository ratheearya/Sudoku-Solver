# This is a sudoku solver that uses recursion and backtracking.
puzzle = [  
[3,0,5,0,7,1,0,0,9],
[0,0,0,3,4,0,0,0,0],
[0,9,0,2,0,0,0,0,0],
[0,3,0,0,0,4,0,0,0],
[0,6,0,0,0,0,0,0,7],
[0,0,0,0,0,2,8,5,0],
[0,0,0,0,0,0,0,8,0],
[0,5,4,0,0,0,9,0,1],
[0,0,7,0,0,0,4,0,0]] # Uses zeroes to represent unsolved positions on the board

ROW_LENGTH = 9
COL_LENGTH = 9  

def checkForZero(): # traverses through entire pzuzle and returns position where 0 is found
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == 0:
                return (row,col)
    return None #If no 0 is found returns None, board is solved

def possibleNum(row,col):
    availableNums = []
    unAvailableNums = []

    for i in range(ROW_LENGTH): #Adds all numbers in row of position to unavailable number list
        if puzzle[row][i] != 0 and puzzle[row][i] not in unAvailableNums:
            unAvailableNums.append(puzzle[row][i])

    for j in range(COL_LENGTH): #Adds all numbers in the col of the position to unavailable number list
        if puzzle[j][col] != 0 and puzzle[j][col] not in unAvailableNums:
            unAvailableNums.append(puzzle[j][col])
    
    #Since each box is separated after 3 rows we use these equations to find which box the number is in
    boxRow = row // 3 
    boxCol = col // 3

    #Checks all of the numbers in the box and adds all of them into the unavailable numbers list
    for k in range(boxRow * 3,boxRow * 3 + 3):
        for l in range (boxCol * 3, boxCol * 3 + 3):
            if puzzle[k][l] != 0 and puzzle[k][l] not in unAvailableNums:
                 unAvailableNums.append(puzzle[k][l])

    #Checks to see which numbers are possible for the current position
    for z in range(1,10):
        if z not in unAvailableNums:
            availableNums.append(z)
    return availableNums

#formats the puzzle into a more readable format for the user
def displayPuzzle():
    for row in range(len(puzzle)):
        if row % 3 == 0 and row!=0:
            print()
        for col in range(len(puzzle)):
            if col % 3 == 0:
                print(" ",end = '')
            if col % 9 == 0:
                print("")
            print (puzzle[row][col], end = '')
    print()

#Solves the board using backtracking
def solve():
    if checkForZero() == None: #If there are no more zeros then the puzzle is solved
        return solved()
    row,col = checkForZero() #Otherwise the position of the nearest zero is found
    for num in possibleNum(row,col): #Loops through all of the possible numbers
        puzzle[row][col] = num #Tests the number in the list, if we have to backtrack it will try the next number in the list
        if solve():
            return True #Uses recursion to go through each position. 
        puzzle[row][col] = 0 
    return False #If there are no more possible numbers then solve() will return false and the position will be set to 0, meaning the next number will be tried

def solved(): #function is called when there are no more zeros left and puzzle is solved
    displayPuzzle()

if __name__ == "__main__":
    displayPuzzle()
    print()
    print()
    print('SOLVED')
    print('___________')
    solve()
