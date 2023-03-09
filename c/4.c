#include <stdio.h>
#define Leap 1
int main(void){
    int a;
    int b;
    printf("Type in number a: \n");
    scanf("%d", &a);
    printf("Type in number b: \n");
    scanf("%d", &b);

    printf("a is %d",a);
    printf("\n");
    printf("b is %d",b);
    printf(Leap);
    return 0;
}