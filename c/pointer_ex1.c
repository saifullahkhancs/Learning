// Online C compiler to run C program online
#include <stdio.h>

int main() {
   int x;
   int *ptr;
   
   ptr = &x;
   *ptr = 0;
   
   printf( "x = %d\n" , x); // 0
   printf( "*ptr = %d\n" , *ptr);
   
   *ptr = *ptr + 5;
   printf( "x = %d\n" , x);
   printf( "*ptr = %d\n" , *ptr);
   
   (*ptr)++;  // incrementing the value of the pointer conating address the variable
      printf( "x = %d\n" , x);
   printf( "*ptr = %d\n" , *ptr);
   
    return 0;
}