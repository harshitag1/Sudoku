import random

def complete_solution(grid):
    numbers = [1,2,3,4,5,6,7,8,9]
    for i in range(0,81):
        x = i//9
        y = i%9
        if grid[x][y]==0:
            random.shuffle(numbers)
            for num in numbers:
                if(checkValid(x,y,grid,num)):
                    grid[x][y] = num
                    if findEmptyloc(grid) == (-1, -1):
                        return True
                    else:
                        if complete_solution(grid):
                            return True
                        grid[x][y]=0
            break
    return False

def NumberOfSolutions(grid):
    count = 0
    numbers = []
    for i in range(0,9):
        numbers.append(i+1)
    x,y = findEmptyloc(grid)
    if (x,y)==(-1,-1):
        return 0
    random.shuffle(numbers)
    for num in numbers:
        if checkValid(x,y,grid,num):
            grid[x][y]=num
            grid1 = [row[:] for row in grid]
            #printSudoku(grid1)
            if complete_solution(grid1):
                count=count+1
                if count!=1:
                    return count

        grid[x][y]=0
    return count


def removeNumbers(grid):
    listNonEmpty = [(i,j) for i in range(0,9) for j in range(0,9)]
    rounds = 3
    nonEmptylength = len(listNonEmpty)
    while rounds > 0 and nonEmptylength >= 17:
        randNum = random.randint(0,len(listNonEmpty)-1)
        x,y = listNonEmpty.pop(randNum)
        nonEmptylength-=1
        box = grid[x][y]
        grid[x][y]=0
        grid1 = [row[:] for row in grid]
        count = NumberOfSolutions(grid1)
        if count>1:
            grid[x][y]=box
            nonEmptylength+=1
            rounds-=1
    return


def generator():
    grid = [[0 for i in range(9)] for j in range(9)]
    complete_solution(grid)
    grid1 = [row[:] for row in grid]
    removeNumbers(grid)
    return grid

def findEmptyloc(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return (i, j)
    return (-1, -1)

def checkValid(row, col, grid, num):
    for i in range(9):
        if grid[row][i] == num and col != i:
            return False
    for i in range(9):
        if grid[i][col] == num and row!=i:
            return False
    x= (row - row%3)
    y= (col - col%3)
    for i in range(3):
        for j in range(3):
            if(grid[x+i][y+j]==num and (x+i)!= row and (y+j)!= col):
                return False
    return True

def printSudoku(grid):
    for i in range(len(grid)):
        if i%3 == 0:
            print("-------------------")
            
        for j in range(len(grid[0])):
            if j%3 == 0:
                print("\b|", end ="")
            
            print(str(grid[i][j])+" ", end="")
        print("\b|")
    print("-------------------")

def SudokuSolver(grid):
    (x, y)=findEmptyloc(grid)
    if (x, y) == (-1, -1):
        return True
    for i in range(1, 10):
        if checkValid(x, y, grid, i):
            grid[x][y]=i
            if SudokuSolver(grid):
                return True
            grid[x][y]=0
    return False


def enter_sudoku():
    more_input=True
    sudoku = [[0 for i in range(9)] for j in range(9)]
    printSudoku(sudoku)
    while(more_input==True):
        row = int(input("Enter row number (0-8): "))
        col = int(input("Enter column number (0-8): "))
        num = int(input("Enter number to be inserted at this location: "))
        if checkValid(row, col, sudoku, num):
            sudoku[row][col] = num
            sudoku1 = [row[:] for row in sudoku]
            if complete_solution(sudoku1):
                printSudoku(sudoku)
        else:
            sudoku[row][col]=0
            print("\nNot a valid input!\n")
            printSudoku(sudoku)
        z = int(input("1. Press 1 to enter more numbers \n2. Press 2 to solve sudoku \n"))
        if z==2:
            more_input = False
            complete_solution(sudoku)
            printSudoku(sudoku)

def user_solve(sudoku):
    user_attempt = False
    while user_attempt == False:
        row = int(input("Enter row number (0-8): "))
        col = int(input("Enter column number (0-8): "))
        num = int(input("Enter number to be inserted at this location: "))
        if sudoku[row][col]!=0:
            print("\n\nPosition already filled!\n\n")
        else:
            sudoku[row][col] = num
            sudoku1 = [row[:] for row in sudoku]
            if checkValid(row, col, sudoku, num) and complete_solution(sudoku1):
                printSudoku(sudoku)
            else:
                sudoku[row][col]=0
                print("\nIncorrect input!!\n")
                printSudoku(sudoku)
        z = int(input("1. Press 1 to solve this Sudoku \n2. Press 2 to display Solved Sudoku \n"))
        if z==2:
            complete_solution(sudoku)
            printSudoku(sudoku)
            user_attempt = True
        elif z==1:
            continue
    

def auto_generate():
    sudoku = generator()
    printSudoku(sudoku)
    z = int(input("1. Press 1 to solve this Sudoku \n2. Press 2 to display Solved Sudoku \n"))
    if z==2:
        complete_solution(sudoku)
        printSudoku(sudoku)
    elif z==1:
        user_solve(sudoku)
print("""

   _____   _    _   _____     ____    _  __  _    _ 
  / ____| | |  | | |  __ \   / __ \  | |/ / | |  | |
 | (___   | |  | | | |  | | | |  | | | ' /  | |  | |
  \___ \  | |  | | | |  | | | |  | | |  <   | |  | |
  ____) | | |__| | | |__| | | |__| | | . \  | |__| |
 |_____/   \____/  |_____/   \____/  |_|\_\  \____/ 
                                                    
                                                    
""")
print("\n\nWelcome to Sudoku Solver Game!\n\n")
valid_input=False
while(valid_input==False):
    x = int(input("1. Press 1 to display a Sudoku to solve \n2. Press 2 to enter the digits of the Sudoku \n"))
    if x==1:
        auto_generate()
        valid_input = True
        print("\n\nThank You!!\n\n")
    elif(x==2):
        enter_sudoku()
        valid_input = True
        print("\n\nThank You!!\n\n")
    else:
        print("Wrong Input! Please Enter valid input...")
