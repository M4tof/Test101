#include <stdio.h> //must have
#include <math.h>

int main(){ 
float a,b;
scanf("%f %f",&a,&b);

float R;
R = 4*a + 2*((a-b-1)/(pow(a,2) + pow(b,2) +1));

printf("%f",R);
    return 0;
}