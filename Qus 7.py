#  Task 7: Triangle Pattern  
   Print this pattern:  
        *  
       ***  
      *****  
     ******* 


n = int(input("Enter the value:"))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
         print('*', end='')
    print() 