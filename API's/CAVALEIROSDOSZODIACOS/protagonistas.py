
from personas import Cavaleiro
from typewriter import MaquinadeEscrever


def Pegasus():
    global peg
    global mensagem
    global texto
    peg = Cavaleiro(407)
    MaquinadeEscrever(peg.texto).mensagem


def PegasusAtaque():
    global peg
    global mensagem
    global texto
    peg = Cavaleiro(407)
    MaquinadeEscrever(peg.textoAtaque).mensagem


def Dragao():
    global drag
    global mensagem
    global texto
    drag = Cavaleiro(430)
    MaquinadeEscrever(drag.texto).mensagem
    MaquinadeEscrever(drag.textoAtaque).mensagem

def DragaoAtaque():
    global drag
    global mensagem
    global texto
    drag = Cavaleiro(430)
    MaquinadeEscrever(drag.textoAtaque).mensagem

def Cisne():
    global cis
    global mensagem
    global texto
    cis = Cavaleiro(198)
    MaquinadeEscrever(cis.texto).mensagem


def CisneAtaque():
    global cis
    global mensagem
    global texto
    cis = Cavaleiro(198)
    MaquinadeEscrever(cis.textoAtaque).mensagem


def Andromeda():
    global andro
    global mensagem
    global texto
    andro = Cavaleiro(443)
    MaquinadeEscrever(andro.texto).mensagem

def AndromedaAtaque():
    global andro
    global mensagem
    global texto
    andro = Cavaleiro(443)
    MaquinadeEscrever(andro.textoAtaque).mensagem

def Fenix():
    global fenix
    global mensagem
    global texto
    fenix = Cavaleiro(213)
    MaquinadeEscrever(fenix.texto).mensagem


def FenixAtaque():
    global fenix
    global mensagem
    global texto
    fenix = Cavaleiro(213)
    MaquinadeEscrever(fenix.textoAtaque).mensagem
