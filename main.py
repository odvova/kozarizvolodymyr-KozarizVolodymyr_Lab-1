import pygame
from Object import FallingObject
pygame.init()


WINDOW_SIZE = width, heigth = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(WINDOW_SIZE)


game_fall_speed = 0.25
game_number_of_objs_per_spawn = 1
game_time_between_spawns = 1000
game_start_time = pygame.time.get_ticks()
game_score = 0
falling_objects = []


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

        score_display(game_score)
        pygame.display.update()
