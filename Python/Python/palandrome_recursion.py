
# A recursive Python program to check whether a given number is palindrome or not
# A recursive function that check a str[s..e] is palindrome or not.

def isPalRec(st, s, e) :	
	
	if (s == e):          # If there is only one character
		return True

	
	if (st[s] != st[e]) :   # If first and last  characters do not match
		return False

	# If there are more than two characters, check if
	# middle substring is also palindrome or not.
	if (s < e + 1) :
		return isPalRec(st, s + 1, e - 1);

	return True

def isPalindrome(st) :
	n = len(st)
 
	if (n == 0) :         	# An empty string is considered as palindrome
		return True
	
	return isPalRec(st, 0, n - 1);


# Driver Code
st = "geeg"
if (isPalindrome(st)) :
	print("Yes")
else :
	print ("No")
