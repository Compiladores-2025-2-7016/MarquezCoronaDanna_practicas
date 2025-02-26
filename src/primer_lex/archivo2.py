import sys
import ply.lex as lex
from ply.lex import TOKEN

# Definiciones de expresiones regulares auxiliares
digito = r'[0-9]'
letra = r'[a-zA-Z]'
hexadecimal = r'0[xX][0-9a-fA-F]+'  # Para los hexadecimales en lenguaje C
identificador_java = r'[a-zA-Z_][a-zA-Z0-9_]{1,32}'  # Identificadores válidos en Java (máximo 32 caracteres)
espacios_blanco = r'[ \t]+'  # Para los espacios en blanco

# Lista de tokens. Siempre REQUERIDO
tokens = (
    "PALABRA",
    "NUMERO",
    "HEX", #Expresión para hexa en C
    "PALABRA_RESERVADA", #Palabras reservadas de C
    "IDENTIFICADOR", #Identificadores con log de 32
    "ESPACIO", #Espacios en blanco
    "PARIZQ",
    "PARDER",
)

# Definición de reglas en una sóla línea sin acción léxica
t_PALABRA = r'[a-zA-Z]+'
t_PARIZQ = r'\('
t_PARDER = r'\)'

# Definición de reglas con acción léxica
@TOKEN(r'(' + digito + r')+')
def t_NUMERO(t):
    print("Encontré un número:", t.value)
    return t

@TOKEN(hexadecimal)
def t_HEX(t):
    print("Encontré un número hexadecimal:", t.value)
    return t

@TOKEN(r'(def|class|import|if|else)\b')  # 5 palabras reservadas de Python
def t_PALABRA_RESERVADA(t):
    print("Encontré una palabra reservada de Python:", t.value)
    return t

@TOKEN(identificador_java)
def t_IDENTIFICADOR(t):
    print("Encontré un identificador Java:", t.value)
    return t

@TOKEN(espacios_blanco)
def t_ESPACIO(t):
    print("Encontré un espacio en blanco")
    return t

# Definimos una regla para el manejo de número de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Una cadena que contiene todos los caracteres que deben ignorarse
t_ignore = ""

# Esta función nos permite manejar el estado de error a nuestra conveniencia
def t_error(t):
    print("Error léxico. Caracter no reconocido: '%s'" % t.value[0])
    t.lexer.skip(1)

###### Instanciación y uso del Analizador Léxico ######

# Construcción del Scanner
lexer = lex.lex()

# Código fuente
data = '''
def holaMundo():
    x = 0xFF
    if x > 10:
        print("Hola")
'''

# En caso de que estemos leyendo un archivo señalado desde la línea de argumentos
if (len(sys.argv) > 1):
    with open(sys.argv[1], 'r') as file:
        data = file.read()

lexer.input(data)

# Tokenización
while True:
    tok = lexer.token()
    if not tok:
        break      # Termina el análisis
    print(tok)
