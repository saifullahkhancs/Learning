#include <stdio.h>
int main()
{
    char c, *cp;
    short s, *sp;
    int i , *ip;
    long l,*lp;
    long long ll, *llp;
    float f;
    double df;
    // void v ,*vp;  compilation error
    void *vp;

    printf("size of c= %lu, %lu \n", sizeof(char),sizeof(c) );
    printf("size of cp= %lu, %lu, %lu \n", sizeof(char *),sizeof(*cp), sizeof(cp));
    
    printf("size of s= %lu, %lu \n", sizeof(short),sizeof(s));
    printf("size of cp= %lu, %lu, %lu \n", sizeof(short *),sizeof(*sp), sizeof(sp));

    printf("size of i= %lu, %lu \n", sizeof(int),sizeof(i));

    printf("size of l= %lu, %lu \n", sizeof(int),sizeof(i));

    printf("size of f= %lu, %lu \n", sizeof(float),sizeof(f));

    printf("size of df= %lu, %lu \n", sizeof(double),sizeof(df));

    printf("size of vp= %lu, %lu \n", sizeof(void *),sizeof(vp));

    printf("size of v= %lu\n", sizeof(void));


    return 0;
}
