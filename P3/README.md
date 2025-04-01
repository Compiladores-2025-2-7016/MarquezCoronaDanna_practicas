<p  align="center">
  <img  width="200"  src="https://www.fciencias.unam.mx/sites/default/files/logoFC_2.png"  alt="">  <br>Compiladores  2025-2 <br>
  Práctica 2: Analizadores léxicos con Lex (PLY) <br> Profesora: Ariel Adara Mercado Martínez
</p>

## Analizador sintáctico de descenso recursivo
### Objetivo:
Que el alumno se familiarice con el análisis sintáctico de descenso recursivo y construya un Analizador de este tipo reforzando sus conocimientos mediante el uso de _PLY/Python_. 

### Introducción
El análisis sintáctico es una de las fases fundamentales en la construcción de un compilador, siendo la segunda fase del proceso de compilación. Su principal objetivo es verificar que la secuencia de _tokens_ generada por el analizador léxico cumpla con las reglas gramaticales de un lenguaje de programación, es decir, que el flujo de tokens pueda ser estructurado de acuerdo con una gramática previamente definida. A través de esta fase, se construye una representación jerárquica del programa fuente, que típicamente se presenta en forma de un árbol de sintaxis.

El análisis sintáctico descendente es una técnica en la que se construye el árbol de sintaxis de arriba hacia abajo, comenzando desde la raíz (el símbolo de inicio) hasta las hojas (los lexemas de entrada). Esto es equivalente a encontrar una serie de derivaciones desde el símbolo inicial _S_ que nos permita generar una cadena _w_ que recibimos como entrada para analizar sintácticamente. 

Existen dos tipos principales de análisis sintáctico descendente:
- Recursivo: Utiliza recursión en las funciones para ir desglosando las producciones de la gramática de manera directa.
- LL(k): Un tipo de análisis más generalizado que se basa en una técnica de análisis de k símbolos de entrada por adelantado para tomar decisiones de análisis.


### Estructura del directorio
```c++
P3
├── README.md
└── src
    └── main
        ├── __init__.py
        ├── analisis
        │   ├── __init__.py
        │   ├── lexico.py // Clase Lexer para la impl. del An. Léxico
        │   └── sintactico.py // Clase Parser para la impl. del An. Sintáctico
        ├── componente
        │   ├── __init__.py
        │   ├── clase_lexica.py // Enum que contiene todas las clases léxicas del lenguaje a reconocer
        │   └── componente_lexico.py // Estructura de datos que conforma un token. Una clase léxica y su lexema asociado.
        └── main.py // script con el método main
```

### Uso

#### Compilacion

```bash
$ jflex src/main/jflex/Lexer.flex
$ javac --source-path src -d build src/main/jflex/Main.java
```

#### Ejecucion

```bash
$ java -cp build main.java.Main tst/prueba.txt  
```

#### Ejercicios
Para la gramática G = ( N, Σ, P, S), descrita por las siguientes producciones: 
> P = {
>> programa → declaraciones sentencias <br>
>> declaraciones → declaraciones declaracion | declaracion <br>
>> declaracion → tipo lista-var **;** <br>
>> tipo → **int** | **float** <br>
>> lista_var → lista_var **,** _**identificador**_ | _**identificador**_ <br>
>> sentencias → sentencias sentencia | sentencia <br>
>> sentencia → _**identificador**_ **=** expresion **;** | **if** **(** expresion **)** sentencias **else** sentencias | **while** **(** expresión **)** sentencias <br>
>> expresion → expresion **+** expresion | expresion **-** expresion | expresion __\*__ expresion | expresion **/** expresión | _**identificador**_ | **_numero_** <br>
>> expresion → **(** expresion **)** <br>
}


1. Determinar en un archivo Readme, en formato Markdown (.md) o LaTeX (.tex) -- con su respectivo PDF, para este último -- , los conjuntos _N_, _Σ_ y el símbolo inicial _S_.  (0.5 pts.)
2. Mostrar en el archivo el proceso de eliminación de ambigüedad o justificar, en caso de no ser necesario. (1 pts.).
3. Mostrar en el archivo el proceso de eliminación de la recursividad izquierda o justificar, en caso de no ser necesario. (1 pts.)
4. Mostrar en el archivo el proceso de factorización izquierda o justificar, en caso de no ser necesario. (1 pts.)
5. Mostrar en el archivo los nuevos conjuntos _N_ y _P_. (0.5 pts.)
6. Modificar el main.py para que nuestro programa sea capaz de recibir archivos y no sólo cadenas. (2 pts.)
7. Implementar el Analizador Sintáctico (_analisis/sintactico.py_) de descenso recursivo, documentando las funciones de cada No-Terminal, de forma que el programa descrito en el archivo _tst/prueba.txt_ sea reconocido y aceptado por el analizador resultante. (4 pts.)

---
#### Extras

9. Documentar TODO el código. (0.25pts)
10. Proponer 4 archivos de prueba nuevos, 2 válidos y 2 inválidos. (0.25pts)