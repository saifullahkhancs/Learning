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
