# Task 6: Transpose of a Matrix  
Use nested loops to compute the transpose of a 3x3 matrix.




val=[[1,2,3],
     [9,6,4],
     [5,7,2]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
        
for i in range(len(val)):
    for j in range(len(val[0])):
        result[j][i]=val[i][j]
for k in result:
    print(k)