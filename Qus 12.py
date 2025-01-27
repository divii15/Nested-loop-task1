#  Task 12: Prime Numbers Grid  
Generate all prime numbers up to 50 and display them in a grid format using nested loops and gives output as even numbers




count=0
for i in range(1,51):
	isDivide=False
	for j in range(2,i):
		if(i%j==0):
		    isDivide=True
		    break
	if(not isDivide):
	    count=count+1
	    if i % 2 != 0:
	        print(i," is a prime number")