Space Invaders - Python
=====================================

Pequeña versión del clásico Space Invaders escrita en Python con pygame.

Contenido
--------
- Código fuente: `Code/`
- Recursos gráficos: `Graphics/`
- Recursos de audio: `Audio/`
- Configuración: `config.txt` (opcional)
- Puntuaciones: `Code/scores.txt`

Descripción
-----------
Este proyecto implementa una versión simple de Space Invaders con:
- Movimiento del jugador y disparos.
- Varias filas de aliens con diferentes puntuaciones.
- Obstáculos destructibles.
- Aliens extra que aparecen ocasionalmente.
- Menú principal y sistema de puntajes.

Requisitos
---------
- Python 3.8+ (probado con 3.10/3.11)
- pygame (recomendado la versión más reciente estable)

Instalación (Windows, cmd.exe)
-----------------------------
1. Crear (opcional) y activar un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Instalar dependencia:

```bash
pip install pygame
```

Ejecución
--------
Desde la carpeta del proyecto puedes ejecutar:

```bash
python "Code\main.py"
```

o navegando a la carpeta `Code`:

```bash
cd "Code"
python main.py
```

Controles
--------
- Flechas izquierda / derecha: mover la nave
- Barra espaciadora: disparar
- P: pausar / reanudar
- R: reiniciar nivel (restablece velocidad de enemigos y vidas)
- ESC: volver al menú principal

Estructura del repositorio
-------------------------
- Code/: código Python (main, game, player, alien, etc.)
- Graphics/: imágenes usadas por el juego
- Audio/: sonidos y música
- README.md: este archivo

Notas de desarrollo y decisiones
-------------------------------
- Las rutas a los assets se cargan con rutas relativas (pathlib) para evitar dependencias de rutas absolutas en el sistema del autor.
- El manejo de eventos se centraliza en `Code/main.py` para evitar que eventos (como la tecla R) se consuman en múltiples lugares.

Problemas conocidos y soluciones
-------------------------------
- Si recibes un error "No module named pygame", instala pygame con `pip install pygame`.
- En algunos entornos, la reproducción de audio puede requerir controladores o permisos del SO.

Contribuciones
--------------
Si quieres mejorar el proyecto:
1. Crea un fork
2. Crea una rama para tu feature/fix
3. Abre un pull request explicando los cambios

Licencia
--------
Todos los Derechos Reservados por licencia MIT.

Créditos
-------
Proyecto de práctica para la universidad. Recursos gráficos y de audio incluidos en las carpetas `Graphics` y `Audio`.

Creador
--------
Mateo Dueñas
