""" Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
 """

[current_row, current_col] = [None, None]

import line_profiler
import atexit

profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)

import pprint
class Solution:
    #@profile
    def safeToAssign(self, board, row, col, num):
      # check if it is safe to insert into the cell at [row][col].
      # the checking rule is it shouldn't introduce multiple number instance in the same row/col/box
      if (num not in board[row] and num not in list(zip(*board))[col]):
        small_box_row = row // 3 * 3
        small_box_col = col // 3 * 3
        return (num not in (board[small_box_row][small_box_col:small_box_col+3] + 
                   board[small_box_row+1][small_box_col:small_box_col+3] +
                   board[small_box_row+2][small_box_col:small_box_col+3]))
      return False

    #@profile
    def recurSolve(self, board, row, col):
      # find unassinged cells,
      # if no cell is empty, we are done, print the new soduku and return True.
      # if still have cell that is empty:
      #   check if the cell is safe to insert with num
      #       if not safe, meaning it will cause conflict, we should return False - backtracking to the parent level on the search tree
      #       if safe, just assign this value and recursive search the solution
      [row, col] = self.findUnassigned(board, row, col)
      # print("find empty cell {} {}".format(row, col))
      if row is not None:
        # we found one unassigned cell
        for num in range(1, 10):
          # print("trying num {}".format(num))
          if self.safeToAssign(board, row, col, str(num)):
            board[row][col] = str(num)
            # pprint.pprint(board)
            if self.recurSolve(board, row, col) == False:
              board[row][col] = '.'
              # pprint.pprint(board)
            else:
              return True
        return False
    #@profile
    def findUnassigned(self, board, row, col):
      if col == 9:
        col = 0
        row = row + 1
      if col == 0 and row == 9:
        return [None, None]
      if board[row][col] == '.':
        return [row, col]
      else:
        return self.findUnassigned(board, row, col+1)
      # return [None, None] # means no unassigned cell.
    
    #@profile
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.recurSolve(board, 0, 0)
        # print("solved")
        

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

board = [[".",".","9","7","4","8",".",".","."],
  ["7",".",".",".",".",".",".",".","."],
  [".","2",".","1",".","9",".",".","."],
  [".",".","7",".",".",".","2","4","."],
  [".","6","4",".","1",".","5","9","."],
  [".","9","8",".",".",".","3",".","."],
  [".",".",".","8",".","3",".","2","."],
  [".",".",".",".",".",".",".",".","6"],
  [".",".",".","2","7","5","9",".","."]]

sol.solveSudoku(board)
pprint.pprint(board)