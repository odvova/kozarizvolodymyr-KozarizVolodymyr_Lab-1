import pygame


class MovementHandler:
    """
    Handles the movement of the player.


    Attributes
    ----------
    player_speed : int
        The speed of the player.

    Methods
    -------
    handle_movement(keys, player_x, player_hitbox)
        Handle the left-right movement of the player.
    """
    def __init__(self, player_speed):
        self.player_speed = player_speed

    def handle_movement(self, keys, player_x, player_hitbox):
        if pygame.K_LEFT in keys and keys[pygame.K_LEFT] and player_x > 15:
            player_x -= self.player_speed
            player_hitbox.x = player_x

        elif pygame.K_RIGHT in keys and keys[pygame.K_RIGHT] and player_x < 785:
            player_x += self.player_speed
            player_hitbox.x = player_x
        return player_x
