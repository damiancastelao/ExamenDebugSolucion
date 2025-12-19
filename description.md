## Descripción del Código en el Directorio
### main.py
Este archivo contiene dos funciones:
- `calcular_siguiente(serie)`: Calcula el siguiente número en una serie sumando los dos últimos elementos.
- `funcion_bucle(n)`: Genera una serie de tipo Fibonacci con 'n' elementos, utilizando `calcular_siguiente`.

El script principal llama a `funcion_bucle(1000)` e imprime la serie resultante.
### recorrerTablero.py
Este script simula el recorrido de un tablero de 8x8 representado por una matriz llamada `t`.
El script realiza las siguientes acciones:
1. Inicializa un tablero con piezas blanco, negro y casillas vacía.
2. Recorre cada casilla del tablero utilizando bucles `while` anidados.
3. Cuenta el número de piezas blanco y negro en el tablero.
4. Imprime la posición de las piezas ocupadas.
5. Al finalizar el recorrido, determina y anuncia qué color de ficha tiene más piezas, o si hay un empate.
