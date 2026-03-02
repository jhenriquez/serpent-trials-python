# Trial 5 - Movimiento continuo

## 1. Objetivo

Hacer que la serpiente siga moviendose sola usando un bucle y la ultima direccion elegida.

## 2. Explicacion del concepto

Un bucle `while` permite repetir acciones varias veces.

En Snake, eso sirve para que el juego:

1. Dibuje el tablero
2. Revise la direccion
3. Mueva la serpiente
4. Repita

Tambien necesitas guardar la ultima direccion para que la serpiente siga avanzando aunque el jugador no cambie nada en ese momento.

## 3. Conexion con Snake

En el trial anterior la serpiente se movia un solo paso.

Ahora vas a darle una sensacion mucho mas real: movimiento continuo.

Este es el momento en que el proyecto empieza a sentirse como un juego de verdad.

## 4. Requisito concreto

Abre `projects/snake-terminal/main.py` y toma tu version del trial anterior.

Luego:

1. Crea un bucle `while` para repetir el juego.
2. Guarda una variable como `direction` con la ultima direccion usada.
3. En cada vuelta del bucle, mueve la cabeza una casilla en esa direccion.
4. Limpia la terminal y vuelve a dibujar el tablero.
5. Permite cambiar la direccion con `W`, `A`, `S`, `D`.

Todavia no necesitas comida ni colisiones.

La meta es que la serpiente siga avanzando automaticamente.

Ejecuta:

```bash
python projects/snake-terminal/main.py
```

## 5. Resultado visible esperado

Debes ver que la `O` cambia de posicion varias veces sin tener que volver a lanzar el programa.

Si mantienes la direccion hacia la derecha, la cabeza debe avanzar una columna por ciclo.

## 6. Desafio opcional

Si quieres una experiencia mas fluida, explora una version con lectura de teclado sin Enter usando:

- `msvcrt.getch()` en Windows
- `termios` y `tty` en Linux o Mac

Esto es opcional y depende de tu sistema operativo.

## Navegacion

[Anterior: Trial 4](../trial-04-manual-movement/)
[Siguiente: Trial 6](../trial-06-food-system/)
