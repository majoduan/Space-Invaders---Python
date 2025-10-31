from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
GRAPHICS_DIR = BASE_DIR / 'Graphics'
AUDIO_DIR = BASE_DIR / 'Audio'

files = [
    GRAPHICS_DIR / 'player.png',
    GRAPHICS_DIR / 'red.png',
    GRAPHICS_DIR / 'green.png',
    GRAPHICS_DIR / 'yellow.png',
    GRAPHICS_DIR / 'extra.png',
    AUDIO_DIR / 'laser.wav',
    AUDIO_DIR / 'laserAlien.wav',
    AUDIO_DIR / 'explosion.wav',
    AUDIO_DIR / 'music.wav',
    AUDIO_DIR / 'gameOver.mp3',
]

missing = []
for f in files:
    if not f.exists():
        missing.append(str(f))
        print(f"MISSING: {f}")
    else:
        print(f"FOUND:   {f}")

if not missing:
    print('\nAll assets found')
else:
    print(f'\nMissing {len(missing)} files')

