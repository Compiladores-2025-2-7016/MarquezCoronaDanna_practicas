import sys
from analisis.sintactico import Parser
from analisis.lexico import Lexer

data =''
if len(sys.argv) > 1:
    reader = open(sys.argv[1], 'r')
    data = reader.read()
else:
    data = """42"""

scanner = Lexer()
scanner.build()
#scanner.scan("3 y 4")
scanner.lexer.input(data)

parser = Parser(scanner)
parser.parse()
