## This program is to perform addition of two numbers

def sum_numbers(a,b):
	return int(a)+int(b)
	
n1 = input ("Enter First No.")
n2 = input ("Enter the Second No.")

print (sum_numbers(n1,n2))
print ("The sum of {} and {} is {}".format(n1,n2,sum_numbers(n1,n2)))