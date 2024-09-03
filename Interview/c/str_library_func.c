#include <stdio.h>
#include <string.h>
int main()
{
  char name[] = "saif";
  int length = strlen(name); // for typecasting
  printf("the length of the string is= %d \n", length);

    char str[100];
    char ch;
    int i = 0;

    while(ch != '\n'){
        scanf("%c", &ch);
        str[i] = ch;
        i++;
    }
        str[i] = '\0';
    puts(str);

        return 0;

}
