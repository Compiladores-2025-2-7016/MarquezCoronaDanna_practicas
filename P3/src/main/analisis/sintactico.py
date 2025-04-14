from analisis.lexico import Lexer
from componente.clase_lexica import ClaseLexica

class Parser:

    def __init__(self, lexer: Lexer):
        self.an_lexico = lexer
        self.token_actual = 0


    def eat(self, clase_lexica: int):
        if self.token_actual == clase_lexica:
            try:
                tok = self.an_lexico.lexer.token()
                if not tok: # No hay mas entrada
                    self.token_actual = 0
                else:
                    self.token_actual = ClaseLexica[tok.type].value
            except Exception as e:
                print("No fue posible leer el siguiente token. {excp}".format(excp=str(e)))
        else:
            print("Se esperaba el token: {actual}".format(actual=self.token_actual))


    def error(self, msg: str):
        print("ERROR DE SINTAXIS: {mensaje}. En la línea {linea}".format(mensaje=msg, 
                                                                         linea=self.an_lexico.lexer.lineno))

    def parse(self):
        try:
            tok = self.an_lexico.lexer.token()
            self.token_actual = ClaseLexica[tok.type].value
        except Exception as e:
            print("No fue posible obtener el primer token de la entrada: {excepcion}".format(excepcion=str(e)))
            exit(1)

        self.S()
        if self.token_actual == 0: # llegamos al EOF sin error
            print("La cadena es aceptada")
        else:
            print("La cadena no pertenece al lenguaje generado por la gramática")

    
    def S(self):
        self.declaraciones()
        self.sentencias()
        

    ########################################################################
    ##                                                                    ##
    ##                    TODO: Funciones por cada NT                     ##
    ##                                                                    ##
    ########################################################################

    def declaraciones(self):
        self.declaracion()
        self.declaraciones_p()

    def declaraciones_p(self):
        if self.token_actual in [ClaseLexica.INT.value, ClaseLexica.FLOAT.value]:
            self.declaracion()
            self.declaraciones_p()

    def declaracion(self):
        self.tipo()
        self.lista_var()
        self.eat(ClaseLexica.PYC.value)

    def tipo(self):
        if self.token_actual == ClaseLexica.INT.value:
            self.eat(ClaseLexica.INT.value)
        elif self.token_actual == ClaseLexica.FLOAT.value:
            self.eat(ClaseLexica.FLOAT.value)
        else:
            self.error("Se espera 'int' o 'float'")

    def lista_var(self):
        """lista_var → identificador lista_var'"""
        self.eat(ClaseLexica.ID.value)
        self.lista_var_p()

    def lista_var_p(self):
        """lista_var' → , identificador lista_var' | ε"""
        if self.token_actual == ClaseLexica.COMA.value:
            self.eat(ClaseLexica.COMA.value)
            self.eat(ClaseLexica.ID.value)
            self.lista_var_p()

    def sentencias(self):
        """sentencias → sentencia sentencias'"""
        self.sentencia()
        self.sentencias_p()

    def sentencias_p(self):
        """sentencias' → sentencia sentencias' | ε"""
        if self.token_actual in [ClaseLexica.ID.value,ClaseLexica.IF.value,ClaseLexica.WHILE.value]:
            self.sentencia()
            self.sentencias_p()

    def sentencia(self):
        """sentencia → sentencia_matched | sentencia_unmatched"""
        if self.token_actual == ClaseLexica.ID.value:
            # sentencia_matched: asignación
            self.eat(ClaseLexica.ID.value)
            self.eat(ClaseLexica.IG.value)
            self.expresion()
            self.eat(ClaseLexica.PYC.value)
        elif self.token_actual == ClaseLexica.IF.value:
            self.eat(ClaseLexica.IF.value)
            self.eat(ClaseLexica.PARIZQ.value)
            self.expresion()
            self.eat(ClaseLexica.PARDER.value)
            self.sentencia()
            self.eat(ClaseLexica.ELSE.value)
            self.sentencia()
        elif self.token_actual == ClaseLexica.WHILE.value:
            self.eat(ClaseLexica.WHILE.value)
            self.eat(ClaseLexica.PARIZQ.value)
            self.expresion()
            self.eat(ClaseLexica.PARDER.value)
            self.sentencia()
        else:
            self.error("Sentencia no válida")

    def expresion(self):
        """expresion → expresion_suma"""
        self.expresion_suma()

    def expresion_suma(self):
        """expresion_suma → expresion_suma + expresion_mult
                          | expresion_suma - expresion_mult
                          | expresion_mult"""
        self.expresion_mult()
        while self.token_actual in [ClaseLexica.SUMA.value, ClaseLexica.RESTA.value]:
            self.eat(self.token_actual)
            self.expresion_mult()

    def expresion_mult(self):
        """expresion_mult → expresion_mult * expresion_base
                          | expresion_mult / expresion_base
                          | expresion_base"""
        self.expresion_base()
        while self.token_actual in [ClaseLexica.MULT.value, ClaseLexica.DIV.value]:
            self.eat(self.token_actual)
            self.expresion_base()

    def expresion_base(self):
        """expresion_base → identificador | numero | ( expresion )"""
        if self.token_actual == ClaseLexica.ID.value:
            self.eat(ClaseLexica.ID.value)
        elif self.token_actual == ClaseLexica.NUM.value:
            self.eat(ClaseLexica.NUM.value)
        elif self.token_actual == ClaseLexica.PARIZQ.value:
            self.eat(ClaseLexica.PARIZQ.value)
            self.expresion()
            self.eat(ClaseLexica.PARDER.value)
        else:
            self.error("Se esperaba un identificador, número o paréntesis")
