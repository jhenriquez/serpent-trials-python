# Trial 3 - Funciones

## 1. Objetivo

Separar partes del codigo en funciones para que el tablero sea mas facil de leer y reutilizar.

## 2. Explicacion del concepto

Una funcion es un bloque de codigo con nombre que puedes ejecutar cuando lo necesitas.

En vez de dejar todo dentro de `main()`, puedes crear funciones como:

- `draw_board()`
- `draw_snake()`

Eso hace que el codigo se vea mas ordenado.

Tambien te ayuda a pensar en partes pequenas del problema, en lugar de intentar resolver todo a la vez.

## 3. Conexion con Snake

Snake va a crecer en complejidad muy pronto.

Si todo el dibujo del tablero queda mezclado en un solo bloque grande, cada cambio sera mas confuso.

En este trial vas a empezar a organizar tu codigo como un juego que puede seguir creciendo.

## 4. Requisito concreto

Abre `projects/snake-terminal/main.py` y toma tu version del trial anterior.

Luego:

1. Crea una funcion para dibujar el tablero.
2. Crea una funcion para preparar o mostrar la posicion de la serpiente.
3. Deja `main()` mas pequeno, usando esas funciones.

No necesitas cambiar el resultado visual.

La meta es que el programa siga mostrando el mismo tablero con la `O`, pero con el codigo mas organizado.

Ejecuta:

```bash
python projects/snake-terminal/main.py
```

## 5. Resultado visible esperado

Debes ver exactamente el mismo tablero que en el trial anterior, o uno muy parecido.

Lo importante en este trial no es cambiar la imagen, sino mejorar la estructura interna del codigo.

Por ejemplo:

```text
+----------+
|          |
|          |
|    O     |
|          |
+----------+
```

## 6. Desafio opcional

Crea una funcion pequena extra para imprimir una sola fila vacia del tablero.
