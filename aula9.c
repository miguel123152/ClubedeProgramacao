#include<stdio.h>
#include<stdlib.h>

void texto(){
    printf("Hello World");
}

void soma() {
    int num1, num2, resultado;
    
    printf("Digite dois números: ");
    scanf("%d %d",&num1,&num2);

    resultado=num1+num2;
    
    printf("O resultado da soma de %d e %d é %d", num1, num2, resultado);
}

void indice(){
    int indice=10;
    
    do{
        printf("%d", indice);
        indice++;
    } while (indice >= 100);
    
}

int main(){
    for (int i=0; ; i++){
        
        if (i==50){
            return 0;
        } else{
            printf("%d \n", i);
        }
    }
}
