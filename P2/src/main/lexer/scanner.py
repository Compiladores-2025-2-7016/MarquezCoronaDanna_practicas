import ply.lex as lex
from ply.lex import TOKEN
from componente.clase_lexica import ClaseLexica
from componente.componente_lexico import ComponenteLexico

# FIXME: agreguemos definiciones de regexp o funciones para reconocer el resto de palabras en el lenguaje.
class Lexer(object):
    # Definiciones de expresiones regulares auxiliares
    numero = r'[0-9]+(\.[0-9]+(e[0-9]+)?)?'
    int_re= r'\bint\b'
    float_re= r'\bfloat\b'
    if_re = r'\bif\b'
    else_re= r'\belse\b'
    while_re= r'\bwhile\b'
    pyc_re= r';'
    coma = r','
    id_re= r'[a-zA-Z0-9_]+'


    # Lista de tokens. Siempre REQUERIDO
    tokens = list(ClaseLexica._member_names_) 


    # Definición de reglas en una sóla línea sin acción léxicas
    t_ESPACIO = r'\ +'

    # Definición de reglas con acción léxica
    #@TOKEN(() parentesis izq
    @TOKEN(r'\(')
    def t_LPAR(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t


    #@TOKEN(() parentesis der
    @TOKEN(r'\)')
    def t_RPAR(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t


    #@TOKEN(int)
    @TOKEN(int_re)
    def t_INT(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t


    #@TOKEN(float)
    @TOKEN(float_re)
    def t_FLOAT(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t


    #@TOKEN(if)
    @TOKEN(if_re)
    def t_IF(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
   
   #@TOKEN(else)
    @TOKEN(else_re)
    def t_ELSE(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t


    #@TOKEN(while)
    @TOKEN(while_re)
    def t_WHILE(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t


    #@TOKEN(pyc)
    @TOKEN(pyc_re)
    def t_PYC(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t


    #@TOKEN(coma)
    @TOKEN(coma)
    def t_COMA(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t


    #@TOKEN(numero)
    @TOKEN(numero)
    def t_NUMERO(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t

    #@TOKEN(id)
    @TOKEN(id_re)
    def t_ID(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t

    # Definimos una regla para el manejo de número de líneas
    def t_newline(self, t):
        r'\n+' # docstring contiene la regex que maneja el salto de línea
        t.lexer.lineno += len(t.value) # Aumentamos la variable de número de línea del Analizador


    # Una cadena que contiene todos los caracteres que deben ignorarse
    # ej. Espacios y tabuladores
    t_ignore  = " \t"

    # Esta función nos permite manejar el estado de error a nuestra conveniencia
    def t_error(self, t):
        print("Error léxico. Caracter no reconocido: '%s'" % t.value[0])
        t.lexer.skip(1)



    # Función que nos permite construir el analizador léxico
    # NO TOCAR
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)


    # Función que nos permite efectuar un análisis léxico
    # sobre una entrada
    def scan(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: 
               break
            #print(tok) # FIXME: imprimamos desde la función que reconoce el patrón