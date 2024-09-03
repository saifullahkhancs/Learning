/*  ___malloc()____  :- memory allocation
            takes number of bytes to be allocated & return
            a pointer of type VOId

            ptr= (*int)malloc(  5*sizeof(int) )
                typecast           5*4         = 20
        it only take single parameter which is size of memory
        for our own ease we multiply it with size of int becasue we
        need memory in our code to allocate memory ti 5 integers
            

                int type ka pointer mail gyy ha jis main
                20 ki memory i tarf point kar raha ha

    __calloc()___    :- continious memory allocation
            intilizes with 0  and return void pointer

        ptr= (*int)calloc(     5,               sizeof(int))
                        number of locations           per location size

    it has two parameeter one is number of blocks or numebr 
    of memory locations , and second is per size memory allocation
        

*/

#include <stdio.h>
#include <stdlib.h>

int main(){
   /* printf("%d\n", sizeof(int));
    printf("%d\n", sizeof(float));
    printf("%d\n", sizeof(char));  */

    int *ptr;
    ptr = (int*) malloc(5 * sizeof(int));

    ptr[0]= 1;
    ptr[1]= 4;
    ptr[2]= 8;
    ptr[3]=10;
    ptr[4]=12;

    for (int i=0; i<5; i++){
        printf("%d\n", ptr[i]);}



    float *ptr1;
    ptr1 = (float*) calloc(5, sizeof(int));

    for (int i=0; i<5; i++){
        printf("%f\n", ptr1[i]);
    }

    free(ptr1);

    ptr1 = (float*) calloc(2, sizeof(int));
    printf("after using freee \n");

    for (int i=0; i<2; i++){
        printf("%f\n", ptr1[i]);
    } 



    return 0;
}