import ply.lex as lex
from ply.lex import TOKEN, LexToken
from componente.clase_lexica import ClaseLexica
from componente.componente_lexico import ComponenteLexico


# FIXME: agreguemos definiciones de regexp o funciones para reconocer el resto de palabras en el lenguaje.
class Lexer(object):
    # Lista de tokens. Siempre REQUERIDO
    tokens = list(ClaseLexica._member_names_) 
    
    # Definición de reglas en una sóla línea sin acción léxica
    t_ESPACIO = r'\ +'

    # Definición de reglas con acción léxica
    @TOKEN(r'\(')
    def t_PARIZQ(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\)')
    def t_PARDER(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\=')
    def t_IG(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\+')
    def t_SUMA(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\-')
    def t_RES(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\*')
    def t_MULT(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\/')
    def t_DIV(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\bint\b')
    def t_INT(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\bfloat\b')
    def t_FLOAT(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\bif\b')
    def t_IF(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    @TOKEN(r'\bwhile\b')
    def t_WHILE(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\b[0-9]+(\.[0-9]+(e[0-9]+)?)?\b')
    def t_NUM(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'[a-zA-Z0-9_]+')
    def t_ID(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\;')
    def t_PYC(self, t):
        print(ComponenteLexico(t.type, t.value))
        return t
    
    @TOKEN(r'\,')
    def t_COMA(self, t):
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