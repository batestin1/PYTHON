#construindo as casas do zodiaco

from personas import Cavaleiro
from typewriter import MaquinadeEscrever
import time



def casadeAries():
    global ars
    global mensagem
    global texto
    global apresentacao

    ars = Cavaleiro(325)
    time.sleep(1)
    print("")
    print('~'*100)
    time.sleep(1)
    print('~' * 100)
    ariestexto = f"""OPONENTE: 
            Você acaba de adentrar a Casa de Áries,
            eu sou {ars.nome} de Áries, e protetor de Athenas.
            Seja você quem for, este é meu único aviso!
            Saia ou morra!"""
    print('~' * 100)
    MaquinadeEscrever(ariestexto).mensagem



def casadeTouros():
    global tou
    global mensagem
    global texto
    global apresentacao

    tou = Cavaleiro(18)

    time.sleep(1)
    print("")
    print('~' * 100)
    time.sleep(1)
    print('~' * 100)
    apresentacao = {f"""
                OPONENTE:
                Você acaba de adentrar a Casa de Touros,
                eu sou {tou.nome} de Touro, e protetor de Athenas.
                Aqui ninguém passa, aqui ninguém volta. Lute agora, ou morra!"""}
    print('~' * 100)
    MaquinadeEscrever(apresentacao).mensagem

def casaDeGemeos():
    global gem
    global mensagem
    global texto

    gem = Cavaleiro(399)


    time.sleep(1)
    print("")
    print('~' * 100)
    time.sleep(1)
    print('~' * 100)
    apresentacao = {f"""OPONENTE:
                    Você acaba de adentrar a Casa de Gêmeos,
                    eu sou {gem.nome} de Gêmeos, protetor de Athenas, e o mais forte
                    dos Cavaleiros de Ouro. Se chegou até aqui, indepdente de quem seja,
                    não seguirá em frente. Irei garantir a sua morte! """}
    print('~' * 100)
    MaquinadeEscrever(apresentacao).mensagem


def casaDeCancer():
    global cam
    global mensagem
    global texto

    cam = Cavaleiro(102)

    time.sleep(1)
    print("")
    print('~' * 100)
    time.sleep(1)
    print('~' * 100)
    apresentacao = {f"""OPONENTE:
                   Você acaba de adentrar a Casa de Cancer.
                   Aqui só a morte pode lhe fazer companhia.
                   eu sou {cam.nome} de Cancer, e este é o seu inferno!
                   Morra verme, miseravel!"""}
    print('~' * 100)
    MaquinadeEscrever(apresentacao).mensagem


def casadeLeao():
    global lion
    global mensagem
    global texto


    lion = Cavaleiro(10)


    time.sleep(1)
    print("")
    print('~' * 100)
    time.sleep(1)
    print('~' * 100)
    apresentacao = {f"""OPONENTE:
                       Você acaba de adentrar a Casa de Leão.
                       É meu dever, por Atena, impedir a sua passagem.
                       eu sou {lion.nome} de Leão.
                       E aqui será vosso túmulo.
                       Morra com a fúria do Leão!
                       """}
    print('~' * 100)
    MaquinadeEscrever(apresentacao).mensagem


def casadeVirgem():
    global virg
    global mensagem
    global texto

    virg = Cavaleiro(420)


    time.sleep(1)
    print("")
    print('~' * 100)
    time.sleep(1)
    print('~' * 100)
    apresentacao = {f""" OPONENTE:
                          Você acaba de adentrar a Casa de Virgem.
                          Quem ousas pertubar minha meditação?
                          Não sabe que eu sou {virg.nome} de Virgem.
                          O homem mais perto de Deus?
                          Não importa.
                          Por sua arrogância, cavarei sua cova
                          Aqui neste santuário!
                          """}
    print('~' * 100)
    MaquinadeEscrever(apresentacao).mensagem

def casadeLibra():
    global lib
    global mensagem
    global texto


    lib = Cavaleiro(113)

    time.sleep(1)
    print("")
    print('~' * 100)
    time.sleep(1)
    print('~' * 100)
    apresentacao = {f"""    
OPONENTE:
Você acaba de adentrar a Casa de Libra.
Eu não posso permitir a sua passagem, 
Nem terei misericórdia de vossa alma.
Eu sou {lib.nome} de Libra.
E minha justiça é sua morte!
                             """}
    print('~' * 100)
    MaquinadeEscrever(apresentacao).mensagem


def casadeEscorpiao():
    global esc
    global mensagem
    global texto


    esc = Cavaleiro(308)


    time.sleep(1)
    print("")
    print('~' * 100)
    time.sleep(1)
    print('~' * 100)
    apresentacao = {f"""OPONENTE:
                                 Você acaba de adentrar a Casa de Escorpião.
                                 Não me importa que tenhas chegado tão longe,
                                 Eu sou {esc.nome} de Escorpião.
                                 Aqui não existe remorso. Aqui não existe perdão.
                                 Apenas a fúria de minhas agulhas
                                 E a impiedosa morte serão teu aconchego!
                                 """}
    print('~' * 100)
    MaquinadeEscrever(apresentacao).mensagem


def casadeSagitario():
    global sag
    global mensagem
    global texto


    sag = Cavaleiro(13)


    time.sleep(1)
    print("")
    print('~' * 100)
    time.sleep(1)
    print('~' * 100)
    apresentacao = {f"""OPONENTE:
                                     Você acaba de adentrar a Casa de Sagitário.
                                     Eu sou {sag.nome} de Sagitário.
                                     Sou o mais fiel dos guardiões de nossa Deusa.
                                     E é meu papel impedir que vermes como você
                                     Avancem...
                                     Então prepara-se para morrer!
                                     """}
    print('~' * 100)
    MaquinadeEscrever(apresentacao).mensagem

def casadeCapricornio():
    global cap
    global mensagem
    global texto


    cap = Cavaleiro(447)


    time.sleep(1)
    print("")
    print('~' * 100)
    time.sleep(1)
    print('~' * 100)
    apresentacao = {f"""OPONENTE:
                                         Você acaba de adentrar a Casa de Capricórnio.
                                         Minha espada está pedindo sangue!
                                         Eu sou {cap.nome} de Capricórnio.
                                         E você vai alimenta-la!
                                         Prepara-se para morrer!
                                         """}
    print('~' * 100)
    MaquinadeEscrever(apresentacao).mensagem


def casadeAquarius():
    global aqu
    global mensagem
    global texto


    aqu = Cavaleiro(75)


    time.sleep(1)
    print("")
    print('~' * 100)
    time.sleep(1)
    print('~' * 100)
    apresentacao = {f"""OPONENTE:
                                             Você acaba de adentrar a Casa de Áquarius.
                                             Aqui apenas reina O Zero Absoluto!
                                             Eu sou {cv.nome} de Áquarius.
                                             E você vai congelar!!
                                             """}
    print('~' * 100)
    MaquinadeEscrever(apresentacao).mensagem


def casadePeixes():
    global pex
    global mensagem
    global texto


    pex = Cavaleiro(32)


    time.sleep(1)
    print("")
    print('~' * 100)
    time.sleep(1)
    print('~' * 100)
    apresentacao = {f"""OPONENTE:
                                                 Você acaba de adentrar a Casa de Peixes
                                                 Esta é sua última aventura.
                                                 Eu sou {pex.nome} de Peixes.
                                                 E neste jardim! 
                                                 Você vai morrer!!
                                                 """}
    print('~' * 100)
    MaquinadeEscrever(apresentacao).mensagem



