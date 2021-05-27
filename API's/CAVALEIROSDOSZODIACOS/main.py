#Pequeno jogo dos Cavaleiros dos Zodiacos trabalhando com API
#Desenvolvido por Maycon Cypriano

#chamando nossas classes

from protagonistas import Pegasus, Dragao, Cisne, Andromeda, Fenix, PegasusAtaque, DragaoAtaque, CisneAtaque, AndromedaAtaque, FenixAtaque
from typewriter import MaquinadeEscrever
from casas import casadeLeao, casadeLibra, casadeAries, casadeVirgem, casadeTouros, casaDeGemeos, casaDeCancer, casadePeixes, casadeAquarius, casadeEscorpiao, casadeSagitario, casadeCapricornio
from ouro import Aries, AriesAtaque, Aquarius, AquariusAtaque, Sagitario, SagitarioAtaque, Libra, LibraAtaque, Cancer, CancerAtaque, Touros, TourosAtaque, Virgem, VirgemAtaque, Escorpiao, EscorpiaoAtaque, Capricornio, CapricornioAtaque, Peixes, PeixesAtaque, Leao,LeaoAtaque,  Gemeos, GemeosAtaque

import random
import time


# variavel de sorte
sorte = ['Você Venceu', 'Você Perdeu']
sorte = random.choice(sorte)
santuA = """ ... Você chegou ao Santuário.
Algo muito estranho está acontecendo aqui!
A primeira casa que você vai enfrentar é a CASA DE ARIES!
"""
santuB = """ Avançando! Próxima desafio! """



venceu = """Você venceu esta Batalha!, mas o jogo ainda não terminou!
Avante Cavaleiro! Salve Athena!"""

derrota = """... Você lutou bravamente, mas ainda precisa melhorar! 
Continue treinando!"""

vilaoVi = """Eu sou um Cavaleiro de Ouro! É claro que você não me venceria!"""

vilaoDe = """
O que???
Você despertou o sétimo sentido?!
Não sou páreo para você!
Pode avançar!"""


#jogando
print('~'*100)
print('')
intro = """ 
Por séculos o destino da humanidade está nas mãos de Deuses e Deusas,
nossa protetora terrestre é chamada de Athenas. 
Para protege-la, são escolhidos cavaleiros cujo poder vem de seu cosmo,
sua constelação protetora.
A estes cavaleiros dar-se o nome de..."""
MaquinadeEscrever(intro).mensagem
print('')
print('~'*100)
print('')
titulo = 'OS CAVALEIROS DOS ZODIACO'
MaquinadeEscrever(titulo).mensagem
print('')
print('~'*100)
print('')
intro2 = """
... Algo de estranho esta acontecendo no Santuário.
E os cavaleiros de Athenas precisam atravessar as 12 casas que regem
o Santuário.
Quem você vai escolher?"""
MaquinadeEscrever(intro2).mensagem
print('')
escolha = """ 
ESCOLHA O SEU CAVALEIRO 
[A] CAVALEIRO DE PÉGASUS; 
[B] CAVALEIRO DE DRAGÃO;
[C] CAVALEIRO DE CISNE;
[D] CAVALEIRO DE ANDRÔMEDA;
[E] CAVALEIRO DE FÊNIX """

MaquinadeEscrever(escolha).mensagem
print('')
id = input('R: ').upper()[0]

