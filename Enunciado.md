# Examen de Depuración en PyCharm

---

## **Instrucciones:**

1. Realiza un fork de este repositorio y clónalo.
1. Las respuestas a las preguntas realízalas en este Readme

### Apartado 1

- Coloca un punto de interrupción **normal** en la línea donde se inicializa la lista de la serie: `serie = [0, 1]`. 
- Inicia el modo *Debug*.

**Pregunta**

1. Si la función es llamada con `n=10`, ¿cuál es el valor de la variable `n` que se visualiza en la ventana de variables del debugger justo antes de que se ejecute la línea `serie = [0, 1]`?

---

### Apartado 2

-  Asegúrate de que la llamada a la función es `print(funcion_bucle(10))`.
-  Inicia el modo *Debug* y avanza hasta que la ejecución se detenga en la línea `siguiente_numero = calcular_siguiente(serie)`.
-  Utiliza la opción de depuración adecuada para **entrar dentro** de la función `calcular_siguiente`.

**Preguntas**

1. Justo cuando el debugger se detiene dentro de la función `calcular_siguiente` por **primera vez**, ¿cuál es el valor que tiene la variable local `aux` *después* de que se ejecute la línea `aux = serie[-1] + serie[-2]`?
**(Indica el valor numérico exacto de la variable `aux` en ese momento y el nombre de la herramienta de *debugging* que utilizaste para entrar en la función).**
2. Si estuvieras dentro de la función `calcular_siguiente` y quisieras salir rápidamente sin ejecutar el resto de las líneas, volviendo al punto de llamada en `funcion_bucle`, ¿qué función del debugger deberías usar?
3. ¿Qué diferencia fundamental existe entre usar *Step Over* y *Step Into* en la línea `siguiente_numero = calcular_siguiente(serie)`?

---

### Apartado 3

-  Cambia la llamada a la función para que el número de elementos sea mayor: `print(funcion_bucle(1000))`.
-  Establece un **Breakpoint Condicional** para que la ejecución se detenga solo cuando `siguiente_numero` sea **mayor que 20000**.

**Pregunta**

1. Cuando el *Breakpoint Condicional* se activa por **primera vez** (la primera vez que `siguiente_numero` es mayor que 20000), ¿qué longitud tiene `serie`?

---

### Apartado 4

-  Asegúrate de que el *Breakpoint Condicional* y los *Watches* están desactivados, dejando solo el punto de interrupción normal en `serie = [0, 1]`.
-  Inicia la depuración con el ejemplo de uso original: `print(funcion_bucle(10))`.
-  Avanza la ejecución hasta la línea `while len(serie) < n:`.
-  Utiliza la función de PyCharm para **modificar el valor** de la variable `n` (el tamaño deseado de la serie) en la ventana de Variables. Cámbiala de `10` a **`5`**.
-  Continúa la ejecución del programa con *Resume Program*.

**Preguntas**

1. Después de modificar el valor de `n` de 10 a 5 y continuar la ejecución con *Resume Program*, ¿cuál será el contenido final exacto de la lista `serie` que se imprime en la consola de salida?
**(Escribe la lista completa de números tal como la devuelve la función y el nombre de la herramienta que utilizaste para modificar la variable `n`).**

2. ¿Qué desventaja o riesgo principal supone la modificación de variables en tiempo de ejecución (`n` en este caso) cuando se está intentando depurar un fallo en la lógica de negocio del programa?

---