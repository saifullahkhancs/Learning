#include <stdio.h>
int countOdd(int *arr , int  n);
// void countOdd(int arr , int  n); as a value
int main()
{
    int arr[] = {1,2,3,4,5,6};
    printf("%d", countOdd(&arr[0] , 6)); // as a pointer
    //  countOdd(arr , 6);  as a value
    return 0;
}

int countOdd(int *arr , int  n){
//
    int count = 0;
    for (int i=0 ; i<n ; i++){
        if ( *(arr+i) % 2 != 0 )
        // if ( arr[i] % 2 != 0 )
        {
            count++;
        }  
    }
    return count;
}