if id == 'A':
    time.sleep(1)
    print('~' * 100)
    dados = 'EIS OS DADOS SOBRE TEU PERSONAGEM!'
    MaquinadeEscrever(dados).mensagem
    Pegasus()
    print('~' * 100)
    MaquinadeEscrever(santuA).mensagem
    print('~'*100)
    print('OPONENTE')
    print('~' * 100)
    Aries()
    print('')
    casadeAries()
    print('')
    print('Você: ')
    PegasusAtaque()
    print('')
    AriesAtaque()
    time.sleep(1)
    print('')

    if sorte == 'Você Venceu':
        MaquinadeEscrever(venceu).mensagem
        print('')
        print('Oponente: ')
        MaquinadeEscrever(vilaoDe).mensagem
        print('')
        print('~'*100)
        print('')
        MaquinadeEscrever(santuB)
        print('')
        print('~'*100)
        print('')
        print('OPONENTE')
        print('')
        Touros()
        print('')
        casadeTouros()
        print('')
        print('Você: ')
        PegasusAtaque()
        print('')
        TourosAtaque()
        time.sleep(1)
        print('')
        if sorte == 'Você Venceu':
            MaquinadeEscrever(venceu).mensagem
            print('')
            print('Oponente: ')
            MaquinadeEscrever(vilaoDe).mensagem
            print('')
            print('~' * 100)
            print('')
            MaquinadeEscrever(santuB)
            print('')
            print('~' * 100)
            print('')
            print('OPONENTE')
            print('')
            Gemeos()
            print('')
            casaDeGemeos()
            print('')
            print('Você: ')
            PegasusAtaque()
            print('')
            GemeosAtaque()
            time.sleep(1)
            print('')
            if sorte == 'Você Venceu':
                MaquinadeEscrever(venceu).mensagem
                print('')
                print('Oponente: ')
                MaquinadeEscrever(vilaoDe).mensagem
                print('')
                print('~' * 100)
                print('')
                MaquinadeEscrever(santuB)
                print('')
                print('~' * 100)
                print('')
                print('OPONENTE')
                print('')
                Cancer()
                print('')
                casaDeCancer()
                print('')
                print('Você: ')
                PegasusAtaque()
                print('')
                CancerAtaque()
                time.sleep(1)
                if sorte == 'Você Venceu':
                    MaquinadeEscrever(venceu).mensagem
                    print('')
                    print('Oponente: ')
                    MaquinadeEscrever(vilaoDe).mensagem
                    print('')
                    print('~' * 100)
                    print('')
                    MaquinadeEscrever(santuB)
                    print('')
                    print('~' * 100)
                    print('')
                    print('OPONENTE')
                    print('')
                    Leao()
                    print('')
                    casadeLeao()
                    print('')
                    print('Você: ')
                    PegasusAtaque()
                    print('')
                    LeaoAtaque()
                    time.sleep(1)
                    if sorte == 'Você Venceu':
                        MaquinadeEscrever(venceu).mensagem
                        print('')
                        print('Oponente: ')
                        MaquinadeEscrever(vilaoDe).mensagem
                        print('')
                        print('~' * 100)
                        print('')
                        MaquinadeEscrever(santuB)
                        print('')
                        print('~' * 100)
                        print('')
                        print('OPONENTE')
                        print('')
                        Virgem()
                        print('')
                        casadeVirgem()
                        print('')
                        print('Você: ')
                        PegasusAtaque()
                        print('')
                        VirgemAtaque()
                        time.sleep(1)
                        if sorte == 'Você Venceu':
                            MaquinadeEscrever(venceu).mensagem
                            print('')
                            print('Oponente: ')
                            MaquinadeEscrever(vilaoDe).mensagem
                            print('')
                            print('~' * 100)
                            print('')
                            MaquinadeEscrever(santuB)
                            print('')
                            print('~' * 100)
                            print('')
                            print('OPONENTE')
                            print('')
                            Libra()
                            print('')
                            casadeLibra()
                            print('')
                            print('Você: ')
                            PegasusAtaque()
                            print('')
                            LibraAtaque()
                            time.sleep(1)
                            if sorte == 'Você Venceu':
                                MaquinadeEscrever(venceu).mensagem
                                print('')
                                print('Oponente: ')
                                MaquinadeEscrever(vilaoDe).mensagem
                                print('')
                                print('~' * 100)
                                print('')
                                MaquinadeEscrever(santuB)
                                print('')
                                print('~' * 100)
                                print('')
                                print('OPONENTE')
                                print('')
                                Escorpiao()
                                print('')
                                casadeEscorpiao()
                                print('')
                                print('Você: ')
                                PegasusAtaque()
                                print('')
                                EscorpiaoAtaque()
                                time.sleep(1)
                                if sorte == 'Você Venceu':
                                    MaquinadeEscrever(venceu).mensagem
                                    print('')
                                    print('Oponente: ')
                                    MaquinadeEscrever(vilaoDe).mensagem
                                    print('')
                                    print('~' * 100)
                                    print('')
                                    MaquinadeEscrever(santuB)
                                    print('')
                                    print('~' * 100)
                                    print('')
                                    print('OPONENTE')
                                    print('')
                                    Sagitario()
                                    print('')
                                    casadeSagitario()
                                    print('')
                                    print('Você: ')
                                    PegasusAtaque()
                                    print('')
                                    SagitarioAtaque()
                                    time.sleep(1)
                                    if sorte == 'Você Venceu':
                                        MaquinadeEscrever(venceu).mensagem
                                        print('')
                                        print('Oponente: ')
                                        MaquinadeEscrever(vilaoDe).mensagem
                                        print('')
                                        print('~' * 100)
                                        print('')
                                        MaquinadeEscrever(santuB)
                                        print('')
                                        print('~' * 100)
                                        print('')
                                        print('OPONENTE')
                                        print('')
                                        Capricornio()
                                        print('')
                                        casadeCapricornio()
                                        print('')
                                        print('Você: ')
                                        PegasusAtaque()
                                        print('')
                                        CapricornioAtaque()
                                        time.sleep(1)
                                        if sorte == 'Você Venceu':
                                            MaquinadeEscrever(venceu).mensagem
                                            print('')
                                            print('Oponente: ')
                                            MaquinadeEscrever(vilaoDe).mensagem
                                            print('')
                                            print('~' * 100)
                                            print('')
                                            MaquinadeEscrever(santuB)
                                            print('')
                                            print('~' * 100)
                                            print('')
                                            print('OPONENTE')
                                            print('')
                                            Aquarius()
                                            print('')
                                            casadeAquarius()
                                            print('')
                                            print('Você: ')
                                            PegasusAtaque()
                                            print('')
                                            AquariusAtaque()
                                            time.sleep(1)
                                            if sorte == 'Você Venceu':
                                                MaquinadeEscrever(venceu).mensagem
                                                print('')
                                                print('Oponente: ')
                                                MaquinadeEscrever(vilaoDe).mensagem
                                                print('')
                                                print('~' * 100)
                                                print('')
                                                MaquinadeEscrever(santuB)
                                                print('')
                                                print('~' * 100)
                                                print('')
                                                print('OPONENTE')
                                                print('')
                                                Peixes()
                                                print('')
                                                casadePeixes()
                                                print('')
                                                print('Você: ')
                                                PegasusAtaque()
                                                print('')
                                                PeixesAtaque()
                                                time.sleep(1)
                                                if sorte == 'Você Venceu':
                                                    MaquinadeEscrever(venceu).mensagem
                                                    print('')
                                                    print('Oponente: ')
                                                    MaquinadeEscrever(vilaoDe).mensagem
                                                    print('')
                                                    print('~' * 100)
                                                    print('Parabéns Você venceu o jogo!')





    else:
        print('')
        MaquinadeEscrever(derrota).mensagem
        print('')
        print('Oponente: ')
        MaquinadeEscrever(vilaoVi).mensagem
        print('')
        print('Fim de Jogo')







