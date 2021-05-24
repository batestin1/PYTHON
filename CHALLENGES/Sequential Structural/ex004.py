'''

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

'''

from cabecalho import Cabecalho


titulo = Cabecalho('004', 'ESTRUTURA SEQUENCIAL')
print(titulo.texto)

mdPortugues = 0
mdMatematica = 0
mdHistoria = 0
mdGeografia = 0
mdCiencia = 0





def portugues():

    global mdPortugues
    global mdMatematica
    global mdHistoria
    global mdGeografia
    global mdCiencia

    print('~~~~~~~~~~~~~~~NOTA PORTUGUÊS ~~~~~~~~~~~~~~~~~~~~~')
    n1 = float(input(' Entre com a nota do primeiro bimestre: '))
    n2 = float(input(' Entre com a nota do segundo bimestre: '))
    n3 = float(input(' Entre com a nota do terceiro bimestre: '))
    n4 = float(input(' Entre com a nota do quarto bimestre: '))
    media = (n1+n2+n3+n4)/4
    mdPortugues = media
    return print(f""" ~~~~~~~ RESULTADO ~~~~~~~~~~~~
    ~~~~~~~ PRIMEIRO BIMESTRE = {n1} ~~~~~~~~~~~~~~
    ~~~~~~~ SEGUNDO BIMESTRE = {n2} ~~~~~~~~~~~~~~
    ~~~~~~~ TERCEIRO BIMESTRE = {n3} ~~~~~~~~~~~~~~
    ~~~~~~~ QUARTO BIMESTRE = {n4} ~~~~~~~~~~~~~~
    ~~~~~~~~ MEDIA FINAL = {mdPortugues:.2f} ~~~~~~~~~~~~
                """)
def matematica():
    global mdPortugues
    global mdMatematica
    global mdHistoria
    global mdGeografia
    global mdCiencia
    print( '~~~~~~~~~~~~~~~NOTA MATEMÁTICA ~~~~~~~~~~~~~~~~~~~~~' )
    n1 = float( input( ' Entre com a nota do primeiro bimestre: ' ) )
    n2 = float( input( ' Entre com a nota do segundo bimestre: ' ) )
    n3 = float( input( ' Entre com a nota do terceiro bimestre: ' ) )
    n4 = float( input( ' Entre com a nota do quarto bimestre: ' ) )
    media = (n1 + n2 + n3 + n4) / 4
    mdMatematica = media
    return print( f""" ~~~~~~~ RESULTADO ~~~~~~~~~~~~
        ~~~~~~~ PRIMEIRO BIMESTRE = {n1} ~~~~~~~~~~~~~~
        ~~~~~~~ SEGUNDO BIMESTRE = {n2} ~~~~~~~~~~~~~~
        ~~~~~~~ TERCEIRO BIMESTRE = {n3} ~~~~~~~~~~~~~~
        ~~~~~~~ QUARTO BIMESTRE = {n4} ~~~~~~~~~~~~~~
        ~~~~~~~~ MEDIA FINAL = {mdMatematica:.2f} ~~~~~~~~~~~~
                    """ )

def historia():
    global mdPortugues
    global mdMatematica
    global mdHistoria
    global mdGeografia
    global mdCiencia

    print( '~~~~~~~~~~~~~~~NOTA HISTÓRIA ~~~~~~~~~~~~~~~~~~~~~' )
    n1 = float( input( ' Entre com a nota do primeiro bimestre: ' ) )
    n2 = float( input( ' Entre com a nota do segundo bimestre: ' ) )
    n3 = float( input( ' Entre com a nota do terceiro bimestre: ' ) )
    n4 = float( input( ' Entre com a nota do quarto bimestre: ' ) )
    media = (n1 + n2 + n3 + n4) / 4
    mdHistoria = media
    return print( f""" ~~~~~~~ RESULTADO ~~~~~~~~~~~~
        ~~~~~~~ PRIMEIRO BIMESTRE = {n1} ~~~~~~~~~~~~~~
        ~~~~~~~ SEGUNDO BIMESTRE = {n2} ~~~~~~~~~~~~~~
        ~~~~~~~ TERCEIRO BIMESTRE = {n3} ~~~~~~~~~~~~~~
        ~~~~~~~ QUARTO BIMESTRE = {n4} ~~~~~~~~~~~~~~
        ~~~~~~~~ MEDIA FINAL = {mdHistoria:.2f} ~~~~~~~~~~~~
                    """ )
