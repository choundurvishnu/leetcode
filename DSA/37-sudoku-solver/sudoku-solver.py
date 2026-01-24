class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        # Initialize masks
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    num = int(board[r][c])
                    mask = 1 << num
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + (c // 3)] |= mask

        def backtrack():
            if not empty:
                return True

            # MRV heuristic
            empty.sort(key=lambda x: bin(
                ~(rows[x[0]] | cols[x[1]] | boxes[(x[0] // 3) * 3 + (x[1] // 3)]) & 0x3FE
            ).count("1"))

            r, c = empty.pop(0)
            box = (r // 3) * 3 + (c // 3)
            available = ~(rows[r] | cols[c] | boxes[box]) & 0x3FE

            while available:
                bit = available & -available
                num = bit.bit_length() - 1

                board[r][c] = str(num)
                rows[r] |= bit
                cols[c] |= bit
                boxes[box] |= bit

                if backtrack():
                    return True

                # Undo
                board[r][c] = "."
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[box] ^= bit

                available ^= bit

            empty.insert(0, (r, c))
            return False

        backtrack()


"""     
        #Apprach 2 using hashmaps to store the values in each row, column and box respectively


        boxes = [{} for _ in range(9)]
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
    
        def getBox(row,col):
            new_c = col //3
            new_r = (row//3)*3
            return new_c + new_r
    
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    value = board[i][j]
                    x = getBox(i,j)
                    boxes[x][value]=True
                    rows[i][value]=True
                    cols[j][value]=True
    
        def isValid(box,row,col,num):
            if (num in box) or (num in row) or (num in col):
                return False
            return True    
    
        def solveBacktrack(board,boxes,rows,cols,r,c):
            if r==9 :
                return True 
            if board[r][c]=='.':
                box = getBox(r,c)
                for num in range(1,10):
                    numVal = str(num)
                    boxId = getBox(r,c)
                    box = boxes[boxId]
                    row = rows[r]
                    col=cols[c]
                    if (isValid(box,row,col,numVal)):
                        board[r][c]= numVal
                        box[numVal]=True
                        row[numVal]=True
                        col[numVal]=True
                        if c==8:
                            if(solveBacktrack(board,boxes,rows,cols,r+1,0)):return True
                        else:
                            if(solveBacktrack(board,boxes,rows,cols,r,c+1)):return True    
                        #backtrack
                        del box[numVal]
                        del row[numVal]
                        del col[numVal]
                        board[r][c]='.'
                return False
            else:
                if c==8:
                    if(solveBacktrack(board,boxes,rows,cols,r+1,0)):return True
                else:
                    if(solveBacktrack(board,boxes,rows,cols,r,c+1)):return True
    
        solveBacktrack(board,boxes,rows,cols,0,0) 
"""

"""
---- Approach 1---------
        def isValid(num,row,col):
            for x in range(9):
                #Column Check
                if board[x][col]==num:
                    return False
                if board[row][x]==num:
                    return False
                
                r = 3*(row//3)+x//3
                c = 3*(col//3) + x%3
                if board[r][c] == num:
                    return False
            return True

        
        def fillTheBoard(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if isValid(num, row,col):
                                board[row][col]= num
                                if(fillTheBoard(board)):
                                    return True
                                board[row][col] = '.' #backtracking
                        return False

            return True
        fillTheBoard(board)
"""