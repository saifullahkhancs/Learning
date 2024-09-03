#include <stdio.h>
int main()
{
 
 char c1 = 'a', c2= 'b' , c;
 unsigned char uc;
 c = c1+c2;
 uc = c1 + c2;
 
 if (c > 'c') 
 {
    printf("True \n");
 }
 else{
    printf("False \n");
 }
  if (uc > 'c') 
 {
    printf("True \n");
 }
 else{
    printf("False \n");
 }




 return 0;
}

/*
a --> 97 , b --> 98, c--> 97+98=195; c-->195
c--> 99
if (195 > 99) --> True

*/