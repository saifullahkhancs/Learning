#include <stdio.h>

// declaration of array
int main() {
    int myNumbers[] = {25, 50, 75, 100};
    // accesses the value of the first element [0] in myNumbers:
    printf("%d  first number of array\n", myNumbers[0]);

    //Change an Array Element
    myNumbers[0] = 33;
     printf("%d changed 1st num \n", myNumbers[0]);

    //  Loop Through an Array
    int i;

    for (i = 0; i < 4; i++) {
        printf("%d\n", myNumbers[i]);
    }

    // Declare an array of four integers:
    int myNumber[4];

    // Add elements
    myNumber[0] = 25;
    myNumber[1] = 50;
    myNumber[2] = 75;
    myNumber[3] = 100;

    printf("%d\n", myNumber[0]);

    // two dimensional arrays

    int matrix[2][3] = { {1, 4, 2}, {3, 6, 8} };
    printf("%d", matrix[0][2]);  // Outputs 2
    // change the element
    matrix[0][0] = 9;
    printf("%d", matrix[0][0]);  // Now outputs 9 instead of 1
    // loop through/print  the 2d array
    int j;
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 3; j++) {
            printf("%d\n", matrix[i][j]);
        }
    }

return 0;
}