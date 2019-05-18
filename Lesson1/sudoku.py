# Sudoku Help
# https://knowledge.udacity.com/questions/42154

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:

def check_sudoku(square):
  for row in square:
    check_list = list(range(1, len(square[0]) + 1))
    for i in row:
      if i not in check_list:
        return False
      check_list.remove(i)
    for n in range(len(square[0])):
      check_list = list(range(1, len(square[0]) + 1))
      for row in square:
        if row[n] not in check_list:
          return False
        check_list.remove(row[n])
    return True
    
print(check_sudoku(incorrect))
print(check_sudoku(correct))
print(check_sudoku(incorrect2))
print(check_sudoku(incorrect3))
print(check_sudoku(incorrect4))
print(check_sudoku(incorrect5))
