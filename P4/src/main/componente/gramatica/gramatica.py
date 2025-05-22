from typing import List

from ..gramatica.produccion import Produccion
from ..gramatica.simbolo import Simbolo

class Gramatica:
    def __init__(self):
        self.simbolos: List[Simbolo] = []
        self.producciones: List[Produccion] = []

    def add_sim(self, simbolo: Simbolo):
        self.simbolos.append(simbolo)

    def add_prod(self, produccion: Produccion):
        self.producciones.append(produccion)

    def get_sim(self, valor: int) -> Simbolo:
        for simbolo in self.simbolos:
            if simbolo.sim.value == valor:
                return simbolo
        raise Exception("No existe un símbolo en la gramática con ese valor")
    
    def get_prod(self, idx: int) -> Produccion:
        return self.producciones[idx]
    

    
