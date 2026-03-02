# Trial 1 - Variables e impresion

## 1. Objetivo

Definir el tamano del tablero y mostrar la primera version visual de Snake en la terminal.

## 2. Explicacion del concepto

Una variable te permite guardar informacion con un nombre.

En vez de repetir numeros y textos directamente, puedes guardarlos en variables como `grid_width` o `grid_height`.

Eso hace que tu codigo sea mas facil de leer y mas facil de cambiar despues.

En este trial tambien usaras `print()` para mostrar texto en pantalla.

## 3. Conexion con Snake

Snake necesita un tablero visible antes de empezar a moverse.

Todavia no vamos a hacer que la serpiente avance, pero ya puedes dibujar una primera version estatica del area de juego.

Este es el primer paso para convertir el mensaje inicial en algo que se parece a un juego.

## 4. Requisito concreto

Abre `projects/snake-terminal/main.py` y reemplaza el mensaje de bienvenida por un tablero simple.

Tu archivo debe:

1. Guardar el ancho del tablero en una variable.
2. Guardar el alto del tablero en una variable.
3. Imprimir un borde superior e inferior.
4. Imprimir varias filas vacias.
5. Imprimir una `O` dentro del tablero para representar la cabeza de la serpiente.

Ejecuta:

```bash
python projects/snake-terminal/main.py
```

## 5. Resultado visible esperado

Debes ver un tablero simple en la terminal con una `O` dentro.

Algo parecido a esto:

```text
+----------+
|          |
|    O     |
|          |
|          |
+----------+
```

No tiene que verse exactamente igual, pero ya debe sentirse como el inicio de Snake.

## 6. Desafio opcional

Cambia el ancho del tablero o mueve la `O` a otra posicion usando solo variables.

## Navegacion

[Anterior: Trial 0](../trial-00-setup/)
[Siguiente: Trial 2](../trial-02-lists-coordinates/)
