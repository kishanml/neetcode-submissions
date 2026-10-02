class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        m = len(board)
        n = len(board[0])

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for i in range(m):
            for j in range(n):

                if "." in board[i][j]:
                    continue
                
                if board[i][j] not in rows[i] or\
                   board[i][j] not in cols[j]  or\
                   board[i][j] not in squares[(i//3, j//3)]:
                   
                   rows[i].add(board[i][j])
                   cols[j].add(board[i][j])
                   squares[(i//3, j//3)].add(board[i][j])

                else:
                    return False
        return True
                