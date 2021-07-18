# Function for nth Fibonacci number

def Fibonacci(n):
	
	# First Fibonacci number is 0
	if n==0:
	    return 0
	# Second Fibonacci number is 1
	elif n==1:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

k = input("Enter a Number. Do not enter any string or symbol")
try: 
  if(int(k) >=0):
    for i in range(int(k)):
      print(Fibonacci(i))   
  else:
    print("its a negative number")    
except:
  print("Hey stupid enter only number")    



