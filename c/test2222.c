#include <stdio.h>
int main(void){
    int n, x, i,s;
    scanf("%d",&n);
    i=0;
    s=0;
    while(i<n){
        scanf("%d", &x);
        s=s+x;
        i=i+1;
    }
    printf("%d",s);
    return 0;
}