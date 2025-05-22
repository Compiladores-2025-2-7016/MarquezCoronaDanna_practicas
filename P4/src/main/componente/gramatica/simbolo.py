from enum import Enum
from typing import Union
from ..clase_lexica import ClaseLexica, NoTerminal


class Simbolo:
    class SimTipo(Enum):
        TERMINAL = "terminal"
        NO_TERMINAL = "no_terminal"
    
    def __init__(self, sim: Union[NoTerminal, ClaseLexica], tipo: SimTipo):
        self.sim = sim
        self.tipo = tipo

    def __repr__(self):
        return f"Simbolo(sim={self.sim}, tipo={self.tipo})"
    
    def __eq__(self, other):
        if not isinstance(other, Simbolo):
            return NotImplemented
        return self.sim.value == other.sim.value and self.tipo.value == other.tipo.value

    def __hash__(self):
        return hash(self.sim.value) 