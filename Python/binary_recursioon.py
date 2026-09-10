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
def decToBinary(n):          #   25 ,,,,   12  ,,, 6 ,,, 3 ,,, 1
	if n > 1:
		decToBinary(n//2)    #   12 ,,,    6 ,,,, 3 ,,, 1
	print(n % 2, end = '')   #   first n=25 print(1)  ,,,, 2nd n=12 print(0)  ,,,, 3rd n=6 print(0)  ,,,, 4th n=3 print(1)  ,,,, 5th n=1 print(1)

	# so the answer was 11001
	# it will become  2^4 + 2^3 + 2^0 = 16 + 8 + 1 = 25

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