'''

Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

from cabecalho import Cabecalho
titulo = Cabecalho('010', 'ESTRUTURA SEQUENCIAL')
print(titulo.texto)



def celciusF(c):
    f = (c * 9/5) + 32
    return print(f"""A temperatura {c}ºC equivale a {f:.2f}ºF """)
def celciusK(c):
    k = c + 273.15
    return print(f""" A temperatura {c}ºC equivale a {k:.2f}ºK""")

def fahrenheitC(f):
    c = (f - 32) * 5/9
    return print(f"""A temperatura {f}ºF equivale a {c:.2f}ºC""")
def fahrenheitK(f):
    k = (f - 32) * 5/9 + 273.15
    return print(f"""A temperatura {f}ºF equivale a {k:.2f}ºK""")

def kelvinC(k):
    c = k - 273.15
    return print(f"""A temperatura {k}ºK equivale a {c:.2f}ºC""")

def kelvinF(k):
    f = (k - 273.15) * 9/5 + 32
    return print(f"""A temperatura {k}ºK equivale a {f:.2f}ºF""")

def conve():
    resp = int(input("""Qual operação deseja efetuar: 
    [1] Celsius -> Fahrenheit
    [2] Celsius > Kelvin
    [3] Fahrenheit -> Celsius
    [4] Fahrenheit -> Kelvin
    [5] Kelvin -> Celsius
    [6] Kelvin -> Fahrenheit
     """))
    if resp == 1:
        c = float( input( "Digite o valor da temperatura em graus Celsius: " ) )
        celciusF(c)
    elif resp == 2:
        c = float( input( "Digite o valor da temperatura em graus Celsius: " ) )
        celciusK( c )

    elif resp == 3:
        f = float( input( "Digite o valor da temperatura em graus Fahrenheit: " ) )
        fahrenheitC( f )

    elif resp == 4:
        f = float( input( "Digite o valor da temperatura em graus Fahrenheit: " ) )
        fahrenheitK( f )

    elif resp == 5:
        k = float( input( "Digite o valor da temperatura em graus Kelvin: " ) )
        kelvinC(k)

    elif resp == 6:
        k = float( input( "Digite o valor da temperatura em graus Kelvin: " ) )
        kelvinF( k )

    else:
        print("Você entrou com a opção inválida!")

conve()


