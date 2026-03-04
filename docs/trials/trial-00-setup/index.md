# Trial 0 - Setup y primera ejecución

## 🎯 Objetivo

Preparar tu entorno de trabajo, crear tu copia del proyecto y ejecutar tu primer programa en Python.

Hoy no construimos la serpiente.

Hoy construimos la base.

Hoy tomas control.

---

## 🧠 ¿Qué está pasando aquí?

Antes de crear un juego, necesitas algo más importante:

👉 Un proyecto que sea tuyo.
👉 Herramientas funcionando en tu computadora.
👉 Poder ejecutar código cuando tú quieras.

Cuando puedes correr un archivo `.py`, significa que tienes control sobre la máquina.

Y eso es donde empieza todo.

---

# 🧰 Parte 1 — Preparar tus herramientas

Si ya tienes todo instalado, puedes saltar esta sección.
Si no, sigue los pasos con calma.

---

## 1️⃣ Instalar Visual Studio Code

Visual Studio Code (VS Code) será nuestro editor principal.

Es donde escribiremos todo el código.

1. Ve a: https://code.visualstudio.com
2. Descarga la versión para tu sistema operativo (Windows).
3. Instálalo normalmente (siguiente, siguiente, siguiente).

Cuando termine, abre VS Code para confirmar que funciona.

---

## 2️⃣ Instalar Python

Si no tienes Python instalado:

1. Ve a: https://www.python.org/downloads/
2. Descarga la versión más reciente para Windows.
3. Durante la instalación, marca la opción:

Add Python to PATH

Esto es MUY importante.

Después de instalarlo, abre una terminal (puede ser la de VS Code más adelante) y escribe:

python --version

Si ves un número de versión, todo está correcto.

---

## 3️⃣ Instalar Git (si no lo tienes)

Git nos permite:

- Guardar cambios
- Subir nuestro progreso
- Trabajar como programadores reales

Para instalarlo:

1. Ve a: https://git-scm.com/download/win
2. Descarga Git for Windows
3. Instálalo con las opciones por defecto

Después de instalarlo, reinicia VS Code si estaba abierto.

---

## 4️⃣ Extensión de Git en VS Code

VS Code ya incluye soporte para Git.

Pero asegúrate de que:

- En la barra lateral izquierda aparece el ícono de "Source Control" (parece una ramita).
- No aparece ningún error diciendo que Git no está instalado.

Si todo se ve normal, estás listo.

---

# 🌐 Parte 2 — GitHub y tu copia del proyecto

---

## 5️⃣ Crear una cuenta en GitHub

Si no tienes cuenta:

1. Ve a https://github.com
2. Crea una cuenta gratuita.
3. Verifica tu correo.

GitHub será tu lugar para guardar tu proyecto en internet.

Es como tu portafolio de programador.

---

## 6️⃣ Hacer un Fork del repositorio

Ir al repositorio principal de Serpent Trials.

Haz clic en el botón:

Fork

Esto crea una copia del proyecto en tu cuenta.

Ahora el proyecto es tuyo.

---

## 7️⃣ Clonar tu Fork

En tu repositorio (el que está en tu cuenta):

1. Haz clic en el botón verde "Code".
2. Copia la URL.
3. En VS Code:
   - Presiona Ctrl + Shift + P
   - Escribe: Git: Clone
   - Pega la URL
   - Elige una carpeta en tu computadora

Cuando termine, abre esa carpeta en VS Code.

Ahora tienes el proyecto en tu máquina.

Eso ya es un gran paso.

---

# 🐍 Parte 3 — Ejecutar tu primer programa

---

## 🛠️ Requisito concreto

1. Abre la carpeta del proyecto en VS Code.
2. Abre la terminal dentro de VS Code (Terminal → New Terminal).
3. Ejecuta:

python projects/snake-terminal/main.py

---

## ✅ Resultado esperado

Debes ver en la terminal:

Welcome to Serpent Trials

Si ves ese mensaje, significa que:

- Python está funcionando.
- Git está funcionando.
- El proyecto está correctamente clonado.
- Puedes ejecutar tu propio código.

Eso es poder.

No estás viendo un video.

No estás leyendo teoría.

Estás ejecutando código real.

---

## 🚀 Desafío opcional

Abre el archivo:

projects/snake-terminal/main.py

Busca el mensaje que se imprime.

Cámbialo para incluir tu nombre.

Ejemplo:

Welcome to Serpent Trials, Sofia

Guarda el archivo.

Vuelve a ejecutar el programa.

Si el mensaje cambia, significa que:

- Editaste código
- Ejecutaste código
- Cambiaste el comportamiento del programa

Eso significa que ya empezaste a programar.

---

## 📍 Navegación

[Siguiente: Trial 1](../trial-01-variables/README.md)