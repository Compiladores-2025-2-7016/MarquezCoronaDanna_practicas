from analisis.sintactico import Parser
from analisis.lexico import Lexer

data = """42"""

scanner = Lexer()
scanner.build()
#scanner.scan("3 y 4")
scanner.lexer.input(data)

parser = Parser(scanner)
parser.parse()