def geografia():
    global mdPortugues
    global mdMatematica
    global mdHistoria
    global mdGeografia
    global mdCiencia

    print( '~~~~~~~~~~~~~~~NOTA GEOGRAFIA ~~~~~~~~~~~~~~~~~~~~~' )
    n1 = float( input( ' Entre com a nota do primeiro bimestre: ' ) )
    n2 = float( input( ' Entre com a nota do segundo bimestre: ' ) )
    n3 = float( input( ' Entre com a nota do terceiro bimestre: ' ) )
    n4 = float( input( ' Entre com a nota do quarto bimestre: ' ) )
    media = (n1 + n2 + n3 + n4) / 4
    mdGeografia = media
    return print( f""" ~~~~~~~ RESULTADO ~~~~~~~~~~~~
        ~~~~~~~ PRIMEIRO BIMESTRE = {n1} ~~~~~~~~~~~~~~
        ~~~~~~~ SEGUNDO BIMESTRE = {n2} ~~~~~~~~~~~~~~
        ~~~~~~~ TERCEIRO BIMESTRE = {n3} ~~~~~~~~~~~~~~
        ~~~~~~~ QUARTO BIMESTRE = {n4} ~~~~~~~~~~~~~~
        ~~~~~~~~ MEDIA FINAL = {mdGeografia:.2f} ~~~~~~~~~~~~
                    """ )
def ciencia():
    global mdPortugues
    global mdMatematica
    global mdHistoria
    global mdGeografia
    global mdCiencia

    print( '~~~~~~~~~~~~~~~NOTA CIÊNCIAS SOCIAIS ~~~~~~~~~~~~~~~~~~~~~' )
    n1 = float( input( ' Entre com a nota do primeiro bimestre: ' ) )
    n2 = float( input( ' Entre com a nota do segundo bimestre: ' ) )
    n3 = float( input( ' Entre com a nota do terceiro bimestre: ' ) )
    n4 = float( input( ' Entre com a nota do quarto bimestre: ' ) )
    media = (n1 + n2 + n3 + n4) / 4
    mdCiencia = media
    return print( f""" ~~~~~~~ RESULTADO ~~~~~~~~~~~~
        ~~~~~~~ PRIMEIRO BIMESTRE = {n1} ~~~~~~~~~~~~~~
        ~~~~~~~ SEGUNDO BIMESTRE = {n2} ~~~~~~~~~~~~~~
        ~~~~~~~ TERCEIRO BIMESTRE = {n3} ~~~~~~~~~~~~~~
        ~~~~~~~ QUARTO BIMESTRE = {n4} ~~~~~~~~~~~~~~
        ~~~~~~~~ MEDIA FINAL = {mdCiencia:.2f} ~~~~~~~~~~~~
                    """ )
def repet():
    resp = int(input(""" Deseja repetir algumas das opcoes abaixo:
    [1] - PORTUGUÊS;
    [2] - MATEMÁTICA;
    [3] - HISTÓRIA;
    [4] - GEOGRÁFIA;
    [5] - CIÊNCIAS SOCIAIS.
    [6] - NENHUM
     """))
    if resp == 1:
        portugues()
    elif resp == 2:
        matematica()
    elif resp == 3:
        historia()
    elif resp == 4:
        geografia()
    elif resp == 5:
        ciencia()
    elif resp == 6:
        print('Obrigado')

def mediaGeral():
    global mdPortugues
    global mdMatematica
    global mdHistoria
    global mdGeografia
    global mdCiencia

    resp = int(input(""" O QUE DESEJAS FAZER AGORA?
     [1] SOMAR TODAS AS NOTAS;
     [2] REPETIR A OPERAÇÃO;
     [3] ENCERRAR A OPERAÇÃO. """))

    if resp == 1:
        med = (mdPortugues + mdMatematica + mdHistoria + mdGeografia + mdCiencia) / 5
        print(f"""Sua notas ficaram assim:
MÉDIA PORTUGUêS: {mdPortugues}
MÉDIA MATEMÁTICA: {mdMatematica}
MÉDIA HISTÓRIA: {mdHistoria}
MÉDIA GEOGRAFIA: {mdGeografia}
MÉDIA CIÊNCIA SOCIAS: {mdCiencia}
MÉDIA FINAL: {med:.2f}""")
    elif resp == 2:
        repet()

    elif resp == 3:
        print("FIM DO PROGRAMA")

portugues()
matematica()
historia()
geografia()
ciencia()
mediaGeral()

