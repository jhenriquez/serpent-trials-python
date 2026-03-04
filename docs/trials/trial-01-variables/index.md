# Trial 1 - Variables e impresion

## 🎯 Objetivo

Aprender qué es una variable en Python y usarla para dibujar la primera versión visual del tablero de Snake en la terminal.

Hoy no solo dibujas algo.

Hoy entiendes cómo el programa recuerda información.

---

## 🧠 ¿Qué es una variable?

Una variable es un nombre que guarda un valor.

Piensa en una variable como una caja con etiqueta.

Si escribes:

```
grid_width = 10
```

Significa:
- Existe una caja llamada `grid_width`
- Dentro de esa caja está el número 10

Luego puedes usar ese nombre en tu código en vez de repetir el número.

Eso hace tu código:
- Más claro
- Más fácil de cambiar
- Más poderoso

---

## 🧩 Sintaxis básica en Python

En Python, crear una variable es muy simple:

nombre = valor

Ejemplos:

```python
age = 13
player_name = "Ana"
score = 0
```

No necesitas decirle a Python qué `tipo` es.
Python lo detecta automáticamente.

```
Tipo: es la categoría del valor que guarda una variable.
Por ejemplo:
- 10 es un número entero (int)
- 3.14 es un número decimal (float)
- "Hola" es texto (str)
- True es un valor lógico (bool)

En muchos lenguajes debes declarar el tipo antes.
En Python no. Python lo detecta automáticamente según el valor.
```
---
## ➕ Operadores básicos en Python

Un operador es un símbolo que le dice a Python que haga algo con valores.

Ya usaste uno sin darte cuenta:

=  → asignación
Sirve para guardar un valor en una variable.

Ejemplo:

score = 0

Esto no significa “igual que”.
Significa “guardar 0 dentro de score”.

---

### Operador +

El símbolo + sirve para sumar números:

3 + 2  →  5

Pero también puede unir texto (esto se llama concatenar):

"Hola" + " Mundo"

Resultado:
Hola Mundo

---

### Operador *

El símbolo * sirve para multiplicar números:

4 * 3  →  12

Pero cuando lo usas con texto y un número,
repite el texto varias veces:

"-" * 5

Resultado:
-----

Esto es exactamente lo que usaremos para dibujar el borde del tablero.

---

## 🧪 Mini Experimento (Muy Importante)

Antes de dibujar el tablero completo, vamos a entender algo clave
que necesitarás para Snake: el estado del juego.

En tu archivo `projects/snake-terminal/main.py`,
debajo de tu mensaje actual, agrega esto:

```python
player_name = "Jugador 1"
score = 0

print("Bienvenido,", player_name)
print("Tu puntaje actual es:", score)
```

Ejecuta el archivo.

Ahora cambia el nombre.
Cambia el puntaje a 5.
Ejecuta otra vez.

¿Qué pasó?

El programa muestra exactamente el valor que escribiste en el código.

Ahora intenta esto:

```
player_name = "Jugador 1"
score = 0
score = score + 1

print("Bienvenido,", player_name)
print("Tu puntaje actual es:", score)
```

Ejecuta.

Verás que imprime 1.

Pero si lo ejecutas otra vez…
seguirá imprimiendo 1.

¿Por qué?

Porque cada vez que ejecutas el archivo,
Python empieza desde la primera línea y ejecuta todo otra vez.

No guarda lo que pasó antes.
No tiene memoria entre ejecuciones.

Eso significa:

👉 Si quieres que Snake tenga puntaje,

👉 si quieres que la serpiente crezca,

👉 si quieres que el juego avance,

tendremos que construir un sistema que mantenga el estado mientras el programa está corriendo.

Por ahora, solo recuerda esto:

Las variables guardan información.
Pero solo mientras el programa está activo.
Cuando termina, todo desaparece.

---

## 🔁 Reasignar Variables

Las variables pueden cambiar.

Ejemplo:

```
score = 0
score = score + 1
```

⚠️ Nota importante

```
score = score + 1
```

Esto parece extraño.
¿Cómo puede score ser igual a score + 1?

Recuerda:
Python primero calcula lo que está a la derecha.
Luego guarda el resultado en la variable.

Es como decir:
“toma el valor actual (0), súmale 1, y reemplázalo”.

---

## 🧱 Conexión con Snake

Snake necesita:

- Un ancho de tablero
- Un alto de tablero

En vez de escribir números directamente muchas veces,
vamos a guardarlos en variables.

Eso nos permitirá cambiar el tamaño del juego fácilmente después.

---

## 🛠️ Requisito del Trial

Ahora sí.

En `projects/snake-terminal/main.py` debes:

1. Crear una variable `grid_width`
2. Crear una variable `grid_height`
3. Usar esas variables para dibujar un tablero
4. Colocar una `O` dentro del tablero (la cabeza de la serpiente)

No escribas números directamente en múltiples lugares.
Usa las variables.

---

## 💡 Pista Técnica

Puedes crear el borde superior así:

"+" + "-" * grid_width + "+"

El operador `*` repite texto.

Ejemplo:

"-" * 5

produce:

-----

Experimenta con eso antes de construir todo el tablero.

---

## ✅ Resultado esperado

Algo parecido a:

```
+----------+
|          |
|    O     |
|          |
|          |
+----------+
```

No tiene que ser exactamente igual.
Pero debe sentirse como un tablero.

🧠 Nota importante

La forma en que estamos dibujando el tablero ahora es bastante simple.

Estamos construyendo líneas de texto manualmente.

Más adelante aprenderás una forma más elegante y poderosa de “pintar”
el tablero usando lógica y posiciones.

Por ahora, el objetivo no es perfección.
Es entender variables y ver algo en pantalla.

---

## 🚀 Desafío opcional

1. Cambia solo `grid_width` y ejecuta el programa.
2. Cambia solo `grid_height`.
3. Mueve la `O` usando variables como:

snake_x = 4
snake_y = 2

Todavía no necesitas lógica compleja.
Solo experimenta.

---

## 🧠 Reflexión

Si cambias el tamaño del tablero y todo se adapta,
entonces entendiste el poder de las variables.

Si tu tablero se rompe…
aún estás aprendiendo 😄

Eso también es parte del proceso.

---

## Navegación

[Anterior: Trial 0](../trial-00-setup/README.md)
[Siguiente: Trial 2](../trial-02-lists-coordinates/README.md)