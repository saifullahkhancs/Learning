# Selection Sort 
# the approch used above is to sort the array buy comparing the elemnt with all other elemnt
lists = ["a","s","d","f","g","h","j","k","l","q","w","e","r","t","y","u"]
for i in range(len(lists)):
    mimi = lists[i]
    index = i
    for j in range(i , len(lists) ):
        if mimi > lists[j]:
            mimi = lists[j]
            index = j
    lists[i] , lists[index] = lists[index] ,lists[i]
print(lists)

# Bubble Sort
# compare and swap the adjecent indexes
listss = ["a","s","d","f","g","h","j","k","l","q","w","e","r","t","y","u"]
for i in range(len(listss)):  
    for j in range(i,len(listss)):
        if listss[i] > listss[j]:
            listss[i] , listss[j] = listss[j] , listss[i] 

print(listss)

# Insertion Sort
# two arrays one is sorted other is unsorted 
# move the elemnt from the sorted to the unsorted
listss = ["a","s","d","f","g","h","j","k","l","q","w","e","r","t","y","u"]
for i in range(1 , len(listss)):  
    key =  listss[i]
    j = i-1
    while j>0 and key < listss[j]:
        listss[j+1] = listss[j]    # the 3 steps is for swapping the element
        j = j-1
        listss[j + 1] = key
print(listss)
