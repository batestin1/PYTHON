#classe para trablhar com maquina de escrever

import sys, time, os

class MaquinadeEscrever():

    def __init__(self, mensagem):
        self.mensagem = mensagem


        for char in mensagem:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
