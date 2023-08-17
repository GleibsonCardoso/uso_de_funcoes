#Gerar funções que duplicam, triplicam e quadruplicam recebendo um parâmetro
import os

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(' ---- Bem vindo ao multiplicador -----')

decisao = 'y'

while decisao == 'y':
    os.system('cls')
    entrada = int(input("Digite um valor para o multiplicador:  "))
    mult = criar_multiplicador(entrada)

    valor = int(input('Digite um valor inteiro para multiplicar:  '))
    resultado = mult(valor)

    print(resultado)

    decisao = input('Quer fazer nova operaçao? [y] or [n]:  ')
    
    
