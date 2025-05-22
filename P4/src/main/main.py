import sys
from analisis.sintactico import ParserLL
from analisis.lexico import Lexer

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        data = f.read()
else:
    data = "42+2"  # entrada por defecto

scanner = Lexer()
scanner.build()
scanner.lexer.input(data)

parser = ParserLL(scanner)
parser.parse()
