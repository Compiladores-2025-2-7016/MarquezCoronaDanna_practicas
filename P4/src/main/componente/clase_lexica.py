from enum import Enum

class ClaseLexica(Enum): #Estos serán miembro de alguna coordenada en la tabla LL(1)
    EOF = 0
    ESPACIO = 5
    NUMERO = 1 
    PLUS = 2


class NoTerminal(Enum): #Estos serán miembro de alguna coordenada en la tabla LL(1)
    epsilon = ''
    s = "s"
    sprim = "sprim"