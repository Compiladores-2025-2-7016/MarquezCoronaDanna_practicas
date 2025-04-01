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
        self.eat(2) # FIXME: Borrar este paso de empate y programar los siguientes pasos de prueba
        #declaraciones()
        #sentencias()
        

    ########################################################################
    ##                                                                    ##
    ##                    TODO: Funciones por cada NT                     ##
    ##                                                                    ##
    ########################################################################