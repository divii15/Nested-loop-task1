#  Task 5: Matrix Addition  
Write a program to add two 2D matrices using nested loops.



val1 = [[12,7],
        [4,5],
        [7,8]]
val2 = [[5,8],
        [6,7],
        [4,5]]
result = [[0,0],
          [0,0],
          [0,0]]
for i in range(len(val1)):
   for j in range(len(val1[0])):
       result[i][j] = val1[i][j] + val2[i][j]
for k in result:
   print(k)