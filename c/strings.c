#include <stdio.h>

void printString(char *arr);

int main()
{
    
    char greetings[] = "Hello World!\n";
    printf("%s", greetings);
    //  prints the first character (0) in greetings
    printf("%c", greetings[0]);
    
    // modify the string
    greetings[0] = 'J';
    printf("%s  Outputs  Jello World! instead of Hello World! \n", greetings);
    
    //another way of creating strings
    char greeting[] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!', '\0'};
    printf("%s \n", greeting);
    
   // Why do we include the \0 character at the end? 
   //This is known as the "null terminating character", 
   //and must be included when creating strings using this method. 
   //It tells C that this is the end of the string.


    // imp //

    char txt[] = "We are the so-called \"Vikings\" from the north.";
    char txt2[] = "It\'s alright.";
    //  \t is for tab

    char class[] = "apna college\n";
    printf("%s", class);  // "%s" string format pecifier

    char lifee[50];
    printf("write name of your life: ");
    scanf("%s", lifee );
    printf("name of your life is= %s \n" , lifee);
    // create a string firstName and lastNameto store details odf user and 
    // print all the characters using a loop

    char firstName[] = "saif";
    char lastName[] = "khan";

    printString(&firstName[0]);
    printString(lastName);
    return 0;
}

void printString(char *arr){
    for (int i= 0; *(arr+i) != '\0' ; i++){
        printf("%c",*(arr+i) );    }
        printf("\n");
    }
