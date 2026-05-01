#include <stdio.h>
#include <string.h>
typedef struct address
{
   int house_no;
   int block;
   char city[20];
   char province[20];
} add ;

void printAdd(struct address adr);

int main()
{
    add adds[3];
    adds[0].house_no=1;
    adds[0].block= 2;
    strcpy(adds[0].city, "mian");
    strcpy(adds[0].province, "punjab");
    adds[1].house_no=2;
    adds[1].block= 2;
    strcpy(adds[1].city, "mianwali");
    strcpy(adds[1].province, "punjab");
    adds[2].house_no=3;
    adds[2].block= 4;
    strcpy(adds[2].city, "karachi");
    strcpy(adds[2].province, "sindh");

    printAdd(adds[0]);
    printAdd(adds[1]);
    printAdd(adds[2]);

    
    return 0;
}

void printAdd(struct address adr){
    printf("adress is = %d , %d, %s, %s \n", adr.house_no, adr.block,adr.city,adr.province);
}
