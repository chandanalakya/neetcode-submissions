class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            s=set()
            for j in range(len(board[0])):
                if board[i][j]!="." and board[i][j] not in s:
                    s.add(board[i][j])
                elif board[i][j]!="." and board[i][j] in s:
                    return False
        for j in range(len(board[0])):
            s=set()
            for i in range(len(board)):
                if board[i][j]!="." and board[i][j] not in s:
                    s.add(board[i][j])
                elif board[i][j]!="." and board[i][j] in s:
                    return False
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                s=set()
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j]!="." and board[i][j] not in s:
                            s.add(board[i][j])
                        elif board[i][j]!="." and board[i][j] in s:
                            return False
        return True  



