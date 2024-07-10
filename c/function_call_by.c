// Pointers in function call
//                     Two types    
//  call by value                          call by reference


#include <stdio.h>

void square_by_value(int n);
void square_by_reference(int *n);

int main() {
    int number=4;
    // Call by value 
    square_by_value(number);
    // jo ham na number baija woh change howa tha  lakin yahan nahy ho raha reason q ka jab ham call by value karta hain jo value ham function ko pass kar raha haota hain woh variable ki copy hoti ha as lyy neecha wala function main job bhi value change woh asal variable ki value ko effect nhy karta 
    printf("number in main after square when call by value:-  number= %d\n", number);
    
    // Call by reference
    square_by_reference(&number);
    // idhar variable waqi change ho jyy ga q ka as ki exact location baij raha hain jis conatiner main woh store ha
    printf("number in main after square when call by reference:-  number= %d\n", number);
    
    return 0;
}

void square_by_value(int n) {
    n= n*n;
    printf("square when call by value square= %d\n", n);
}  

void square_by_reference(int *n) {
    *n = (*n)*(*n);
    printf("square when call by reference square= %d\n", *n);
} 