elif id == 'B':
    time.sleep(1)
    print('~' * 100)
    dados = 'EIS OS DADOS SOBRE TEU PERSONAGEM!'
    MaquinadeEscrever(dados).mensagem
    Dragao()
    print('~' * 100)
    MaquinadeEscrever(santuA).mensagem
    print('~' * 100)
    print('OPONENTE')
    print('~' * 100)
    Aries()
    print('')
    casadeAries()
    print('')
    print('Você: ')
    DragaoAtaque()
    print('')
    AriesAtaque()
    time.sleep(1)
    print('')

    if sorte == 'Você Venceu':
        MaquinadeEscrever(venceu).mensagem
        print('')
        print('Oponente: ')
        MaquinadeEscrever(vilaoDe).mensagem
        print('')
        print('~' * 100)
        print('')
        MaquinadeEscrever(santuB)
        print('')
        print('~' * 100)
        print('')
        print('OPONENTE')
        print('')
        Touros()
        print('')
        casadeTouros()
        print('')
        print('Você: ')
        DragaoAtaque()
        print('')
        TourosAtaque()
        time.sleep(1)
        print('')
        if sorte == 'Você Venceu':
            MaquinadeEscrever(venceu).mensagem
            print('')
            print('Oponente: ')
            MaquinadeEscrever(vilaoDe).mensagem
            print('')
            print('~' * 100)
            print('')
            MaquinadeEscrever(santuB)
            print('')
            print('~' * 100)
            print('')
            print('OPONENTE')
            print('')
            Gemeos()
            print('')
            casaDeGemeos()
            print('')
            print('Você: ')
            DragaoAtaque()
            print('')
            GemeosAtaque()
            time.sleep(1)
            print('')
            if sorte == 'Você Venceu':
                MaquinadeEscrever(venceu).mensagem
                print('')
                print('Oponente: ')
                MaquinadeEscrever(vilaoDe).mensagem
                print('')
                print('~' * 100)
                print('')
                MaquinadeEscrever(santuB)
                print('')
                print('~' * 100)
                print('')
                print('OPONENTE')
                print('')
                Cancer()
                print('')
                casaDeCancer()
                print('')
                print('Você: ')
                DragaoAtaque()
                print('')
                CancerAtaque()
                time.sleep(1)
                if sorte == 'Você Venceu':
                    MaquinadeEscrever(venceu).mensagem
                    print('')
                    print('Oponente: ')
                    MaquinadeEscrever(vilaoDe).mensagem
                    print('')
                    print('~' * 100)
                    print('')
                    MaquinadeEscrever(santuB)
                    print('')
                    print('~' * 100)
                    print('')
                    print('OPONENTE')
                    print('')
                    Leao()
                    print('')
                    casadeLeao()
                    print('')
                    print('Você: ')
                    DragaoAtaque()
                    print('')
                    LeaoAtaque()
                    time.sleep(1)
                    if sorte == 'Você Venceu':
                        MaquinadeEscrever(venceu).mensagem
                        print('')
                        print('Oponente: ')
                        MaquinadeEscrever(vilaoDe).mensagem
                        print('')
                        print('~' * 100)
                        print('')
                        MaquinadeEscrever(santuB)
                        print('')
                        print('~' * 100)
                        print('')
                        print('OPONENTE')
                        print('')
                        Virgem()
                        print('')
                        casadeVirgem()
                        print('')
                        print('Você: ')
                        DragaoAtaque()
                        print('')
                        VirgemAtaque()
                        time.sleep(1)
                        if sorte == 'Você Venceu':
                            MaquinadeEscrever(venceu).mensagem
                            print('')
                            print('Oponente: ')
                            MaquinadeEscrever(vilaoDe).mensagem
                            print('')
                            print('~' * 100)
                            print('')
                            MaquinadeEscrever(santuB)
                            print('')
                            print('~' * 100)
                            print('')
                            print('OPONENTE')
                            print('')
                            Libra()
                            print('')
                            casadeLibra()
                            print('')
                            print('Você: ')
                            DragaoAtaque()
                            print('')
                            LibraAtaque()
                            time.sleep(1)
                            if sorte == 'Você Venceu':
                                MaquinadeEscrever(venceu).mensagem
                                print('')
                                print('Oponente: ')
                                MaquinadeEscrever(vilaoDe).mensagem
                                print('')
                                print('~' * 100)
                                print('')
                                MaquinadeEscrever(santuB)
                                print('')
                                print('~' * 100)
                                print('')
                                print('OPONENTE')
                                print('')
                                Escorpiao()
                                print('')
                                casadeEscorpiao()
                                print('')
                                print('Você: ')
                                DragaoAtaque()
                                print('')
                                EscorpiaoAtaque()
                                time.sleep(1)
                                if sorte == 'Você Venceu':
                                    MaquinadeEscrever(venceu).mensagem
                                    print('')
                                    print('Oponente: ')
                                    MaquinadeEscrever(vilaoDe).mensagem
                                    print('')
                                    print('~' * 100)
                                    print('')
                                    MaquinadeEscrever(santuB)
                                    print('')
                                    print('~' * 100)
                                    print('')
                                    print('OPONENTE')
                                    print('')
                                    Sagitario()
                                    print('')
                                    casadeSagitario()
                                    print('')
                                    print('Você: ')
                                    DragaoAtaque()
                                    print('')
                                    SagitarioAtaque()
                                    time.sleep(1)
                                    if sorte == 'Você Venceu':
                                        MaquinadeEscrever(venceu).mensagem
                                        print('')
                                        print('Oponente: ')
                                        MaquinadeEscrever(vilaoDe).mensagem
                                        print('')
                                        print('~' * 100)
                                        print('')
                                        MaquinadeEscrever(santuB)
                                        print('')
                                        print('~' * 100)
                                        print('')
                                        print('OPONENTE')
                                        print('')
                                        Capricornio()
                                        print('')
                                        casadeCapricornio()
                                        print('')
                                        print('Você: ')
                                        DragaoAtaque()
                                        print('')
                                        CapricornioAtaque()
                                        time.sleep(1)
                                        if sorte == 'Você Venceu':
                                            MaquinadeEscrever(venceu).mensagem
                                            print('')
                                            print('Oponente: ')
                                            MaquinadeEscrever(vilaoDe).mensagem
                                            print('')
                                            print('~' * 100)
                                            print('')
                                            MaquinadeEscrever(santuB)
                                            print('')
                                            print('~' * 100)
                                            print('')
                                            print('OPONENTE')
                                            print('')
                                            Aquarius()
                                            print('')
                                            casadeAquarius()
                                            print('')
                                            print('Você: ')
                                            DragaoAtaque()
                                            print('')
                                            AquariusAtaque()
                                            time.sleep(1)
                                            if sorte == 'Você Venceu':
                                                MaquinadeEscrever(venceu).mensagem
                                                print('')
                                                print('Oponente: ')
                                                MaquinadeEscrever(vilaoDe).mensagem
                                                print('')
                                                print('~' * 100)
                                                print('')
                                                MaquinadeEscrever(santuB)
                                                print('')
                                                print('~' * 100)
                                                print('')
                                                print('OPONENTE')
                                                print('')
                                                Peixes()
                                                print('')
                                                casadePeixes()
                                                print('')
                                                print('Você: ')
                                                DragaoAtaque()
                                                print('')
                                                PeixesAtaque()
                                                time.sleep(1)
                                                if sorte == 'Você Venceu':
                                                    MaquinadeEscrever(venceu).mensagem
                                                    print('')
                                                    print('Oponente: ')
                                                    MaquinadeEscrever(vilaoDe).mensagem
                                                    print('')
                                                    print('~' * 100)
                                                    print('Parabéns Você venceu o jogo!')





    else:
        print('')
        MaquinadeEscrever(derrota).mensagem
        print('')
        print('Oponente: ')
        MaquinadeEscrever(vilaoVi).mensagem
        print('')
        print('Fim de Jogo')
