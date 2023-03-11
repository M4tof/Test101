#include <stdio.h> //must have
#include <math.h>

int main(){ 
int a;
printf("Input the length of the word: \n");
scanf("%d",&a);

a++;

printf("Input the word: \n");
char m[a];

scanf("%s",&m);


printf("the word is : ");
printf("%s\n",m);

printf("It consists of : \n");

for (int i=65; i<91 ;i++){
    //printf("%c",i);
    int count=0;
    for (int g=0; g<a; g++){
        int N =(int)(m[g]);
        if (N == i){
            count++;
        }
    }
    if(count >0){
    printf("%c",i);
    printf(":");
    printf("%d\n",count);}
}

for (int i=97; i<123 ;i++){
    //printf("%c",i);
    int count=0;
    for (int g=0; g<a; g++){
        int N =(int)(m[g]);
        if (N == i){
            count++;
        }
    }
    if(count >0){
    printf("%c",i);
    printf(":");
    printf("%d\n",count);}
}
return 0;
}