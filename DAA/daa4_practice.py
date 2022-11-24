global N
N = 4


def solve(board, row, cols=[], bsd=[], sd=[]):
    if row == N:
        for i in range(N):
            for j in range(N):
                print(board[i][j], end="|")
            print()
        print()
        return

    for col in range(N):
        if cols[col] == 0 and bsd[row + col] == 0 and sd[row - col + N - 1] == 0:
            board[row][col] = 1
            cols[col] = 1
            bsd[row + col] = 1
            sd[row - col + N - 1] = 1

            solve(board, row + 1, cols, bsd, sd)

            board[row][col] = 0
            cols[col] = 0
            bsd[row + col] = 0
            sd[row - col + N - 1] = 0


board = []
cols = []
bsd = []
sd = []

for i in range(N):
    temp = []
    for j in range(N):
        temp.append(0)
    board.append(temp)

for i in range(N):
    cols.append(0)
for j in range(2*N - 1):
    bsd.append(0)
    sd.append(0)

solve(board, 0, cols, bsd, sd)