elif id == 'C':
    time.sleep(1)
    print('~' * 100)
    dados = 'EIS OS DADOS SOBRE TEU PERSONAGEM!'
    MaquinadeEscrever(dados).mensagem
    time.sleep(1)
    Cisne()
    print('~' * 100)
    MaquinadeEscrever(santuA).mensagem
    print('~' * 100)
    print('OPONENTE')
    print('~' * 100)
    Aries()
    print('')
    casadeAries()
    print('')
    print('Você: ')
    CisneAtaque()
    print('')
    AriesAtaque()
    time.sleep(1)
    print('')

    if sorte == 'Você Venceu':
        MaquinadeEscrever(venceu).mensagem
        print('')
        print('Oponente: ')
        MaquinadeEscrever(vilaoDe).mensagem
        print('')
        print('~' * 100)
        print('')
        MaquinadeEscrever(santuB)
        print('')
        print('~' * 100)
        print('')
        print('OPONENTE')
        print('')
        Touros()
        print('')
        casadeTouros()
        print('')
        print('Você: ')
        CisneAtaque()
        print('')
        TourosAtaque()
        time.sleep(1)
        print('')
        if sorte == 'Você Venceu':
            MaquinadeEscrever(venceu).mensagem
            print('')
            print('Oponente: ')
            MaquinadeEscrever(vilaoDe).mensagem
            print('')
            print('~' * 100)
            print('')
            MaquinadeEscrever(santuB)
            print('')
            print('~' * 100)
            print('')
            print('OPONENTE')
            print('')
            Gemeos()
            print('')
            casaDeGemeos()
            print('')
            print('Você: ')
            CisneAtaque()
            print('')
            GemeosAtaque()
            time.sleep(1)
            print('')
            if sorte == 'Você Venceu':
                MaquinadeEscrever(venceu).mensagem
                print('')
                print('Oponente: ')
                MaquinadeEscrever(vilaoDe).mensagem
                print('')
                print('~' * 100)
                print('')
                MaquinadeEscrever(santuB)
                print('')
                print('~' * 100)
                print('')
                print('OPONENTE')
                print('')
                Cancer()
                print('')
                casaDeCancer()
                print('')
                print('Você: ')
                CisneAtaque()
                print('')
                CancerAtaque()
                time.sleep(1)
                if sorte == 'Você Venceu':
                    MaquinadeEscrever(venceu).mensagem
                    print('')
                    print('Oponente: ')
                    MaquinadeEscrever(vilaoDe).mensagem
                    print('')
                    print('~' * 100)
                    print('')
                    MaquinadeEscrever(santuB)
                    print('')
                    print('~' * 100)
                    print('')
                    print('OPONENTE')
                    print('')
                    Leao()
                    print('')
                    casadeLeao()
                    print('')
                    print('Você: ')
                    CisneAtaque()
                    print('')
                    LeaoAtaque()
                    time.sleep(1)
                    if sorte == 'Você Venceu':
                        MaquinadeEscrever(venceu).mensagem
                        print('')
                        print('Oponente: ')
                        MaquinadeEscrever(vilaoDe).mensagem
                        print('')
                        print('~' * 100)
                        print('')
                        MaquinadeEscrever(santuB)
                        print('')
                        print('~' * 100)
                        print('')
                        print('OPONENTE')
                        print('')
                        Virgem()
                        print('')
                        casadeVirgem()
                        print('')
                        print('Você: ')
                        CisneAtaque()
                        print('')
                        VirgemAtaque()
                        time.sleep(1)
                        if sorte == 'Você Venceu':
                            MaquinadeEscrever(venceu).mensagem
                            print('')
                            print('Oponente: ')
                            MaquinadeEscrever(vilaoDe).mensagem
                            print('')
                            print('~' * 100)
                            print('')
                            MaquinadeEscrever(santuB)
                            print('')
                            print('~' * 100)
                            print('')
                            print('OPONENTE')
                            print('')
                            Libra()
                            print('')
                            casadeLibra()
                            print('')
                            print('Você: ')
                            CisneAtaque()
                            print('')
                            LibraAtaque()
                            time.sleep(1)
                            if sorte == 'Você Venceu':
                                MaquinadeEscrever(venceu).mensagem
                                print('')
                                print('Oponente: ')
                                MaquinadeEscrever(vilaoDe).mensagem
                                print('')
                                print('~' * 100)
                                print('')
                                MaquinadeEscrever(santuB)
                                print('')
                                print('~' * 100)
                                print('')
                                print('OPONENTE')
                                print('')
                                Escorpiao()
                                print('')
                                casadeEscorpiao()
                                print('')
                                print('Você: ')
                                CisneAtaque()
                                print('')
                                EscorpiaoAtaque()
                                time.sleep(1)
                                if sorte == 'Você Venceu':
                                    MaquinadeEscrever(venceu).mensagem
                                    print('')
                                    print('Oponente: ')
                                    MaquinadeEscrever(vilaoDe).mensagem
                                    print('')
                                    print('~' * 100)
                                    print('')
                                    MaquinadeEscrever(santuB)
                                    print('')
                                    print('~' * 100)
                                    print('')
                                    print('OPONENTE')
                                    print('')
                                    Sagitario()
                                    print('')
                                    casadeSagitario()
                                    print('')
                                    print('Você: ')
                                    CisneAtaque()
                                    print('')
                                    SagitarioAtaque()
                                    time.sleep(1)
                                    if sorte == 'Você Venceu':
                                        MaquinadeEscrever(venceu).mensagem
                                        print('')
                                        print('Oponente: ')
                                        MaquinadeEscrever(vilaoDe).mensagem
                                        print('')
                                        print('~' * 100)
                                        print('')
                                        MaquinadeEscrever(santuB)
                                        print('')
                                        print('~' * 100)
                                        print('')
                                        print('OPONENTE')
                                        print('')
                                        Capricornio()
                                        print('')
                                        casadeCapricornio()
                                        print('')
                                        print('Você: ')
                                        CisneAtaque()
                                        print('')
                                        CapricornioAtaque()
                                        time.sleep(1)
                                        if sorte == 'Você Venceu':
                                            MaquinadeEscrever(venceu).mensagem
                                            print('')
                                            print('Oponente: ')
                                            MaquinadeEscrever(vilaoDe).mensagem
                                            print('')
                                            print('~' * 100)
                                            print('')
                                            MaquinadeEscrever(santuB)
                                            print('')
                                            print('~' * 100)
                                            print('')
                                            print('OPONENTE')
                                            print('')
                                            Aquarius()
                                            print('')
                                            casadeAquarius()
                                            print('')
                                            print('Você: ')
                                            CisneAtaque()
                                            print('')
                                            AquariusAtaque()
                                            time.sleep(1)
                                            if sorte == 'Você Venceu':
                                                MaquinadeEscrever(venceu).mensagem
                                                print('')
                                                print('Oponente: ')
                                                MaquinadeEscrever(vilaoDe).mensagem
                                                print('')
                                                print('~' * 100)
                                                print('')
                                                MaquinadeEscrever(santuB)
                                                print('')
                                                print('~' * 100)
                                                print('')
                                                print('OPONENTE')
                                                print('')
                                                Peixes()
                                                print('')
                                                casadePeixes()
                                                print('')
                                                print('Você: ')
                                                CisneAtaque()
                                                print('')
                                                PeixesAtaque()
                                                time.sleep(1)
                                                if sorte == 'Você Venceu':
                                                    MaquinadeEscrever(venceu).mensagem
                                                    print('')
                                                    print('Oponente: ')
                                                    MaquinadeEscrever(vilaoDe).mensagem
                                                    print('')
                                                    print('~' * 100)
                                                    print('Parabéns Você venceu o jogo!')





    else:
        print('')
        MaquinadeEscrever(derrota).mensagem
        print('')
        print('Oponente: ')
        MaquinadeEscrever(vilaoVi).mensagem
        print('')
        print('Fim de Jogo')
