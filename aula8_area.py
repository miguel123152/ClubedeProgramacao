def quadrado ():
    lado=int(input('Digite o valor do lado: '))
    resultado=lado**2
    return resultado
def triangulo ():
    base=int(input('Digite o valor da base: '))
    altura=int(input('Digite o valor da altura: '))
    resultado=(base*altura)/2
    return resultado
def pentagono ():
    lado=int(input('Digite o valor do lado: '))
    apotema=int(input('Digite o valor do apotema: '))
    resultado=(5*lado*apotema)/2
    return resultado
def trapezio ():
    base_maior=int(input('Digite o valor da base maior: '))
    base_menor=int(input('Digite o valor da base menor: '))
    altura=int(input('Digite o valor da altura: '))
    resultado=((base_maior++base_menor)*altura)/2
    return resultado
def retangulo ():
    base=int(input('Digite o valor da base: '))
    altura=int(input('Digite o valor da altura: '))
    resultado=base*altura
    return resultado
def circulo ():
    raio=int(input('Digite o valor do raio: '))
    resultado=3.14*(raio**2)
    return int(resultado)
def menu():
    escolha=input('''Qual área deseja calcular?
    t-Triangulo
    q-Quadrado
    r-Retangulo
    tr-Trapezio
    c-Circulo
    p-Pentagono
    escolha: ''')
    
    if escolha=='q':
        area=quadrado()
    elif escolha=='t':
        area=triangulo()
    elif escolha=='r':
        area=retangulo()
    elif escolha=='tr':
        area=trapezio()
    elif escolha=='c':
        area=circulo()
    elif escolha=='p':
        area=petagono()
    else:
        print('Inválido')
        
    print(f'A área é {area})
    
    novamente=input('Usar novamente? (s/n)')
    if novamente='s':
        menu()
menu()
