import pygame
from Object import FallingObject
pygame.init()
clock = pygame.time.Clock()

WINDOW_SIZE = width, heigth = 800, 600
WHITE = (255, 255, 255)
FPS = 60


screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("DodgeBall Game")
icon = pygame.image.load('Images/icon/sonic.png')
pygame.display.set_icon(icon)
bg_music = pygame.mixer.Sound('Music/sonic_music.mp3')
bg_music.play(-1)
background_image = pygame.image.load(
    'Images/Backgrounds/GameProcessBackground.png')

player_anim_count = 0
player_x = 100
player_y = 500
player_speed = 7
bg_x = 0
game_fall_speed = 6  # 0.5
game_number_of_objs_per_spawn = 1
game_time_between_spawns = 1000
game_start_time = pygame.time.get_ticks()
game_score = 0
game_font = pygame.font.Font('Images/Backgrounds/RetroGamingFont.ttf', 24)
falling_objects = []
walk_left = [
    pygame.image.load('Images/hero_left/sonic1_l.png'),
    pygame.image.load('Images/hero_left/sonic2_l.png'),
    pygame.image.load('Images/hero_left/sonic3_l.png'),
    pygame.image.load('Images/hero_left/sonic4_l.png'),
    pygame.image.load('Images/hero_left/sonic5_l.png'),
    pygame.image.load('Images/hero_left/sonic6_l.png'),
    pygame.image.load('Images/hero_left/sonic7_l.png'),
    pygame.image.load('Images/hero_left/sonic8_l.png'),
    pygame.image.load('Images/hero_left/sonic9_l.png'),
]
walk_right = [
    pygame.image.load('Images/hero_right/sonic1_r.png'),
    pygame.image.load('Images/hero_right/sonic2_r.png'),
    pygame.image.load('Images/hero_right/sonic3_r.png'),
    pygame.image.load('Images/hero_right/sonic4_r.png'),
    pygame.image.load('Images/hero_right/sonic5_r.png'),
    pygame.image.load('Images/hero_right/sonic6_r.png'),
    pygame.image.load('Images/hero_right/sonic7_r.png'),
    pygame.image.load('Images/hero_right/sonic8_r.png'),
    pygame.image.load('Images/hero_right/sonic9_r.png'),
]


def score_display(score: int) -> None:
    img = game_font.render(f'Score {game_score}', True, (233, 229, 0))
    screen.blit(img, (20, 20))


def game_pause() -> None:
    game_pause = True
    bg_music.stop()

    while game_pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_pause = False
                    bg_music.play()

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        img_pause = game_font.render('Pause | |', True, (233, 229, 0))
        img_c = game_font.render('c - countinue', True, (233, 229, 0))
        img_q = game_font.render('q - quit game', True, (233, 229, 0))
        screen.blit(
            img_pause, ((WINDOW_SIZE[0]/2) - 50, (WINDOW_SIZE[1]/2) - 50))
        screen.blit(
            img_c, ((WINDOW_SIZE[0]/2) - 90, (WINDOW_SIZE[1]/2) - 20))
        screen.blit(
            img_q, ((WINDOW_SIZE[0]/2) - 90, WINDOW_SIZE[1]/2))

        pygame.display.update()
        clock.tick(5)


def game_time_display(time: float) -> None:
    if time >= 60:
        minutes = int(time // 60)
        seconds = int(time % 60)
        img = game_font.render(
            f'Time {minutes} : {seconds}', True, (233, 229, 0))
        screen.blit(img, (20, 50))
    else:
        img = game_font.render(f'Time {time}', True, (233, 229, 0))
        screen.blit(img, (20, 50))


if __name__ == "__main__":
    while True:
        # Setting background image
        background_image = pygame.transform.scale(background_image, (800, 600))
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        game_now_time = pygame.time.get_ticks()
        game_time_display(game_now_time/1000)
        score_display(game_score)

        if game_now_time - game_start_time > game_time_between_spawns:
            game_start_time = game_now_time
            falling_objects.append(FallingObject(WINDOW_SIZE))

            # game_time_between_spawns -= 5  # Needs to be normalized
            game_fall_speed += 0.05          # Needs to be normalized

        for obj in falling_objects:  # Updating object 'Y' coordinate
            obj.update_position(game_fall_speed)

        for obj in falling_objects:
            obj.spawn_obj(screen, WHITE)  # Draw object

            if obj.y > 600:  # Check if object already crashed
                falling_objects.remove(obj)
                game_score += 5

        keys = pygame.key.get_pressed()  # модуль key
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_RIGHT]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[0], (player_x, player_y))
        if keys[pygame.K_ESCAPE]:
            game_pause()

        # Збільшення лічильника кадрів
        player_anim_count += 1
        if player_anim_count >= len(walk_right):
            player_anim_count = 0

        if keys[pygame.K_LEFT] and player_x > 15:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 740:
            player_x += player_speed
            # Оновлення екрану
            pygame.display.flip()

        clock.tick(FPS)
        pygame.display.update()
