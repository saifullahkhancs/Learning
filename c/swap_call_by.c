#include <stdio.h>
void swap(int *ptr_x, int *ptr_y);
int main() {
    int x=3 , y=5;
    printf("values before swap value of x=%d and value of y= %d \n", x,y);
    swap(&x, &y);
    printf("values after swap value of x=%d and value of y= %d", x,y);
    return 0;
}

void swap(int *ptr_x, int *ptr_y) {
    int z;
    int *ptr_z=&z;
    *ptr_z = *ptr_x;
    *ptr_x = *ptr_y;
    *ptr_y = *ptr_z;
}