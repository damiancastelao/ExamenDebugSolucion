# Solución: Examen de Depuración en PyCharm

Apartado 1

Respuesta 1:
- 10

Apartado 2

Pregunta 2.1:
- Valor de `aux`: 1
- Herramienta usada para entrar en la función: Step Into

Pregunta 2.2:
- Herramienta para salir rápidamente a la llamada: Step Out (Step Return)

Pregunta 2.3
- Diferencia entre Step Over y Step Into en `siguiente_numero = calcular_siguiente(serie)`:
   - Step Over: ejecuta la llamada completa sin entrar en la función.
   - Step Into: entra dentro de la función y permite depurar sus líneas internas.

Apartado 3

Pregunta 3.1:
- Longitud de `serie` cuando el breakpoint condicional `siguiente_numero > 20000` se activa por primera vez: 23

Apartado 4

Pregunta 4.1:
- Contenido final de `serie`: [0, 1, 1, 2, 3]
- Herramienta usada para modificar `n`: Ventana Variables de PyCharm (Set Value / Edit Value)

Preguntas 4.2:
- Si se cambia `n` después de que el bucle `while` ya terminó, no tiene efecto en el resultado final (el bucle ya se ejecutó con el valor anterior).
- Riesgo principal de modificar variables en tiempo de ejecución: puede enmascarar errores reales, producir resultados no reproducibles y llevar a conclusiones equivocadas sobre la lógica del programa.
