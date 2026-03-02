# Trial 7 - Deteccion de colisiones

## 1. Objetivo

Terminar la regla principal del juego: perder cuando la serpiente choca.

## 2. Explicacion del concepto

Una colision ocurre cuando la cabeza entra en una posicion no permitida.

En este trial vas a revisar dos casos:

- choque con una pared
- choque con el propio cuerpo

Eso se resuelve con condiciones `if` que comparan la cabeza con los limites del tablero y con las posiciones guardadas en la serpiente.

## 3. Conexion con Snake

Sin colisiones, el juego no tiene riesgo.

Al agregar esta regla, ya existe una forma de ganar puntos y una forma de perder.

Eso completa la base del reto de Snake.

## 4. Requisito concreto

Abre `projects/snake-terminal/main.py` y toma tu version del trial anterior.

Luego:

1. Revisa si la cabeza sale del tablero.
2. Revisa si la cabeza toca otra parte del cuerpo.
3. Si ocurre una colision, termina el bucle del juego.
4. Muestra un mensaje como `Game Over`.

No necesitas reiniciar todavia.

La meta es que el juego se detenga claramente cuando ocurre un choque.

Ejecuta:

```bash
python projects/snake-terminal/main.py
```

## 5. Resultado visible esperado

Cuando la serpiente toca una pared o su propio cuerpo, el movimiento debe detenerse y debes ver un mensaje de fin de juego.

## 6. Desafio opcional

Muestra un mensaje diferente segun el tipo de colision: pared o cuerpo.
