import random

print('$-'*15)
print(' '*8,'LOTOFACIL')
print('$-'*15)

try:
    print('\nDigite seus 15 números')
    numero=[]
    for contador in range(1,16):
        numero.append(int(input(f'Digite o {contador}º:')))#append para mostrar
        #todos os números no print
        numeroSorteados = random.sample(range(1,25),15)
    print(f'\nSeus números são {numero}')
    print(f'Números sorteados: {sorted(numeroSorteados, key=int)}')
                                    #sorted para mostrar de ordem crescente.
    if numero == numeroSorteados:
        print('\nPárabéns você ganhou!!!')
    else:
        print('\nNão foi dessa vez!')
except:
    print('Erro! Digite apenas números.')




