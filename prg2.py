def sum_numbers(a,b):
	return int(a)+int(b)

def multiply(a,b):
	return int(a)*int(b)
	
def substract(a,b):
	if int(a)>int(b):
		return a-b
	else:
		return b-a
	
n1 = input ("Enter First No.")
n2 = input ("Enter the Second No.")

n1=int(n1)
n2=int(n2)

#result

print ("The sum is",sum_numbers(n1,n2))
print ("The product is",multiply(n1,n2))
print ("The difference is",substract(n1,n2))
#print ("The sum of {} and {} is {}".format(n1,n2,sum_numbers(n1,n2)))