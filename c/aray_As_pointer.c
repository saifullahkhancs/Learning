#include <stdio.h>
int main()
{
 int loans[5];
 // input

 int *ptr= &loans[0];

//  while using pointers

 for (int i = 0; i<5 ; i++ ){
 printf("%d index: ", i);
 scanf("%d", (ptr+i));
 }
     for (int i = 0; i<5 ; i++ ){
 printf("%d index = %d\n ", i, *(ptr+i));
     }

//   while using other simple methods

 for (int i = 0; i<5 ; i++ ){
 printf("%d index: ", i);
 scanf("%d", &loans[i]);
 }
     for (int i = 0; i<5 ; i++ ){
 printf("%d index = %d\n ", i, loans[i]);
     }


    return 0;
}