elif id == 'D':
    time.sleep(1)
    print('~' * 100)
    dados = 'EIS OS DADOS SOBRE TEU PERSONAGEM!'
    MaquinadeEscrever(dados).mensagem
    Andromeda()
    MaquinadeEscrever(santuA).mensagem
    print('~' * 100)
    print('OPONENTE')
    print('~' * 100)
    Aries()
    print('')
    casadeAries()
    print('')
    print('Você: ')
    AndromedaAtaque()
    print('')
    AriesAtaque()
    time.sleep(1)
    print('')

    if sorte == 'Você Venceu':
        MaquinadeEscrever(venceu).mensagem
        print('')
        print('Oponente: ')
        MaquinadeEscrever(vilaoDe).mensagem
        print('')
        print('~' * 100)
        print('')
        MaquinadeEscrever(santuB)
        print('')
        print('~' * 100)
        print('')
        print('OPONENTE')
        print('')
        Touros()
        print('')
        casadeTouros()
        print('')
        print('Você: ')
        AndromedaAtaque()
        print('')
        TourosAtaque()
        time.sleep(1)
        print('')
        if sorte == 'Você Venceu':
            MaquinadeEscrever(venceu).mensagem
            print('')
            print('Oponente: ')
            MaquinadeEscrever(vilaoDe).mensagem
            print('')
            print('~' * 100)
            print('')
            MaquinadeEscrever(santuB)
            print('')
            print('~' * 100)
            print('')
            print('OPONENTE')
            print('')
            Gemeos()
            print('')
            casaDeGemeos()
            print('')
            print('Você: ')
            AndromedaAtaque()
            print('')
            GemeosAtaque()
            time.sleep(1)
            print('')
            if sorte == 'Você Venceu':
                MaquinadeEscrever(venceu).mensagem
                print('')
                print('Oponente: ')
                MaquinadeEscrever(vilaoDe).mensagem
                print('')
                print('~' * 100)
                print('')
                MaquinadeEscrever(santuB)
                print('')
                print('~' * 100)
                print('')
                print('OPONENTE')
                print('')
                Cancer()
                print('')
                casaDeCancer()
                print('')
                print('Você: ')
                AndromedaAtaque()
                print('')
                CancerAtaque()
                time.sleep(1)
                if sorte == 'Você Venceu':
                    MaquinadeEscrever(venceu).mensagem
                    print('')
                    print('Oponente: ')
                    MaquinadeEscrever(vilaoDe).mensagem
                    print('')
                    print('~' * 100)
                    print('')
                    MaquinadeEscrever(santuB)
                    print('')
                    print('~' * 100)
                    print('')
                    print('OPONENTE')
                    print('')
                    Leao()
                    print('')
                    casadeLeao()
                    print('')
                    print('Você: ')
                    AndromedaAtaque()
                    print('')
                    LeaoAtaque()
                    time.sleep(1)
                    if sorte == 'Você Venceu':
                        MaquinadeEscrever(venceu).mensagem
                        print('')
                        print('Oponente: ')
                        MaquinadeEscrever(vilaoDe).mensagem
                        print('')
                        print('~' * 100)
                        print('')
                        MaquinadeEscrever(santuB)
                        print('')
                        print('~' * 100)
                        print('')
                        print('OPONENTE')
                        print('')
                        Virgem()
                        print('')
                        casadeVirgem()
                        print('')
                        print('Você: ')
                        AndromedaAtaque()
                        print('')
                        VirgemAtaque()
                        time.sleep(1)
                        if sorte == 'Você Venceu':
                            MaquinadeEscrever(venceu).mensagem
                            print('')
                            print('Oponente: ')
                            MaquinadeEscrever(vilaoDe).mensagem
                            print('')
                            print('~' * 100)
                            print('')
                            MaquinadeEscrever(santuB)
                            print('')
                            print('~' * 100)
                            print('')
                            print('OPONENTE')
                            print('')
                            Libra()
                            print('')
                            casadeLibra()
                            print('')
                            print('Você: ')
                            AndromedaAtaque()
                            print('')
                            LibraAtaque()
                            time.sleep(1)
                            if sorte == 'Você Venceu':
                                MaquinadeEscrever(venceu).mensagem
                                print('')
                                print('Oponente: ')
                                MaquinadeEscrever(vilaoDe).mensagem
                                print('')
                                print('~' * 100)
                                print('')
                                MaquinadeEscrever(santuB)
                                print('')
                                print('~' * 100)
                                print('')
                                print('OPONENTE')
                                print('')
                                Escorpiao()
                                print('')
                                casadeEscorpiao()
                                print('')
                                print('Você: ')
                                AndromedaAtaque()
                                print('')
                                EscorpiaoAtaque()
                                time.sleep(1)
                                if sorte == 'Você Venceu':
                                    MaquinadeEscrever(venceu).mensagem
                                    print('')
                                    print('Oponente: ')
                                    MaquinadeEscrever(vilaoDe).mensagem
                                    print('')
                                    print('~' * 100)
                                    print('')
                                    MaquinadeEscrever(santuB)
                                    print('')
                                    print('~' * 100)
                                    print('')
                                    print('OPONENTE')
                                    print('')
                                    Sagitario()
                                    print('')
                                    casadeSagitario()
                                    print('')
                                    print('Você: ')
                                    AndromedaAtaque()
                                    print('')
                                    SagitarioAtaque()
                                    time.sleep(1)
                                    if sorte == 'Você Venceu':
                                        MaquinadeEscrever(venceu).mensagem
                                        print('')
                                        print('Oponente: ')
                                        MaquinadeEscrever(vilaoDe).mensagem
                                        print('')
                                        print('~' * 100)
                                        print('')
                                        MaquinadeEscrever(santuB)
                                        print('')
                                        print('~' * 100)
                                        print('')
                                        print('OPONENTE')
                                        print('')
                                        Capricornio()
                                        print('')
                                        casadeCapricornio()
                                        print('')
                                        print('Você: ')
                                        AndromedaAtaque()
                                        print('')
                                        CapricornioAtaque()
                                        time.sleep(1)
                                        if sorte == 'Você Venceu':
                                            MaquinadeEscrever(venceu).mensagem
                                            print('')
                                            print('Oponente: ')
                                            MaquinadeEscrever(vilaoDe).mensagem
                                            print('')
                                            print('~' * 100)
                                            print('')
                                            MaquinadeEscrever(santuB)
                                            print('')
                                            print('~' * 100)
                                            print('')
                                            print('OPONENTE')
                                            print('')
                                            Aquarius()
                                            print('')
                                            casadeAquarius()
                                            print('')
                                            print('Você: ')
                                            AndromedaAtaque()
                                            print('')
                                            AquariusAtaque()
                                            time.sleep(1)
                                            if sorte == 'Você Venceu':
                                                MaquinadeEscrever(venceu).mensagem
                                                print('')
                                                print('Oponente: ')
                                                MaquinadeEscrever(vilaoDe).mensagem
                                                print('')
                                                print('~' * 100)
                                                print('')
                                                MaquinadeEscrever(santuB)
                                                print('')
                                                print('~' * 100)
                                                print('')
                                                print('OPONENTE')
                                                print('')
                                                Peixes()
                                                print('')
                                                casadePeixes()
                                                print('')
                                                print('Você: ')
                                                AndromedaAtaque()
                                                print('')
                                                PeixesAtaque()
                                                time.sleep(1)
                                                if sorte == 'Você Venceu':
                                                    MaquinadeEscrever(venceu).mensagem
                                                    print('')
                                                    print('Oponente: ')
                                                    MaquinadeEscrever(vilaoDe).mensagem
                                                    print('')
                                                    print('~' * 100)
                                                    print('Parabéns Você venceu o jogo!')





    else:
        print('')
        MaquinadeEscrever(derrota).mensagem
        print('')
        print('Oponente: ')
        MaquinadeEscrever(vilaoVi).mensagem
        print('')
        print('Fim de Jogo')
