import pygame
from Object import FallingObject
pygame.init()
clock = pygame.time.Clock()

WINDOW_SIZE = width, heigth = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30




screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("DodgeBall Game")
icon = pygame.image.load('Images/icon/sonic.png')
pygame.display.set_icon(icon)
bg_music = pygame.mixer.Sound('Music/sonic_music.mp3')
bg_music.play(-1)

player_anim_count = 0 
player_x = 100  
player_y = 500
player_speed = 7
bg_x = 0
game_fall_speed = 6 # 0.5
game_number_of_objs_per_spawn = 1
game_time_between_spawns = 1000
game_start_time = pygame.time.get_ticks()
game_score = 0
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
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'Score {game_score}', True, WHITE)
    screen.blit(img, (20, 20))


if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        game_now_time = pygame.time.get_ticks()

        if game_now_time - game_start_time > game_time_between_spawns:
            game_start_time = game_now_time
            falling_objects.append(FallingObject(WINDOW_SIZE))

            game_time_between_spawns -= 5  # Needs to be normalized
            game_fall_speed += 0.005       # Needs to be normalized

        for obj in falling_objects:  # Updating object 'Y' coordinate
            obj.update_position(game_fall_speed)
        screen.fill((0, 0, 0))

        for obj in falling_objects:
            obj.spawn_obj(screen, WHITE)  # Draw object

            if obj.y > 600:  # Check if object already crashed
                falling_objects.remove(obj)
                game_score += 5
                print(game_score)

        # screen.fill((0, 0, 0))
    
        keys = pygame.key.get_pressed() # модуль key
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x,player_y))
        elif keys[pygame.K_RIGHT]:
            screen.blit(walk_right[player_anim_count],(player_x,player_y))
        else:
            screen.blit(walk_right[0], (player_x,player_y)) 

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
        score_display(game_score)
        pygame.display.update()
