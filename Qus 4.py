#  Task 4: Table of Multiplication  
Generate a multiplication table for numbers 1 to 5 using nested loops:  
1 x 1 = 1  
1 x 2 = 2  
...  
5 x 5 = 25




for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