elif id == 'E':
    time.sleep(1)
    print('~' * 100)
    dados = 'EIS OS DADOS SOBRE TEU PERSONAGEM!'
    MaquinadeEscrever(dados).mensagem
    Fenix()
    MaquinadeEscrever(santuA).mensagem
    print('~' * 100)
    print('OPONENTE')
    print('~' * 100)
    Aries()
    print('')
    casadeAries()
    print('')
    print('Você: ')
    FenixAtaque()
    print('')
    AriesAtaque()
    time.sleep(1)
    print('')

    if sorte == 'Você Venceu':
        MaquinadeEscrever(venceu).mensagem
        print('')
        print('Oponente: ')
        MaquinadeEscrever(vilaoDe).mensagem
        print('')
        print('~' * 100)
        print('')
        MaquinadeEscrever(santuB)
        print('')
        print('~' * 100)
        print('')
        print('OPONENTE')
        print('')
        Touros()
        print('')
        casadeTouros()
        print('')
        print('Você: ')
        FenixAtaque()
        print('')
        TourosAtaque()
        time.sleep(1)
        print('')
        if sorte == 'Você Venceu':
            MaquinadeEscrever(venceu).mensagem
            print('')
            print('Oponente: ')
            MaquinadeEscrever(vilaoDe).mensagem
            print('')
            print('~' * 100)
            print('')
            MaquinadeEscrever(santuB)
            print('')
            print('~' * 100)
            print('')
            print('OPONENTE')
            print('')
            Gemeos()
            print('')
            casaDeGemeos()
            print('')
            print('Você: ')
            FenixAtaque()
            print('')
            GemeosAtaque()
            time.sleep(1)
            print('')
            if sorte == 'Você Venceu':
                MaquinadeEscrever(venceu).mensagem
                print('')
                print('Oponente: ')
                MaquinadeEscrever(vilaoDe).mensagem
                print('')
                print('~' * 100)
                print('')
                MaquinadeEscrever(santuB)
                print('')
                print('~' * 100)
                print('')
                print('OPONENTE')
                print('')
                Cancer()
                print('')
                casaDeCancer()
                print('')
                print('Você: ')
                FenixAtaque()
                print('')
                CancerAtaque()
                time.sleep(1)
                if sorte == 'Você Venceu':
                    MaquinadeEscrever(venceu).mensagem
                    print('')
                    print('Oponente: ')
                    MaquinadeEscrever(vilaoDe).mensagem
                    print('')
                    print('~' * 100)
                    print('')
                    MaquinadeEscrever(santuB)
                    print('')
                    print('~' * 100)
                    print('')
                    print('OPONENTE')
                    print('')
                    Leao()
                    print('')
                    casadeLeao()
                    print('')
                    print('Você: ')
                    FenixAtaque()
                    print('')
                    LeaoAtaque()
                    time.sleep(1)
                    if sorte == 'Você Venceu':
                        MaquinadeEscrever(venceu).mensagem
                        print('')
                        print('Oponente: ')
                        MaquinadeEscrever(vilaoDe).mensagem
                        print('')
                        print('~' * 100)
                        print('')
                        MaquinadeEscrever(santuB)
                        print('')
                        print('~' * 100)
                        print('')
                        print('OPONENTE')
                        print('')
                        Virgem()
                        print('')
                        casadeVirgem()
                        print('')
                        print('Você: ')
                        FenixAtaque()
                        print('')
                        VirgemAtaque()
                        time.sleep(1)
                        if sorte == 'Você Venceu':
                            MaquinadeEscrever(venceu).mensagem
                            print('')
                            print('Oponente: ')
                            MaquinadeEscrever(vilaoDe).mensagem
                            print('')
                            print('~' * 100)
                            print('')
                            MaquinadeEscrever(santuB)
                            print('')
                            print('~' * 100)
                            print('')
                            print('OPONENTE')
                            print('')
                            Libra()
                            print('')
                            casadeLibra()
                            print('')
                            print('Você: ')
                            FenixAtaque()
                            print('')
                            LibraAtaque()
                            time.sleep(1)
                            if sorte == 'Você Venceu':
                                MaquinadeEscrever(venceu).mensagem
                                print('')
                                print('Oponente: ')
                                MaquinadeEscrever(vilaoDe).mensagem
                                print('')
                                print('~' * 100)
                                print('')
                                MaquinadeEscrever(santuB)
                                print('')
                                print('~' * 100)
                                print('')
                                print('OPONENTE')
                                print('')
                                Escorpiao()
                                print('')
                                casadeEscorpiao()
                                print('')
                                print('Você: ')
                                FenixAtaque()
                                print('')
                                EscorpiaoAtaque()
                                time.sleep(1)
                                if sorte == 'Você Venceu':
                                    MaquinadeEscrever(venceu).mensagem
                                    print('')
                                    print('Oponente: ')
                                    MaquinadeEscrever(vilaoDe).mensagem
                                    print('')
                                    print('~' * 100)
                                    print('')
                                    MaquinadeEscrever(santuB)
                                    print('')
                                    print('~' * 100)
                                    print('')
                                    print('OPONENTE')
                                    print('')
                                    Sagitario()
                                    print('')
                                    casadeSagitario()
                                    print('')
                                    print('Você: ')
                                    FenixAtaque()
                                    print('')
                                    SagitarioAtaque()
                                    time.sleep(1)
                                    if sorte == 'Você Venceu':
                                        MaquinadeEscrever(venceu).mensagem
                                        print('')
                                        print('Oponente: ')
                                        MaquinadeEscrever(vilaoDe).mensagem
                                        print('')
                                        print('~' * 100)
                                        print('')
                                        MaquinadeEscrever(santuB)
                                        print('')
                                        print('~' * 100)
                                        print('')
                                        print('OPONENTE')
                                        print('')
                                        Capricornio()
                                        print('')
                                        casadeCapricornio()
                                        print('')
                                        print('Você: ')
                                        FenixAtaque()
                                        print('')
                                        CapricornioAtaque()
                                        time.sleep(1)
                                        if sorte == 'Você Venceu':
                                            MaquinadeEscrever(venceu).mensagem
                                            print('')
                                            print('Oponente: ')
                                            MaquinadeEscrever(vilaoDe).mensagem
                                            print('')
                                            print('~' * 100)
                                            print('')
                                            MaquinadeEscrever(santuB)
                                            print('')
                                            print('~' * 100)
                                            print('')
                                            print('OPONENTE')
                                            print('')
                                            Aquarius()
                                            print('')
                                            casadeAquarius()
                                            print('')
                                            print('Você: ')
                                            FenixAtaque()
                                            print('')
                                            AquariusAtaque()
                                            time.sleep(1)
                                            if sorte == 'Você Venceu':
                                                MaquinadeEscrever(venceu).mensagem
                                                print('')
                                                print('Oponente: ')
                                                MaquinadeEscrever(vilaoDe).mensagem
                                                print('')
                                                print('~' * 100)
                                                print('')
                                                MaquinadeEscrever(santuB)
                                                print('')
                                                print('~' * 100)
                                                print('')
                                                print('OPONENTE')
                                                print('')
                                                Peixes()
                                                print('')
                                                casadePeixes()
                                                print('')
                                                print('Você: ')
                                                FenixAtaque()
                                                print('')
                                                PeixesAtaque()
                                                time.sleep(1)
                                                if sorte == 'Você Venceu':
                                                    MaquinadeEscrever(venceu).mensagem
                                                    print('')
                                                    print('Oponente: ')
                                                    MaquinadeEscrever(vilaoDe).mensagem
                                                    print('')
                                                    print('~' * 100)
                                                    print('Parabéns Você venceu o jogo!')





    else:
        print('')
        MaquinadeEscrever(derrota).mensagem
        print('')
        print('Oponente: ')
        MaquinadeEscrever(vilaoVi).mensagem
        print('')
        print('Fim de Jogo')



