# Python3 code for decimal to binary
# conversion using recursion

# Decimal to binary conversion
# using recursion
def find( decimal_number ):
	if decimal_number == 0:
		return 0
	else:
		return (decimal_number % 2 + 10 * find(int(decimal_number // 2)))

# Driver Code
decimal_number = 25
print(find(decimal_number))

# This code is contributed
# by "Sharad_Bhardwaj"

# another way to do the same thing
def decToBinary(n):
	if n > 1:
		decToBinary(n//2)
	print(n % 2, end = '')

number= 25
decToBinary(number)

print()  # for new line after the binary output

def decToBinary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decToBinary(n // 2) + str(n % 2)

number = 25
binary_number = decToBinary(number)
print(binary_number)   # Output: 11001


# binary_number = ""

# def decToBinary(n, binary_number):
# 	if n > 1:	
# 		n = decToBinary(n//2 , binary_number)
# 	binary_number += str(n % 2)	
# 	return binary_number

# number= 25
# decToBinary(number, binary_number)
# print(binary_number)