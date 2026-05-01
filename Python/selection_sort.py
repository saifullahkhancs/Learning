def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        min = arr[i]
        index = i
        minj = min
        for j in range(i, n):      
            if minj > arr[j]:
                minj  = arr[j] 
                index = j 
        arr[i] , arr[index]= arr[index] , arr[i] 
        print(arr)
        


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
  
    bubbleSort(arr)
  
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end="\n ")