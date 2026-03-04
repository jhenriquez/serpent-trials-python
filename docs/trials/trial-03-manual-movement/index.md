# Trial 3 - Movimiento manual

## 1. Objetivo

Hacer que la `O` (la cabeza de la serpiente) **se mueva** cambiando sus coordenadas.

En este trial todavía no hay “serpiente larga”, ni comida, ni choque.

Solo esto:

- tienes una posición `[x, y]`
- cambias esa posición con teclas
- vuelves a dibujar el tablero
- y ves la `O` moverse

Eso ya es un juego empezando a vivir.

---

## 2. Idea clave: “Mover” es cambiar números

Tu tablero es una cuadrícula.

La serpiente (por ahora) es solo una coordenada:

    snake = [x, y]

Mover significa ajustar esos números:

- izquierda  → `x - 1`
- derecha    → `x + 1`
- arriba     → `y - 1`
- abajo      → `y + 1`

No hay magia.

Solo sumar o restar.

---

## 3. Reglas de este trial

### 3.1 Movimiento por turnos (no tiempo real)
Todavía no vamos a hacer “teclas en vivo”.

Vamos a hacer movimiento por turnos usando `input()`:

- El programa dibuja el tablero
- Te pregunta qué hacer
- Tú escribes una letra y presionas Enter
- La `O` se mueve
- Se vuelve a dibujar

Esto es perfecto para aprender sin complicarnos.

### 3.2 Controles (simple y clásico)
Usa letras simples:

- `w` = arriba
- `s` = abajo
- `a` = izquierda
- `d` = derecha
- `q` = salir

---

## 4. Un detalle importante: límites del tablero

Si la `O` se sale del tablero, tu dibujo se rompe.

En este trial usa una regla fácil:

- Si el movimiento intenta salir, **no lo permitas**
- La serpiente se queda donde está

Ejemplo:
- Si `x` ya está en `0` y presionas `a`, no pasa nada.

---

## 5. Requisito concreto

Abre:

    projects/snake-terminal/main.py

Partiendo de tu Trial 2, haz estos cambios:

1) Mantén la posición de la serpiente como coordenadas (`snake_x`, `snake_y` o `snake = [x, y]`).
2) Crea un loop principal que repita:
   - dibujar tablero con la `O` en la posición actual
   - pedir comando con `input()`
   - actualizar posición según `w/a/s/d`
3) Permite salir con `q`.

Importante:
- No necesitas funciones todavía.
- Hoy aceptamos un `main()` más largo.
- En el próximo trial, lo vamos a limpiar con funciones (porque ahora sí vale la pena).

Ejecuta:

    python projects/snake-terminal/main.py

---

## 6. Resultado visible esperado

Una sesión típica debería verse más o menos así:

    +----------+
    |          |
    |    O     |
    |          |
    |          |
    +----------+
    Move (w/a/s/d) or q to quit: d

Luego redibuja y la `O` aparece un paso más a la derecha.

---

## 7. Pista rápida: “redibujar” en terminal

Tu programa va a imprimir muchos tableros uno debajo del otro.

Eso está bien por ahora.

Más adelante aprenderemos a “limpiar” la pantalla para que parezca animación real.

Hoy lo importante es que:

- cambie la coordenada
- el dibujo refleje ese cambio

---

## 8. Desafío opcional

### Opción A: comandos en mayúscula
Permite que `WASD` también funcione.

### Opción B: wrap-around (modo “Pac-Man”)
En vez de bloquear el borde:

- si sales por la izquierda, apareces por la derecha
- si sales por arriba, apareces por abajo

Esta opción es más divertida, pero requiere pensar bien los límites.

## 🔥 Desafío adicional – Mejora visual

Si probaste mover la `O` varias veces, seguramente notaste algo:

El tablero se imprime una y otra vez hacia abajo en la terminal.

No es un error.

Eso pasa porque cada vez que el programa dibuja, simplemente imprime otro tablero debajo del anterior.

Pero podemos mejorar eso.

---

### 🎯 Objetivo del desafío

Limpiar la pantalla antes de volver a dibujar el tablero, para que parezca que la `O` se mueve en el mismo lugar.

---

### 🛠 Cómo hacerlo

1. Importa el módulo `os` al inicio de tu archivo:

   import os

2. Justo antes de dibujar el tablero en cada turno, agrega:

   os.system("clear")

Eso limpia la pantalla en macOS y Linux.

Si estás usando Windows, usa:

   os.system("cls")

---

### 🧠 ¿Qué está pasando aquí?

Tu programa no está "moviendo" nada realmente.

Lo que hace es:

- borrar la pantalla
- volver a dibujar todo
- pero con la nueva posición

Eso crea la ilusión de movimiento.

---

### 🚀 Resultado esperado

Ahora, cada vez que presiones `w`, `a`, `s` o `d`, el tablero se verá limpio y la `O` parecerá moverse suavemente.

Pequeño cambio.
Gran mejora visual.

Ese es el poder de entender cómo funciona realmente la terminal.

---

## Navegación

[Anterior: Trial 2](../trial-02-lists-coordinates/README.md)
[Siguiente: Trial 4](../trial-04-functions/README.md)