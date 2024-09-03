import  copy

lsit = [1,2,3,4]

print(lsit, "before copy")

shallow_copy = copy.copy(lsit)



# lsit[0][2] = 45
shallow_copy[1] = 10
# deep_copy[3] = 11


print(lsit ,  " i am the orignal list")
print(shallow_copy , "i am shallow copy")
# print(deep_copy , "i am a deep copy ")




