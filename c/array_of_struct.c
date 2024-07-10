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
    struct student arr[100];
    arr[0].roll = 14;
    arr[0].cgpa = 3.7;
 //   s1.name = "saif"; can not assign
    strcpy(arr[0].name, "saif");
    printf("roll no= %d\n", arr[0].roll);
    printf("cgpa = %f\n", arr[0].cgpa);
    printf("name = %s\n", arr[0].name);

    struct student s1 = {15,3.4,"ali"};
    printf("roll no= %d\n", s1.roll);
     printf("cgpa = %f\n", s1.cgpa);
    printf("name = %s\n", s1.name);
    return 0;

}