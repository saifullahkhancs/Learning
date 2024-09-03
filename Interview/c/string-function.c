#include <stdio.h>
#include <string.h>
int main()
{
    char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    printf("%d", strlen(alphabet));
    
    // we used sizeof to get the size of a string/array. 
    //Note that sizeof and strlen behaves differently, 
    //as sizeof also includes the \0 character when counting
    printf("%d", sizeof(alphabet));   // 27

    // It is also important that you know that sizeof will always return the memory size (in bytes), and not the actual string length:

    char alphabets[50] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    printf("%d", strlen(alphabet));   // 26
    printf("%d", sizeof(alphabet));   // 50

    char str1[20] = "Hello ";
    char str2[] = "World!";

    // Concatenate str2 to str1  (result is stored in str1)
    strcat(str1, str2);

    // Print str1
    printf("%s", str1);

    char strr1[20] = "Hello World!";
    char strr2[20];

    // Copy str1 to str2
    strcpy(strr2, strr1);

    // Print str2
    printf("%s", strr2);
    
    
    
    
    char ster1[] = "Hello";
    char ster2[] = "Hello";
    char ster3[] = "Hi";

    // Compare str1 and str2, and print the result
    printf("%d\n", strcmp(ster1, ster2));  // Returns 0 (the strings are equal)

    // Compare str1 and str3, and print the result
    printf("%d\n", strcmp(ster1, ster3)); 
// Returns -4 (the strings are not equal and it is smaller)
// ascii values are comapred when there is first difference
// so between Hello and Hi e and i compared and the difference is 4 ascii
// values thats and i is greater then e so it is negative value
    
    
    return 0;

}