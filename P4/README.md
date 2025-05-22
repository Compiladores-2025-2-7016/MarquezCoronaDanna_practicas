<p  align="center">
  <img  width="200"  src="https://www.fciencias.unam.mx/sites/default/files/logoFC_2.png"  alt="">  <br>Compiladores  2025-2 <br>
  Práctica 4: Analizadores sintácticos de descenso predictivo LL(1) <br> Profesora: Ariel Adara Mercado Martínez
</p>

## Analizador sintáctico de descenso recursivo
### Objetivo:
Que el alumno se familiarice con el análisis sintáctico de descenso predictivo y construya un Analizador de este tipo reforzando sus conocimientos mediante el uso de _PLY/Python_. 

### Introducción
Existen dos tipos principales de análisis sintáctico descendente:
- Recursivo: Utiliza recursión en las funciones para ir desglosando las producciones de la gramática de manera directa.
- LL(k): Un tipo de análisis más generalizado que se basa en una técnica de análisis de k símbolos de entrada por adelantado para tomar decisiones de análisis.

El análisis sintáctico de descenso recursivo es una técnica de _parsing_ basada en una colección de funciones recursivas, donde cada función representa una regla gramatical. Este método puede manejar una amplia variedad de gramáticas, incluidas algunas que no son adecuadas para análisis predictivo, pero puede requerir _backtracking_ (retroceso) cuando hay ambigüedad o múltiples opciones posibles. En cambio, el análisis sintáctico LL(k), también conocido como descenso predictivo, es una forma más restringida y eficiente del descenso recursivo que no utiliza retroceso. Se basa en una tabla de predicción y en una gramática que debe ser libre de ambigüedades y factoreada a la izquierda, lo que permite decidir qué producción aplicar mirando solo los siguientes K símbolos de entrada. Por lo tanto, LL(k) es más rápido y determinista, pero menos flexible que el descenso recursivo general.

Es importante considerar lo siguiente para el análisis sintáctico predictivo:

- Es necesario determinar la producción que debe ser aplicada en cada paso para encontrar la
derivación requerida para obtener la cadena de entrada.
- El análisis sintáctico predictivo es un caso particular del análisis de descenso recursivo, para el
que el proceso de backtracking, no es requerido.
- El análisis sintáctico predictivo escoge la producción necesaria para hallar la derivación,
empleando los siguientes símbolos en la cadena de entrada, usualmente uno, p.ej. LL(1).


### Estructura del directorio
```c++
p4
├── README.md
├── src
│   └── main
│       ├── __init__.py
│       ├── analisis
│       │   ├── __init__.py
│       │   ├── lexico.py // contiene la definición del An. Léxico con PLY
│       │   └── sintactico.py // contiene la definición del An. Sintáctico LL(1)
│       ├── componente
│       │   ├── __init__.py
│       │   ├── clase_lexica.py // contiene la enumeración de las clases léxicas, que servirán como T y los no_terminales que servirán como N.
│       │   ├── componente_lexico.py // contiene la definición de un token 
│       │   └── gramatica
│       │       ├── __init__.py
│       │       ├── gramatica.py // contiene la definición de una gramática compuesta de dos listas de Símbolos y otra de Producciones
│       │       ├── produccion.py // contiene la definición de un objeto Produccion
│       │       └── simbolo.py // contiene la definición de un objeto Simbolo 
│       └── main.py // Script o clase principal que se ejecutará para manejar la entrada del usuario del lenguaje, 
└── tst
    └── prueba.txt // archivo ejemplo de código fuente en nuestro lenguaje de programación de a mentis.
```

### Uso

#### Ejecución

```bash
$ cd src/
$ python main/main.py
```

#### Ejercicios
Para la gramática G = ( N, Σ, P, S), descrita por las siguientes producciones: 
> P = {
>> S → num S' <br>
>> S' → + num S' | ε <br>
}


1. Determinar en un archivo Readme, en formato Markdown (.md) o LaTeX (.tex) - con su respectivo PDF, para este último - , los conjuntos _N_, _Σ_ y el símbolo inicial _S_.  (0.5 pts.) <br>
2. Mostrar en el archivo la construcción de la tabla de análisis sintáctico predictivo para _G_. (1 pt.)
3. Modificar el main.py para que nuestro programa sea capaz de recibir archivos y no sólo cadenas. (2 pts.)
4. Agregar las reglas necesarias para que el Analizador Léxico (lexico.py) reconozca los terminales de _G_. (0.5 pts.)
5. Definir _Σ_ en el _**enum**_ de _ClaseLexica_ en _clase_lexica.py_. (0.10 pts.)
6. Definir _N_ en un _**enum**_ de _NoTerminales_ en _clase_lexica.py_. (0.10 pts.)
7. Cargar _N ∪ Σ_ en _sintactico.py_. (0.25 pts.) 
8. Cargar _P_ en _sintactico.py_. (0.25 pts.)
9. Cargar la tabla de análisis sintáctico predictivo en _sintactico.py_. (0.25 pts.)
10. Implementar el algoritmo de análisis sintáctico de descenso predictivo en _sintactico.py_ de modo que el programa acepte el archivo _tst/prueba.txt_ e imprima las producciones necesarias para llegar de S a w; S el símbolo inicial, w la cadena de entrada. (4 pts.)
11. Sobrescribir la función *\_\_str\_\_* de Producción para hacer más legible la impresión de las producciones necesaria para la derivación de S →* w. (1.05 pts.) 
---
#### Extras

12. Generalizar la generación del analizador LL(1) al obtener una gramática (N,T,P,S). Podemos suponer que es LL(1). (4 pts)
13. Documentar el código. (0.25 pts)
14. Proponer 4 archivos de prueba nuevos, 2 válidos y 2 inválidos. (0.25 pts)
15. Modificar la búsqueda de símbolos (_get_sim_) en la clase _Gramatica_ para hacerla más eficiente en tiempo. Es válido cambiar la implementación de la clase o de la práctica en general para lograrlo. (2 pts)
