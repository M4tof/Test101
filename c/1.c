#include <stdio.h> //must have
int main(){ 
    
    char m[]="This is some text";

    char C = m[1];

    printf("%c",C);

    for(int i=0;i<10;i++){
        printf("%c\n",m[i]);
    }
    return 0;
}