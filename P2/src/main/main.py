from lexer.scanner import Lexer
import sys

'''
lexer = Lexer()
lexer.build()
lexer.scan("3 y 4")
'''


input=''

if len(sys.argv) > 1:
    file = sys.argv[1]
    with open(file,'r') as reader:
        input = reader.read().strip()
else:
    input="3 y 4"

lexer = Lexer()
lexer.build()
lexer.scan(input)