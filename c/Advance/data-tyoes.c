// to write a program Minimum & Maximum value for Short Data Types
 #include <stdio.h>

 void method1(void);

int main()
{

    method1();
   
    return 0;
}

void method1(void){
    short s;
    short tmp;
    s = 0;
    tmp = s - 1;

// loop to calculate the max value of a short datatype
    while(s > tmp)  {
        s++;
        tmp++;    }
    printf("Max value for Short Data Type (signed ) is %d\n", tmp);  
}

/*
    short data types : 2 bytes:  16 bits of data
                    1111 1111 1111 1111
                    0000 0000 0000 0000
    signed data   0\1(msb), 15-bits, maximum

*/