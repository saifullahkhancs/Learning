#include <stdio.h>
int main()
{
  // gets and fgets to get the input value with the s space 
  // gets get the multiworld input
// and the function to diplay all the gets input is   puts
// lets see them

char str[100];
    printf("enter the string: ");
    // gets(str); or 
    fgets(str, 100, stdin);
    puts(str);

    return 0;

}
