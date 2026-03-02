# Trial 2 - Listas y coordenadas

## 1. Objetivo

Guardar la posicion de la serpiente usando coordenadas para que el juego tenga un estado mas claro.

## 2. Explicacion del concepto

Una lista te permite guardar varios valores en orden.

En Snake, eso es util porque la serpiente no se entiende solo como un dibujo en pantalla. Tambien necesita una posicion en el tablero.

Una coordenada es una forma de indicar un lugar, por ejemplo:

```text
[4, 2]
```

Eso puede significar:

- columna 4
- fila 2

Si guardas la posicion de la cabeza en una lista, luego sera mucho mas facil moverla.

## 3. Conexion con Snake

En el trial anterior dibujaste una `O`, pero esa `O` estaba puesta de forma fija.

Ahora vas a guardar su posicion en una variable con forma de lista.

Eso hace que la serpiente ya no sea solo un dibujo: ahora tambien tiene datos.

## 4. Requisito concreto

Abre `projects/snake-terminal/main.py` y cambia tu version del trial anterior para que:

1. Guardes la posicion de la cabeza en una lista como `snake_head = [x, y]`.
2. Uses esos valores para decidir en que parte del tablero aparece la `O`.
3. Mantengas el tablero visible en la terminal.

No necesitas mover la serpiente todavia.

La meta es que la `O` siga apareciendo, pero ahora su posicion debe salir de una coordenada guardada en una lista.

Ejecuta:

```bash
python projects/snake-terminal/main.py
```

## 5. Resultado visible esperado

Debes seguir viendo un tablero con una `O` dentro.

La diferencia importante es interna: ahora la posicion ya no esta escrita "a mano" en el dibujo, sino guardada en una lista de coordenadas.

Por ejemplo, si usas una coordenada como `[4, 2]`, el resultado podria verse asi:

```text
+----------+
|          |
|          |
|    O     |
|          |
+----------+
```

## 6. Desafio opcional

Crea una segunda coordenada de prueba y mueve la `O` cambiando solo los numeros de la lista.
