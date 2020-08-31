""" Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9. 

Need a command function to check if upto 9 digits are unique.

"""

# import numpy as np
class Solution:
  def check_dup_from_9_elements(self, list):
    temp_dict = dict()
    for ele in list:
      if ele != '.':
        if temp_dict.get(ele) != None:
          return False
        else:
          temp_dict[ele] = True
    return True
  
  def isValidSudoku(self, board) -> bool:
    for j in board:
      if self.check_dup_from_9_elements(j) == False:
        return False
    
    transposed = zip(*board) # this is really a good way to transpos a 2nd array
    for i in transposed:
      if self.check_dup_from_9_elements(i) == False:
        return False
    
    for board_index in range(len(board[0])):
      #print(index)
      #find out each small sub-box
      box_to_list = []
      board_row_index = (board_index // 3)*3
      board_col_index = (board_index % 3)*3
      # print([board_row_index, board_col_index])
      box_to_list = board[board_row_index][board_col_index:board_col_index+3] + board[board_row_index+1][board_col_index:board_col_index+3] + board[board_row_index+2][board_col_index:board_col_index+3]
      if self.check_dup_from_9_elements(box_to_list) == False:
        return False
    return True


sol = Solution()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(sol.isValidSudoku(board))