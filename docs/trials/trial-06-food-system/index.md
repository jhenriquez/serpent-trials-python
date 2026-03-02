# Trial 6 - Sistema de comida

## 1. Objetivo

Agregar comida al tablero para que la serpiente pueda comer y crecer.

## 2. Explicacion del concepto

Ahora vas a sumar dos ideas nuevas:

- un valor aleatorio para colocar comida
- una condicion para revisar si la cabeza llego a esa posicion

Puedes usar el modulo `random` para elegir una coordenada dentro del tablero.

Cuando la cabeza de la serpiente toca esa coordenada, significa que la comida fue comida.

## 3. Conexion con Snake

Sin comida, Snake solo se mueve.

Con comida, ya existe un objetivo claro para el jugador.

Este cambio convierte el movimiento en una mecanica real del juego.

## 4. Requisito concreto

Abre `projects/snake-terminal/main.py` y toma tu version del trial anterior.

Luego:

1. Crea una coordenada para la comida.
2. Muestra la comida en el tablero con un simbolo consistente, por ejemplo `*`.
3. Revisa si la cabeza toca la comida.
4. Si la toca, haz crecer la serpiente.
5. Coloca una nueva comida en otra coordenada.

La comida debe aparecer dentro del tablero y no fuera de los bordes.

Ejecuta:

```bash
python projects/snake-terminal/main.py
```

## 5. Resultado visible esperado

Debes ver una comida en pantalla y, cuando la serpiente la alcance, la serpiente debe crecer y aparecer una nueva comida.

Por ejemplo, el tablero ya no tiene solo `O`, tambien debe mostrar `*`.

## 6. Desafio opcional

Haz que la comida nunca aparezca encima del cuerpo de la serpiente.

## Navegacion

[Anterior: Trial 5](../trial-05-continuous-movement/)
[Siguiente: Trial 7](../trial-07-collision-detection/)
