#include <stdio.h>
int main(void){
    int n, x[10], i,s;
    scanf("%d",&n);
    i=0;
    s=0;
    while(i<n){
        scanf("%d", &x[i]);
        i=i+1;
    }
    i=i-1;
    while(i>=0){
        s=s+x[i];
        i= i-1;
    }
    printf("%d",s);
    return 0;
}