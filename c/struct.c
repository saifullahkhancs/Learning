#include <stdio.h>
#include <string.h>
struct student 
{
   int roll;
   float cgpa;
    char name[10];
};


int main()
{
    struct student s1;
    s1.roll = 14;
    s1.cgpa = 3.7;
 //   s1.name = "saif"; can not assign
    strcpy(s1.name, "saif");

    printf("roll no= %d\n", s1.roll);
    printf("cgpa = %f\n", s1.cgpa);
    printf("name = %s\n", s1.name);

    
    return 0;

}