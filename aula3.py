i=0
while 1:
    i+=1
    if i==11:
        break
    if i%2==1:
        continue
    print(i) 

frutas=['abacaxi','maça','banana','kiwi','uva','manga','limao','morango','mamao','kibe']
frutas.append('mirtilo')
frutas.append('pitaia')
frutas.remove('kibe')
for fruta in frutas:
    print(fruta)

paises=['brasil','japao','austria','argentina','alemanha','china','inglaterra','eua','canada','franca']
paises.append('portugal')
paises.append('espanha')
for pais in paises:
    print(pais)

print('Tente Adivinhar o Número!')

import random
numero=random.randint(1,100)

palpite=0 
tentativa=0 
while 1:
    tentativa+=1
    print('Tentativa:'+str(tentativa))
    palpite=int(input ('Qual o número?'))
    if palpite<=0 or palpite >=101:
        print('Número Invalido')
        continue
    if palpite==numero:
            print('Parabéns!')
            break
    elif palpite>numero:
            print('Palpite é maior que o número.')
    elif palpite<numero:
           print('Palpite é menor que o número')
