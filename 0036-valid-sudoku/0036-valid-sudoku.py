class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checked = set()
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                box = (r // 3, c // 3)
                row = ("row", r, num) 
                col = ("col", c, num) 
                checkbox = ("box", box, num) 
                if row in checked or col in checked or checkbox in checked:
                    return False
                checked.add(row)
                checked.add(col)
                checked.add(checkbox)
        return True
                