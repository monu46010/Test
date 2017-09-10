## This program is to perform addition of two numbers

def sum_numbers(a,b):
	return int(a)+int(b)

def division(a,b):
	if a>b:
		return a/b
	else:
		return b/a

def multiply(a,b):
	return int(a)*int(b)
	
n1 = input ("Enter First No.")
n2 = input ("Enter the Second No.")
n1 = int(n1)
n2 = int(n2)

#Resultfromgit


print ("The sum is",sum_numbers(n1,n2))
print ("Division result",division(n1,n2))
print ("The product is",multiply(n1,n2))


print ("The sum of {} and {} is {}".format(n1,n2,sum_numbers(n1,n2)))
