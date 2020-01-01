class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [[set() for x in range(3)] for y in range(3)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != "." and (num in columns[i] or num in rows[j] or num in boxes[i//3][j//3]):
                    return False
                columns[i].add(num)
                rows[j].add(num)
                boxes[i//3][j//3].add(num)
        
        return True
