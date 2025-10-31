import pygame
import sys
from game import Game
from menu import MainMenu

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game(screen, screen_width, screen_height)
    delay_duration = 1000

    #C
    # Reusar el score manager ya inicializado dentro de Game para evitar inconsistencias
    score_manager = game.score_manager
    score_manager.load_scores()

    main_menu = MainMenu(screen_width, screen_height, score_manager)
    #CF

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)
    in_main_menu = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Manejar teclas globales (siempre deben tener efecto)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game.restart_level()
                # Asegurar flags coherentes
                game.game_over = False
                game.in_main_menu = False
                in_main_menu = False
            if in_main_menu:
                action = main_menu.handle_event(event)
                if action == "start_game":
                    # Reiniciar estado del juego por si venimos de un game over
                    game.restart_level()
                    in_main_menu = False
                    game.in_main_menu = False
                elif action == "quit":
                    pygame.quit()
                    sys.exit()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game.paused = not game.paused
                    if event.key == pygame.K_ESCAPE:
                        # Volver al menú principal
                        in_main_menu = True
                        game.in_main_menu = True
                        # Asegurar que el estado de game_over no persista
                        game.game_over = False

                if not game.paused:
                    if event.type == ALIENLASER:
                        game.alien_shoot()

        screen.fill((30, 30, 30))

        if in_main_menu:
            main_menu.draw(screen)
        else:
            if game.paused:
                pause_message = game.font.render("PAUSA", True, (255, 255, 255))
                screen.blit(pause_message, (screen_width // 2 - pause_message.get_width() // 2,
                                            screen_height // 2 - pause_message.get_height() // 2))
            else:
                game.run()
                #C
                if game.game_over:
                    new_score = game.player.sprite.score  # Obtén el puntaje del jugador cuando el juego termine
                    score_manager.add_score(new_score)  # Agrega el puntaje a la lista de puntajes
                    score_manager.save_scores()  # Guarda los puntajes actualizados
                    # Obtener los nuevos puntajes máximos después de agregar el nuevo puntaje.
                    top_scores = score_manager.get_top_scores()
                    print("Updated Top Scores:", top_scores)
                    #limpiar nivel
                    # Asegurar que el reinicio ocurra pero manteniendo el estado de game_over hasta volver al menú
                    game.restart_level()
                    # Establece el retraso de 1 segundo1 (1000 milisegundos)
                    pygame.time.delay(delay_duration)
                    in_main_menu = True
                    game.in_main_menu = True

                #CF

        pygame.display.flip()
        clock.tick(60)

    # Fin del bucle principal — guardar puntajes si se llegase aquí (no debería ocurrir)
    # (esta sección normalmente no se alcanza porque el loop principal es infinito)
