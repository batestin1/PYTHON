'''

Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
'''


from cabecalho import Cabecalho
titulo = Cabecalho('010', 'ESTRUTURA SEQUENCIAL')
print(titulo.texto)



def celcius(c):
    f = (c * 9/5) + 32
    return print(f"""A temperatura {c}ºC equivale a {f:.2f}ºF """)
def fahrenheit(f):
    c = (f - 32) * 5/9
    return print(f"""A temperatura {f}ºF equivale a {c:.2f}ºC""")
def conve():
    resp = int(input("""Qual operação deseja efetuar: 
    [1] Celsius -> Fahrenheit
    [2] Fahreinheit -> Celcius 
    """))
    if resp == 1:
        c = float( input( "Digite o valor da temperatura em graus Celsius: " ) )
        celcius(c)
    elif resp == 2:
        f = float( input( "Digite o valor da temperatura em graus Fahrenheit: " ) )
        fahrenheit(f)
    else:
        print("Você entrou com a opção inválida!")

conve()


