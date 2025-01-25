#  Task 8: Count Combinations  
Use nested loops to print all combinations of two dice rolls (1-6) and count how many combinations sum to 7.



count=0
for i in range(1,7):
	for j in range(1,7):
		if(i+j==7):
		   count=count+1
print(count)