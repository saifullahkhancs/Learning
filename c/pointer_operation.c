#include <stdio.h>
int main()
{
  int age = 22;
  int *ptr = &age;
  printf("ptr = %u\n" , ptr);
  ptr++;
  // actual main integer ka size sa value bahr jyy gi
  printf("ptr = %u\n" , ptr);
  // aik integer size sa address kam ho ga mean 4 byte
  ptr--;
  printf("ptr = %u\n" , ptr);

    // if float *ptr = increase 4 bytes when add and decrease
    //  4 bytes if ptr is mius
    // if cha *ptr = increase 1 byte when add and decrease
    //  1 bytes if ptr is mius

    // SUBTRACT ONE POINTER FROM OTHER

    int _age = 23;
    int *_ptr = &_age;

    printf("%u , %u the difference between pointer= %u\n", ptr,_ptr,ptr-_ptr );

    printf("comaprison when values different= %u\n", ptr == _ptr);
     // if we make the same value
     _ptr = &age;
    // print when values of the pointer is same
    printf("comaprison when values are same= %u\n", ptr == _ptr);
    return 0;

}
