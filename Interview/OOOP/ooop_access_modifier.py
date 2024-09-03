# program to illustrate access modifiers of a class

# public members can be accessed outside through the objects
# protected members can be only acccessed through the child objects
# private members can be accessed only in the same class


class Super:   # super class
	
	var1 = None  # public data member

	_var2 = None  # protected data member 
	
	__var3 = None  # private data member
	
	def __init__(self, var1, var2, var3):   # constructor
		self.var1 = var1
		self._var2 = var2
		self.__var3 = var3
		 
	def displayPublicMembers(self):    # public member function

		print("Public Data Member: ", self.var1)   # accessing public data members
		
	def _displayProtectedMembers(self):   # protected member function

		print("Protected Data Member: ", self._var2)  # accessing protected data members
	
	def __displayPrivateMembers(self):     # private member function
		
		print("Private Data Member: ", self.__var3) # accessing private data members  

	def accessPrivateMembers(self):	  # public member function
		
		self.__displayPrivateMembers()  # accessing private member function



class Sub(Super):   # derived class

	def __init__(self, var1, var2, var3):                  # constructor
				Super.__init__(self, var1, var2, var3)
		
	# public member function
	def accessProtectedMembers(self):
				
				self._displayProtectedMembers() #   accessing protected member functions of super class

obj = Sub("Geeks", 4, "Geeks !")  # creating objects of the derived class	


# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
#print(obj.__var3)
