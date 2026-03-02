# Trial 8 - Puntaje y reinicio

## 1. Objetivo

Mostrar un puntaje y permitir jugar otra vez sin cerrar el programa.

## 2. Explicacion del concepto

Ahora vas a usar variables de estado para guardar:

- el puntaje
- si el jugador quiere reiniciar

Cada vez que la serpiente come, el puntaje aumenta.

Cuando termina la partida, puedes preguntar si el jugador quiere volver a empezar.

## 3. Conexion con Snake

Con puntaje, el jugador puede medir su progreso.

Con reinicio, el juego ya se puede volver a jugar sin tener que ejecutar el archivo otra vez.

Eso deja completa la primera version del Snake en terminal.

## 4. Requisito concreto

Abre `projects/snake-terminal/main.py` y toma tu version del trial anterior.

Luego:

1. Crea una variable para el puntaje.
2. Suma puntos cada vez que la serpiente come comida.
3. Muestra el puntaje en pantalla.
4. Cuando aparezca `Game Over`, pregunta si el jugador quiere reiniciar.
5. Si responde que si, vuelve a crear el estado inicial del juego.

La meta es que el juego pueda empezar otra vez sin cerrar el programa.

Ejecuta:

```bash
python projects/snake-terminal/main.py
```

## 5. Resultado visible esperado

Debes ver el puntaje durante la partida y, al perder, una opcion para volver a jugar.

## 6. Desafio opcional

Guarda y muestra el mejor puntaje de la sesion mientras el programa siga abierto.

## Navegacion

[Anterior: Trial 7](../trial-07-collision-detection/README.md)
[Siguiente: Trial 9](../trial-09-turtle-setup/README.md)
