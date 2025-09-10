import random
sorteio=random.randint(0,1)
lista=['cara','coroa']
computador=(lista[sorteio])
escolha=input('Cara ou Coroa!:').lower()
print(computador)
if escolha==computador:
  print("Você acertou!")
  input('Pressione Enter para sair...')
else:
    print("Errou!")
    input('Pressione Enter para sair...')