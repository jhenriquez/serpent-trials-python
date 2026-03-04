# Trial 2 - El tablero como sistema de coordenadas

## 🎯 Objetivo

Entender que la pantalla es una grilla de posiciones.

Hoy dejamos de ver el tablero como “texto”.
Empezamos a verlo como un sistema de coordenadas.

La serpiente ahora existira en una posicion numerica real.

---

## 🧠 Antes de listas: la pantalla es una grilla

Mira el tablero que dibujaste en el trial anterior.

Aunque lo imprimimos como texto, en realidad es una grilla.

Cada espacio dentro del borde es una celda.

Podemos imaginarlo asi:

- Hay filas (vertical)
- Hay columnas (horizontal)

Si numeramos las columnas:

```
0 1 2 3 4 5 6 7 8 9
```



Y numeramos las filas:

```
0
1
2
3
```

Entonces cada posicion del tablero se puede describir con dos numeros:

[columna, fila]

Por ejemplo:

[4, 2]

Significa:

- columna 4
- fila 2

```
0 1 2 3 4 5 6 7 8 9
1     X
2
3
4
```

Eso es una coordenada.

La pantalla no es solo texto.
Es una matriz de posiciones.

Y ahora vamos a empezar a pensar como el juego piensa.

### Nota importante: ¿Por que empezamos en 0?

En programacion es muy comun que las posiciones empiecen en 0.

Eso se llama indexacion basada en cero (zero-based indexing).

Si algo tiene 4 posiciones, sus indices son:

```
0
1
2
3
```

No 1, 2, 3, 4.

¿Por que?

Porque el indice representa desplazamiento desde el inicio.

0 significa:
"No me he movido desde el inicio."

1 significa:
"Me movi una posicion."

En nuestro tablero pasa lo mismo.

Si el ancho es 10, las columnas van de:

0 a 9

Si la altura es 4, las filas van de:

0 a 3

Esto no es algo raro de Snake.
Es algo muy comun en casi todos los lenguajes de programacion.

Al principio puede sentirse extraño.

Despues se vuelve completamente natural.

---

## 🧠 Nuevo concepto 1: Listas

En Python, una lista permite guardar varios valores en orden.

Ejemplo:

```
snake_head = [4, 2]
```

Esa lista representa una coordenada.

El primer numero es la columna.
El segundo numero es la fila.

Ahora la posicion de la serpiente no esta dibujada.
Esta almacenada como datos.

Eso es un cambio enorme.

---

## 🧠 Nuevo concepto 2: Bucles for

Si el tablero es una grilla…

Entonces necesitamos recorrer:

- Cada fila
- Cada columna dentro de cada fila

Para eso usamos un bucle for.

Un bucle for repite algo varias veces.

Ejemplo simple:

```python
for i in range(3):
    print(i)
```

```
🧠 Nota rapida: ¿Que es range?

Ya conocemos `print()`.

Sabemos que sirve para escribir cosas en la pantalla.

Ahora estamos usando algo nuevo: `range()`.

Por ahora solo necesitas saber esto:

range(n) produce una secuencia de numeros que empieza en 0 y termina en n - 1.

Ejemplo:

range(4)

Produce los numeros:

0, 1, 2, 3

Eso es perfecto para nosotros porque si el tablero tiene 4 filas,
sus posiciones tambien van de 0 a 3.

No te preocupes por como funciona `range()` internamente.
Mas adelante aprenderemos mas sobre funciones.

Por ahora solo piensa:

range(n) → numeros desde 0 hasta n - 1.
```

En nuestro caso vamos a usar:

- Un bucle para las filas
- Otro bucle para las columnas

Eso nos permitira construir el tablero celda por celda.

---

## 🐍 Conexion con Snake

En el trial anterior, la O estaba escrita directamente en el dibujo.

Ahora vamos a cambiar la regla:

Si la posicion actual coincide con snake_head → imprimir "O"
Si no → imprimir espacio

Eso significa que el dibujo depende de los datos.

El juego empieza a tener estado.

---

## 🛠️ Requisito

Abre:

projects/snake-terminal/main.py

Ahora modifica tu codigo para que:

1. Definas:
   grid_width
   grid_height

2. Crees:
   snake_head = [4, 2]

3. Dibujes el tablero usando:
   - Un bucle for para recorrer las filas
   - Un bucle for dentro para recorrer las columnas

4. Dentro del bucle interno:
   - Si col y row coinciden con snake_head → imprimir "O"
   - Si no → imprimir espacio

5. Mantengas los bordes del tablero.

No uses funciones todavia.
No agregues movimiento.
Solo genera el tablero dinamicamente.

Ejecuta:

python projects/snake-terminal/main.py

---

## ✅ Resultado esperado

Debe verse algo como:

```
+----------+
|          |
|          |
|    O     |
|          |
+----------+
```

Pero ahora la O aparece porque el programa compara coordenadas.

Si cambias:

```
snake_head = [1, 1]
```


La O debe moverse.

Eso significa que el tablero ya no es texto fijo.
Es una representacion de datos.

---

## 🚀 Desafio opcional

Prueba coordenadas diferentes.

Pregunta interesante:

¿Que pasa si usas numeros mayores que el tamaño del tablero?

No lo soluciones todavia.
Solo observa.

---

## 🔥 Super Desafío – El t  ablero del tamaño real de tu terminal

Hasta ahora el tablero tiene un tamaño fijo.

Pero… ¿y si el juego pudiera detectar automaticamente el tamaño de tu terminal?

Es decir:

Que el ancho del tablero sea igual al ancho real de tu ventana.
Que la altura del tablero se adapte tambien.

Python puede obtener esa informacion del sistema.

Existe una funcion que permite saber:

- Cuantas columnas tiene tu terminal
- Cuantas lineas tiene disponibles

Tu desafio es investigar como obtener:

- El ancho (columns)
- La altura (lines)

Y usarlos para definir:

grid_width
grid_height

Pista 1:
Busca algo como “python get terminal size”.

Pista 2:
Existe una funcion llamada get_terminal_size.

⚠️ Consejo importante:

Probablemente no quieras usar todo el alto disponible.
Puedes restar algunos espacios para que el tablero no se pegue al borde inferior.

Ejemplo mental:

Si el terminal tiene 40 lineas,
quizas uses 36 para el tablero.

No es obligatorio que lo logres.
Pero si lo haces…

Tu juego ya no sera fijo.

Sera adaptable.

Eso es nivel programador.

---

## Navegacion

[Anterior: Trial 1](../trial-01-variables/README.md)
[Siguiente: Trial 3](../trial-03-manual-movement/README.md)