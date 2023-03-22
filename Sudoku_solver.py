board =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0],
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0]]
ROWS = len(board)
COLS = len(board[0])
def next_box():
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 0:
                return (i,j)
    return None

def print_board(mat):
    for i in range(len(mat)):
        if i%3  == 0 and i!=0:
            print("-"*24)
        for j in range(len(mat[0])):
            # if i%3 == 0:
            #
            #     print("--------------------",end="")
            if j%3 == 0 and j!=0:
                print(" | ",end="")
            print(mat[i][j],end=" ")
        print()

def is_valid(row,col):
    cnum = board[row][col]
    subr = row//3
    subc = col//3
    for i in range(COLS):
        if i == col: continue
        # print(board[row][i],"---")
        if board[row][i] == cnum: return False
    for i in range(ROWS):
        if i == row: continue
        # print(board[i][col],"***")
        if board[i][col] == cnum: return False
    for i in range(subr*3,(subr*3)+3):
        for j in range(subc*3,(subc*3)+3):
            if i== row and col==j: continue
            # print(board[i][j],end=" ")
            if board[i][j] == cnum:return False
    return True
print_board(board)
def solver(tempboard):
    if next_box() == None:
        # print_board(tempboard)
        return True
    temprow,tempcol = next_box()
    for i in range(1,10):
        tempboard[temprow][tempcol] = i
        if is_valid(temprow,tempcol):
            if solver(tempboard):
                return True

        tempboard[temprow][tempcol] = 0
    return False
solver(board)
print("**************************************")
print_board(board)
