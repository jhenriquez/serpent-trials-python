# Solutions

These are reference implementations for learners who want to compare their work after attempting the trials.

- `solutions/snake-terminal/main.py` contains a complete terminal Snake game.
- `solutions/snake-turtle/main.py` contains a complete Turtle Snake game.

The starter files in `projects/` remain unchanged for students to edit during the course.

## Turtle Requirement

The Turtle solution needs `tkinter`, because Python's `turtle` module depends on it.

If `solutions/snake-turtle/main.py` fails with `No module named 'tkinter'`, install the Tk package for your system Python first.

### Linux

- Ubuntu or Debian: `sudo apt install python3-tk`
- Fedora: `sudo dnf install python3-tkinter`
- Arch: `sudo pacman -S tk`

### Windows

- If you installed Python from python.org, `tkinter` is usually included already. Re-run the Python installer and make sure `tcl/tk and IDLE` is enabled.
- If you installed Python with `winget` or the Microsoft Store and `tkinter` is missing, install the official python.org build instead.
