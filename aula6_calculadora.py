def soma(val1,val2):
    resultado=val1+val2
    print(resultado)

def subtracao(val1,val2):
    resultado=val1-val2
    print(resultado)

def multiplicacao(val1,val2):
    resultado=val1*val2
    print(resultado)

def divisao(val1,val2):
    resultado=val1/val2
    print(resultado)

while 1:
    num1=int(input('Qual o primeiro número?'))

    num2=int(input('Qual o segundo número?'))

    sinal=input('Qual a operação?').lower()
    if num2==0 and sinal==('divisao') or sinal==('/'):
        print('Erro. Impossível dividir por zero.')
    
    if sinal==("soma") or sinal==("+"):
        soma(num1,num2)
        
    elif sinal==("subtracao") or sinal==("-"):
        subtracao(num1,num2)
        
    elif sinal==('multiplicacao') or sinal==("*"):
        multiplicacao(num1,num2)
        
    elif sinal==('divisao') or sinal==("/"):
        divisao(num1,num2)
  
    else:  
        print ('Inválido')
        
    if (input('Usar novamente?').lower())=='nao':
        break
