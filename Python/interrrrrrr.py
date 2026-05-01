# if __name__ == '__main__':
#     n = int(input())
#     array =input().split()
#     arr= []
#     for i in array:
#         arr.append(int(i))
#     for i in range(len(arr)):
#         max = arr[i]
#         index = i
#         for j in range(i , len(arr)):
#             if max<arr[j]:
#                 max = arr[j]
#                 index = j
#         arr[i],arr[index] = arr[index] , arr[i]
        
#     print(arr)
#     index = 0    
#     while arr[index] == arr[index+1]:
#         index = index+1
            
#     print(arr[index+1])
    
        
from copy import copy
a = ['aa','bb','cc']
b = copy(a)

b[0] = 'wer'

print(a.index)
print(b)