import pygame
from laser import Laser
from pathlib import Path


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        # Cargar recursos usando rutas relativas al repositorio
        BASE_DIR = Path(__file__).resolve().parent.parent
        GRAPHICS_DIR = BASE_DIR / 'Graphics'
        AUDIO_DIR = BASE_DIR / 'Audio'

        self.image = pygame.image.load(str(GRAPHICS_DIR / 'player.png')).convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_x_constraint = constraint
        #Variables para el disparo
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 1000
        self.lasers = pygame.sprite.Group()
        # Usar ruta relativa para el sonido
        self.laser_sound = pygame.mixer.Sound(str(AUDIO_DIR / 'laser.wav'))
        self.laser_sound.set_volume(0.05)

        #puntuacion
        self.score = 0

        # Variables para el parpadeo cuando recibe daño
        self.is_hit = False
        self.hit_time = 0
        self.blink_duration = 2000  # Duración del parpadeo en milisegundos (2 segundos)
        self.blink_interval = 100  # Intervalo de parpadeo en milisegundos
        self.visible = True

    def take_damage(self):
        """Marca al jugador como golpeado y comienza el parpadeo"""
        self.is_hit = True
        self.hit_time = pygame.time.get_ticks()
        self.visible = True

    def update_blink(self):
        """Actualiza el estado de parpadeo del jugador"""
        if self.is_hit:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.hit_time

            if elapsed_time < self.blink_duration:
                # Alternar visibilidad basado en el intervalo de parpadeo
                self.visible = (elapsed_time // self.blink_interval) % 2 == 0
            else:
                # Terminar el parpadeo
                self.is_hit = False
                self.visible = True

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        #Implementar mecánica de disparo
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        """Función de recarga, se vizualiza la resta entre el tiempo actual y el tiempo desde que se
        disparó el ultimo proyectil, si ese tiempo es mayor al cooldawn entonces el boleano se cambia
        a verdadero para volver a tener la posibilidad de dispara."""
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time > self.laser_cooldown:
                self.ready = True

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    # Añadir mecánica de disparo
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center,-6,self.rect.bottom))
        self.laser_sound.play()
    def update(self):

        self.get_input()
        self.constraint()
        self.recharge()
        self.update_blink()  # Actualizar el estado de parpadeo
        self.lasers.update()