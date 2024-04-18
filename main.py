import pygame
from object import GameObjectFactory
from menu import DeathMenu
from movement import MovementHandler

# Constants
WINDOW_SIZE = (800, 600)
WHITE = (255, 255, 255)
FPS = 60
BG_MUSIC_PATH = 'Music/sonic_music.mp3'
ICON_PATH = 'Images/icon/sonic.png'
BACKGROUND_IMAGE_PATH = 'Images/Backgrounds/GameProcessBackground.png'
FONT_PATH = 'Images/Backgrounds/RetroGamingFont.ttf'
PLAYER_LEFT_IMAGES = [f'Images/hero_left/sonic{i}_l.png' for i in range(1, 10)]
PLAYER_RIGHT_IMAGES = [f'Images/hero_right/sonic{i}_r.png' for i in range(1, 10)]


def initialize_game():
    """
    Initialize the game by setting up the screen, background music, background image, player info, and game info.

    :param clock: pygame.time.Clock object
    :param screen: pygame.Surface object
    :param bg_music: pygame.mixer.Sound object
    :param background_image: pygame.Surface object
    :param player_info: dict
    :param game_info: dict
    :param game_running: bool

    :return: clock, screen, bg_music, background_image, player_info, game_info, game_running

    """
    game_running = True
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("DodgeBall Game")
    pygame.display.set_icon(pygame.image.load(ICON_PATH))
    bg_music = pygame.mixer.Sound(BG_MUSIC_PATH)
    bg_music.play(-1)
    background_image = pygame.image.load(BACKGROUND_IMAGE_PATH)

    player_info = {
        'anim_count': 0,
        'x': 55,
        'y': 500,
        'speed': 7,
        'hitbox': pygame.Rect(55, 500, 40, 60)
    }

    game_info = {
        'bg_x': 0,
        'fall_speed': 6,
        'num_objs_per_spawn': 1,
        'time_between_spawns': 1000,
        'start_time': pygame.time.get_ticks(),
        'score': 0,
        'font': pygame.font.Font(FONT_PATH, 24),
        'falling_objects': [],
        'walk_left': [pygame.image.load(img_path) for img_path in PLAYER_LEFT_IMAGES],
        'walk_right': [pygame.image.load(img_path) for img_path in PLAYER_RIGHT_IMAGES]
    }

    return clock, screen, bg_music, background_image, player_info, game_info, game_running


def display_text(text, position, font, screen):
    img = font.render(text, True, (233, 229, 0))
    screen.blit(img, position)


def game_pause(clock, screen, bg_music, font, window_size):
    """
    Pause the game and display pause screen.
    :param clock: pygame.time.Clock object
    :param screen: pygame.Surface object
    :param bg_music: pygame.mixer.Sound object
    :param font: pygame.font.Font object
    :param window_size: tuple

    :return: None

    """
    bg_music.stop()
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    bg_music.play()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        img_pause = font.render('Pause | |', True, (233, 229, 0))
        img_c = font.render('c - continue', True, (233, 229, 0))
        img_q = font.render('q - quit game', True, (233, 229, 0))
        screen.blit(img_pause, ((window_size[0] / 2) - 50, (window_size[1] / 2) - 50))
        screen.blit(img_c, ((window_size[0] / 2) - 90, (window_size[1] / 2) - 20))
        screen.blit(img_q, ((window_size[0] / 2) - 90, window_size[1] / 2))
        pygame.display.update()
        clock.tick(5)


def handle_events():
    """
    Handle events such as quitting the game or pausing the game.
    :return:  None

    """
    global game_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_pause(clock, screen, bg_music, game_info['font'], window_size)


def update_falling_objects():
    """
    Update the falling objects by increasing the speed and adding new objects.
    :return: None

    """
    game_now_time = pygame.time.get_ticks()
    if game_now_time - game_info['start_time'] > game_info['time_between_spawns']:
        game_info['start_time'] = game_now_time
        game_info['falling_objects'].append(GameObjectFactory.create_falling_object(window_size))
        game_info['fall_speed'] += 0.05

    objects_to_remove = []
    for obj in game_info['falling_objects']:
        obj.update_position(game_info['fall_speed'])
        obj.spawn_obj(screen, WHITE)
        if player_info['hitbox'].colliderect(pygame.Rect(obj.x, obj.y, 20, 20)):
            handle_collision()
        if obj.y > 600:
            objects_to_remove.append(obj)
            game_info['score'] += 5

    for obj in objects_to_remove:
        game_info['falling_objects'].remove(obj)


def handle_collision():
    death_menu = DeathMenu(screen)
    death_menu.run()
    game_info['score'] = 0
    game_info['fall_speed'] = 6
    game_info['time_between_spawns'] = 1000
    game_info['falling_objects'] = []
    game_info['start_time'] = pygame.time.get_ticks()


def render_game(keys):
    """
    Render the game by displaying the score, time, falling objects, player, and updating the display.
    :param keys: pygame.key.get_pressed()

    :return: keys
    """
    screen.blit(pygame.transform.scale(background_image, window_size), (0, 0))
    display_text(f'Score {game_info["score"]}', (20, 20), game_info['font'], screen)
    display_text(f'Time {pygame.time.get_ticks() / 1000}', (20, 50), game_info['font'], screen)

    for obj in game_info['falling_objects']:
        obj.spawn_obj(screen, WHITE)

    player_image = game_info['walk_left'][player_info['anim_count']] if keys[pygame.K_LEFT] else \
        game_info['walk_right'][player_info['anim_count']]
    screen.blit(player_image, (player_info['x'], player_info['y']))
    player_info['anim_count'] += 1
    if player_info['anim_count'] >= len(game_info['walk_right']):
        player_info['anim_count'] = 0
    pygame.display.flip()


if __name__ == "__main__":
    clock, screen, bg_music, background_image, player_info, game_info, game_running = initialize_game()
    window_size = WINDOW_SIZE

    movement_handler = MovementHandler(player_info['speed'])

    while True:
        handle_events()
        update_falling_objects()
        keys = pygame.key.get_pressed()
        player_info['x'] = movement_handler.handle_movement(keys, player_info['x'], player_info['hitbox'])
        render_game(keys)
        clock.tick(FPS)
        pygame.display.update()

