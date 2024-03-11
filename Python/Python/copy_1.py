import  copy

lsit = [1,2,3,4]


shallow_copy = copy.copy(lsit)
deep_copy = copy.deepcopy(lsit)


lsit[2] = 45

shallow_copy[1] = 10
deep_copy[3] = 11


print(lsit)

print(shallow_copy , "i am shallow copy")
print(deep_copy , "i am a deep copy ")




