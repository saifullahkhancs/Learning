// pointer to pointer 
//                  a variable that strores the memory address of another pointer.
#include <stdio.h>

int main() {
        // int **ptr 
    // char **pptr
    // float **pptr 
    // char **star
   
   float price = 10000;
   float *pr = &price;
   float **prr = &pr;
   
   // print the value of i(any number) from its pointer to pointer
   printf("%f\n", **prr);  // normal
   printf("%d\n", *pr);
   
    return 0;
}