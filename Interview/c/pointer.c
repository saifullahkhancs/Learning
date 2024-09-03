#include <stdio.h>

int main() {
    // Write C code here
    // int *ptr = &age <----  int age = 22
    // char *ptr= &star <--- char star = "*"
    // float *ptr= &price <---  float price = 10000
    int age =22;
    int *ptr= &age;
    int _age = *ptr; // new variable

    char chp[] = "ali";

   // char chp = "ali";
    // printf("my name is %c\n", *(chp+1));

    char *cp = &chp;
    printf("my name is %s\n", cp);

    
    
    printf("%d", _age);

    // how to print a pointer address
    printf("%p\n" , &age);   // hexadecimal value
    printf("%u\n" , ptr);   // unsigned integer value show the addre in the number  format
    printf("%u\n" , &age);  // adress of the pointer

     // how to print vlaue of a pointer
    
    printf("%d\n", age);  // normal
    printf("%d\n", *ptr); // value at pointer
    printf("%d\n", *(&age)); // pointing the address of the variable
    
    return 0;
}