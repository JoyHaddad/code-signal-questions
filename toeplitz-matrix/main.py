from typing import List

def is_toeplitz(matrix: List[List[int]]) -> bool:
   
   length = len(matrix)
   
   for i in range(length - 1, -1, -1):
      for j in range(length - 1, -1, -1):
         for count in range(1, length + 1, 1):
            if i + count >= length or j + count >= length:
               break
            if matrix[i][j] != matrix[i + count][j + count]:
               return False
      
   return True
   # [last][last]
   # [second to last][second to last]
   # [third to last][third to last]
   
   
