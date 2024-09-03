#include <stdio.h>
int main()
{
    // character/string with pointer can be changed
    char *canChange = "hello world";
    puts(canChange);
    canChange = "Hello";
    puts(canChange);
    char cannotChange[] = "hello world";
    cannotChange = "hello";
    // character/string with array can not be changed 
 return 0;

}
