# Trial 9 - Configuracion de Turtle

## 1. Objetivo

Abrir una ventana con `turtle` y dibujar el primer elemento visible del juego grafico.

## 2. Explicacion del concepto

La libreria `turtle` te permite dibujar en una ventana usando Python.

En vez de imprimir caracteres en la terminal, ahora vas a mover un cursor grafico.

Este cambio no reemplaza el proyecto de terminal: es una segunda version del mismo juego.

## 3. Conexion con Snake

Ya construiste la logica base en terminal.

Ahora vas a rehacer la experiencia en una ventana grafica, paso a paso, usando ideas parecidas pero con otra forma de mostrar el resultado.

## 4. Requisito concreto

Abre `projects/snake-turtle/main.py`.

Antes de empezar:

La libreria `turtle` depende de `tkinter`.

Si ves un error como `No module named 'tkinter'`, instala el soporte de Tk para tu sistema:

- Linux (Ubuntu/Debian): `sudo apt install python3-tk`
- Linux (Fedora): `sudo dnf install python3-tkinter`
- Linux (Arch): `sudo pacman -S tk`
- Windows: vuelve a ejecutar el instalador oficial de Python y asegurate de incluir `tcl/tk and IDLE`

Luego:

1. Importa `turtle`.
2. Crea una ventana.
3. Crea una forma simple para representar la cabeza de la serpiente.
4. Muestra esa figura en pantalla.

Todavia no necesitas comida ni cuerpo.

Ejecuta:

```bash
python projects/snake-turtle/main.py
```

## 5. Resultado visible esperado

Debes ver una ventana de Turtle con una figura simple que represente el inicio de la serpiente.

## 6. Desafio opcional

Cambia el color de la figura o el fondo de la ventana.

Si usas Windows y `turtle` no abre, revisa primero la instalacion de Python antes de cambiar el codigo.

## Navegacion

[Anterior: Trial 8](../trial-08-score-restart/)
[Siguiente: Trial 10](../trial-10-snake-body-turtle/)
