from typing import Dict, List
from analisis.lexico import Lexer
from componente.gramatica.produccion import Produccion
from componente.gramatica.simbolo import Simbolo
from componente.clase_lexica import ClaseLexica, NoTerminal
from componente.gramatica.gramatica import Gramatica


class ParserLL:

    def __init__(self, lexer: Lexer):
        self.an_lexico = lexer
        self.token_actual = 0
        self.gramatica = Gramatica()
        self.tabla: Dict[Simbolo, Dict[Simbolo, Produccion]] = {} # self.tabla[S_inicial][NUMERO] -> Produccion

    def eat(self):
        # hint: ip++ == self.eat()
        try:
            tok = self.an_lexico.lexer.token()
            if not tok: # No hay mas entrada
                self.token_actual = 0
            else:
                self.token_actual = ClaseLexica[tok.type].value
        except Exception as e:
            print("No fue posible leer el siguiente token. {excp}".format(excp=str(e)))


    def error(self, msg: str):
        print("ERROR DE SINTAXIS: {mensaje}. En la línea {linea}".format(mensaje=msg, 
                                                                         linea=self.an_lexico.lexer.lineno))
        exit(1)



    ########################################################################
    ##                                                                    ##
    ##                    TODO: Hardcodeo de la gramática                 ##
    ##                                                                    ##
    ########################################################################

    def load_syms(self):
        # TODO: Llenar la lista de símbolos de G.
        # hint: self.gramatica.simbolos.extend([])

        # No Terminales (incluímos epsilon porque en la tabla es un miembro de coordenada)
        s = Simbolo(NoTerminal.s, Simbolo.SimTipo.NO_TERMINAL)
        sprim = Simbolo(NoTerminal.sprim, Simbolo.SimTipo.NO_TERMINAL)
        epsilon = Simbolo(NoTerminal.epsilon, Simbolo.SimTipo.NO_TERMINAL)

        # Terminales
        num = Simbolo(ClaseLexica.NUMERO, Simbolo.SimTipo.TERMINAL)
        plus = Simbolo(ClaseLexica.PLUS, Simbolo.SimTipo.TERMINAL)
        eof = Simbolo(ClaseLexica.EOF, Simbolo.SimTipo.TERMINAL)

        self.gramatica.simbolos.extend([s, sprim, epsilon, num, plus, eof])



    def load_prods(self):
        # TODO: Llenar la lista de producciones de G.
        # hint: 
        # self.gramatica.producciones.extend([])
        # Alias
        s = Simbolo(NoTerminal.s, Simbolo.SimTipo.NO_TERMINAL)
        sprim = Simbolo(NoTerminal.sprim, Simbolo.SimTipo.NO_TERMINAL)
        epsilon = Simbolo(NoTerminal.epsilon, Simbolo.SimTipo.NO_TERMINAL)

        num = Simbolo(ClaseLexica.NUMERO, Simbolo.SimTipo.TERMINAL)
        plus = Simbolo(ClaseLexica.PLUS, Simbolo.SimTipo.TERMINAL)

        # Producciones
        p1 = Produccion(s, [num, sprim])                 # s → NUMERO sprim
        p2 = Produccion(sprim, [plus, num, sprim])       # sprim → PLUS NUMERO sprim
        p3 = Produccion(sprim, [epsilon])                # sprim → ε

        self.gramatica.producciones.extend([p1, p2, p3])


    def load_table(self):
        # TODO: Llenar la tabla LL(1)
        # hint:
        # self.tabla[s] = {} 
        # self.tabla[s][numero] = Produccion(?, [?,?,...,?])
        # Alias
        s = Simbolo(NoTerminal.s, Simbolo.SimTipo.NO_TERMINAL)
        sprim = Simbolo(NoTerminal.sprim, Simbolo.SimTipo.NO_TERMINAL)
        epsilon = Simbolo(NoTerminal.epsilon, Simbolo.SimTipo.NO_TERMINAL)

        num = Simbolo(ClaseLexica.NUMERO, Simbolo.SimTipo.TERMINAL)
        plus = Simbolo(ClaseLexica.PLUS, Simbolo.SimTipo.TERMINAL)
        eof = Simbolo(ClaseLexica.EOF, Simbolo.SimTipo.TERMINAL)

        # Producciones (mismo orden que en load_prods)
        p1 = Produccion(s, [num, sprim])
        p2 = Produccion(sprim, [plus, num, sprim])
        p3 = Produccion(sprim, [epsilon])

        self.tabla[s] = {num: p1}
        self.tabla[sprim] = {
            plus: p2,
            eof: p3
        }

    def parse(self):
        self.load_syms()
        self.load_prods()
        self.load_table()
        # TODO: Implementar el algoritmo de An. Sintáctico LL(1)
        # Inicializar la pila con símbolo inicial y EOF
        stack: List[Simbolo] = []

        eof = Simbolo(ClaseLexica.EOF, Simbolo.SimTipo.TERMINAL)
        start = Simbolo(NoTerminal.s, Simbolo.SimTipo.NO_TERMINAL)

        stack.append(eof)
        stack.append(start)

        # Primer token de entrada
        self.eat()
        ip = self.token_actual

        while stack:
            x = stack.pop()

            if x.tipo == Simbolo.SimTipo.TERMINAL:
                if x.sim.value == ip:
                    self.eat()
                    ip = self.token_actual
                else:
                    self.error(f"Se esperaba {x}, pero se encontró {ip}")
            elif x.tipo == Simbolo.SimTipo.NO_TERMINAL:
                entrada = Simbolo(ClaseLexica(ip), Simbolo.SimTipo.TERMINAL)
                if x in self.tabla and entrada in self.tabla[x]:
                    produccion = self.tabla[x][entrada]
                    #print(produccion)  Muestra la derivación

                    # Apilar RHS en orden inverso (excepto epsilon)
                    for sym in reversed(produccion.cuerpo):
                        if sym.sim != NoTerminal.epsilon:
                            stack.append(sym)
                else:
                    self.error(f"No hay producción para {x} con entrada {entrada}")
            else:
                self.error(f"Símbolo desconocido en la pila: {x}")

        if ip == 0:
            print("La cadena es aceptada")
        else:
            self.error("Tokens restantes sin consumir.")

        """
        Sea w una cadena de entrada (código fuente), STACK una pila, X un símbolo no terminal, Yi ∈ NUT y M una tabla de Análisis Sintáctico LL(1), 
        1. ip := w[0], x := top(STACK)
        2. Mientras x ≠ $ hacer:
            a. Si x == ip, entonces pop(STACK); ip++;
            b. si no, si x ∈ T: error( );
            c. si no, si M[x, ip] == ☐: error( );
            d. si no, si M[x, ip] == X ⟶ Y1Y2 ... Yk:
                i. imprimir X ⟶ Y1Y2 ... Yk ;
                ii. STACK.pop();
                iii. STACK.push(Yk,Yk-1, ..., Y2, Y1); 
                    Nota: Epsilon puede omitirse del push dado que no es un símbolo o manejarse de otra manera en las condiciones a.-d.
            e. x := top(STACK)
        """
    


    