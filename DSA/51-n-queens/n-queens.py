class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for _ in range(n)]

        def convertBoard(board):
            return [''.join(row) for row in board]


        def isValid(row,col,board):
            # col check
            for x in range(row):
                if board[x][col] == 'Q':
                    return False
            
            # top left diagonal
            for r,c in zip(range(row,-1,-1),range(col,-1,-1)):
                if board[r][c] =='Q':
                    return False
            
            # top right diagonal
            for r,c in zip(range(row,-1,-1),range(col,n)):
                if board[r][c] =='Q':
                    return False
            return True





        def placeNextQueen(board,row):
            if row == n:
                res.append(convertBoard(board))
            for col in range(n):
                if isValid(row,col,board):
                    board[row][col] = 'Q'
                    placeNextQueen(board,row+1)
                    board[row][col]= '.'

        

        placeNextQueen(board,0)
        return res

        