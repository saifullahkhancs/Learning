#include <stdio.h>
void printNumbers(int *arr , int  n);
void reverse(int *arr , int  n);

int main()
{
    int arr[] = {1,2,3,4,5,6};
    printNumbers(&arr[0] , 6); // as a pointer
    printf("after reverse \n");
    //  printNumbers(arr , 5);  as a value
    reverse(&arr[0] , 6);
    printNumbers(&arr[0] , 6); // as a pointer
    return 0;
}


void reverse(int *arr , int  n){
    for (int i= 0 ; i<n/2; i++){
        int firstValue = *(arr+i);
     //   printf(" the first reverse value is =%d\n", firstValue);
        int secondValue = *((arr+n)-i-1);
       // printf(" the second reverse value is =%d\n", secondValue);
        arr[i] = secondValue;
        
        arr[n-i-1] = firstValue; }
}
void printNumbers(int *arr , int  n){
    for (int i=0 ; i<n ; i++){
        printf("%d \t", *(arr+i)); // as a pointer
    //  printf("%d \t", arr[i]);  as a value       }
    printf("\n"); }
}
