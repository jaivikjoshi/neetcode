class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = {}
        boxes = {}

        for r in range(len(board)):
            row = {} 

            for c in range(len(board[r])):
                num = board[r][c]

                if num != ".":
                    if num in column and c in column[num]:
                        return False
                    else:
                        if num not in column:
                            column[num] = []
                        column[num].append(c)

                     

                    if num in row:
                        return False
                    else:
                        row[num] = 1
                    

                    box_key = (r // 3, c // 3)

                    if box_key not in boxes:
                        boxes[box_key] = {}

                    if num in boxes[box_key]:
                        return False
                    else:
                        boxes[box_key][num] = 1 

                    
        
        return True
                    

        