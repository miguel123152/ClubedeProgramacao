def delta(val1,val2,val3):
    resultado=(val2**2)+(-4*val1*val3)
    return(resultado)
    
def bhaskarap(val1,val2,val3):
    resultado=(-val2+val3**0.5)/(val1*2)
    return(resultado)
    
def bhaskaran(val1,val2,val3):
    resultado=(-val2-val3**0.5)/(val1*2)
    return(resultado)

def bhaskara():
    a=int(input('Valor de a:'))

    b=int(input('Valor de b:'))

    c=int(input('Valor de c:'))
    
    d=delta(a,b,c)
    
    x1=bhaskarap(a,b,d)
    x2=bhaskaran(a,b,d)
    
    print (d)
    
    if d<0:
         print('Erro. Apenas números reais disponíveis.')
         
    else:
        print(f'O resultado foi: {x1} e {x2}')
    escolha=input ('Deseja usar de novo?:(s/n)')
    if escolha==('s'):
        bhaskara()
bhaskara()
