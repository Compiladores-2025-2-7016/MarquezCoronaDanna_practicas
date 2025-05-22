from typing import List
from ..gramatica.simbolo import Simbolo


class Produccion:
    
    def __init__(self, cabeza: Simbolo = None, cuerpo: List[Simbolo] = None):
        self.cabeza = cabeza
        self.cuerpo = cuerpo if cuerpo is not None else []
    
    def __str__(self):
        cabeza_str = str(self.cabeza)
        cuerpo_filtrado = [str(simbolo) for simbolo in self.cuerpo]
        cuerpo_str = ' '.join(cuerpo_filtrado)
        return f'{cabeza_str} → {cuerpo_str}'

