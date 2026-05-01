#include <stdio.h>
#include <string.h>
struct student 
{
   int roll;
   float cgpa;
    char name[10];
};
                                            // imp to remember
void printInfo(struct student s1);        // structis defined first so it can be used in function 

int main()
{
    struct student s1 = {15,3.4,"ali"};
    printInfo(s1);                          // mostly callled by value
    return 0;
}

void printInfo(struct student s1){

    printf("student information : \n");
    printf("roll no= %d\n", s1.roll);
    printf("cgpa = %f\n", s1.cgpa);
    printf("name = %s\n", s1.name);

}