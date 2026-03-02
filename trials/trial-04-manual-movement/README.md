# Trial 4 - Movimiento manual

## 1. Objetivo

Mover la serpiente un paso a la vez usando una direccion elegida por el jugador.

## 2. Explicacion del concepto

Ahora vas a combinar dos ideas importantes:

- `input()` para leer una accion del jugador
- `if` para decidir como cambiar la posicion de la serpiente

Cada vez que el jugador escriba una direccion, tu programa debe cambiar la coordenada de la cabeza.

Todavia no vamos a usar un bucle continuo.

Eso significa que el juego hara una sola pregunta, movera la serpiente una vez y volvera a dibujar el tablero.

## 3. Conexion con Snake

Este es el primer momento en que el jugador controla la serpiente.

Hasta ahora la cabeza estaba fija.

Con este cambio, la serpiente ya responde a una direccion y se siente mas cerca de un juego real.

## 4. Requisito concreto

Abre `projects/snake-terminal/main.py` y toma tu version del trial anterior.

Luego:

1. Pide una direccion al jugador.
2. Acepta `W`, `A`, `S`, `D` como controles.
3. Si tu terminal lo permite, acepta tambien las flechas como alternativa.
4. Usa `if` para cambiar la coordenada de la cabeza una sola vez.
5. Vuelve a dibujar el tablero con la nueva posicion.

Usa esta idea:

- `W` o flecha arriba: subir
- `A` o flecha izquierda: ir a la izquierda
- `S` o flecha abajo: bajar
- `D` o flecha derecha: ir a la derecha

Nota importante:

Con `input()` normal, algunas terminales no entregan las flechas de forma simple. Si en tu terminal las flechas no funcionan, `W/A/S/D` sigue siendo la ruta principal y suficiente para completar el trial.

Ejecuta:

```bash
python projects/snake-terminal/main.py
```

## 5. Resultado visible esperado

Debes ver el tablero antes y despues de un solo movimiento.

Si la cabeza estaba en el centro y eliges derecha, la `O` debe aparecer una columna mas a la derecha.

Por ejemplo:

```text
Antes:
+----------+
|          |
|    O     |
|          |
+----------+

Despues:
+----------+
|          |
|     O    |
|          |
+----------+
```

## 6. Desafio opcional

Haz que el programa convierta letras minusculas a mayusculas para que `w` y `W` funcionen igual.

Si quieres que el control se sienta mas fluido, intenta una version extra donde no haga falta presionar Enter.

Esa mejora depende del sistema operativo, asi que dejala como experimento opcional:

- En Windows, puedes investigar `msvcrt.getch()`.
- En Linux o Mac, puedes investigar `termios` y `tty`.

No necesitas resolver esto para completar el trial principal.

La meta del desafio es explorar una lectura de teclado mas inmediata, sabiendo que es una ruta mas avanzada y mas dependiente de tu sistema.

## Navegacion

[Anterior: Trial 3](../trial-03-functions/README.md)
[Siguiente: Trial 5](../trial-05-continuous-movement/README.md)
