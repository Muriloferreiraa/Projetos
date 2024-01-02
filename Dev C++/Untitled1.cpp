#include<stdio.h>
void soma(int *vetor){
	int soma=0,i;
for(i=0;i<10;i++){
	soma=soma+vetor[i];
}
printf("\n%d",soma);
}
void sub(int *vetor){
	int sub=0,i;
for(i=0;i<10;i++){
	sub=vetor[9]-vetor[0];
}
printf("\n%d",sub);
}
void mult(int *vetor){
	int mult=1,i;
for(i=0;i<10;i++){
	mult=mult*vetor[i];
}
printf("\n%d",sub);
}


int main(){
int i=0,vetor[10];

for(i=0;i<10;i++){
	printf("digite 10 numeros:");
    scanf("%d", &vetor[i]);
}
soma(vetor);
sub(vetor);
mult(vetor);
}
