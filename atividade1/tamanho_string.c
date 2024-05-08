//Bibliotecas
#include <stdio.h>

//Protótipos de funções
int tamanhoPalavra(char*);
int tamanhoPalavraR(char*, int);

//Função encapsuladora
int tamanhoPalavra(char* S) {
    return tamanhoPalavraR(S, 0);
}

//Função recursiva
int tamanhoPalavraR(char* S, int valor) {
    if(S[valor] == '\0') {
        return valor;
    }
    else {
        return tamanhoPalavraR(S, valor + 1);
    }
}

int main() {
    char palavra[50];
    gets(palavra);
    int tamanho = tamanhoPalavra(palavra);
    printf("O tamanho eh %d\n", tamanho);
    
    return 0;
}


