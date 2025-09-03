import random
Repetir=['Sim','Nao']
alea=random.randint(0,2)
lista=['Pedra', 'Papel','Tesoura']
computador=lista[alea]
print(computador)
user=input('Pedra, Papel, Tesoura!')
print(computador)
while 1:
    print ('O computador escolheu:',computador)
    if computador=='pedra' and user=='papel': print('Você ganhou!')
    computador=='papel' and user=='tesoura':  print('Você ganhou!')
    computador=='tesoura' and user=='pedra': print('Você ganhou!')
    
    else:
        print ('Errou!')
        break
