from componente.clase_lexica import ClaseLexica

class ComponenteLexico(): # también llamado token
    clase: ClaseLexica
    lexema: str

    def __init__(self, clase, lexema):
        self.clase = clase
        self.lexema = lexema


    def __str__(self):
         return '<{}, {}>'.format(self.clase,self.lexema)