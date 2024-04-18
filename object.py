from random import randint
import pygame
from pygame import draw


class GameObjectFactory:
    """
    A factory class to create falling objects.

    Methods
    -------
    create_falling_object(window_size)
        Create a falling object.
    """
    @staticmethod
    def create_falling_object(window_size):
        return FallingObject(window_size)


class FallingObject:
    """
    A class to represent a falling object.

    Attributes
    ----------
    falling_objects : list
        A list of all falling objects.
    x : int
        The x-coordinate of the falling object.
    y : int
        The y-coordinate of the falling object.

    Methods
    -------
    __init__(window_size)
        Initialize the falling object.
    spawn_obj(surface, color)
        Spawn the falling object on the surface.
    update_position(speed)
        Update the position of the falling object.
    """
    falling_objects = []

    def __init__(self, window_size: list) -> None:
        self.x = randint(0, window_size[0])
        self.y = 0
        FallingObject.falling_objects.append(self)

    def spawn_obj(self, surface, color) -> pygame.Rect:
        obj_rect = pygame.Rect(self.x, self.y, 20, 20)
        draw.rect(surface, color, obj_rect)
        return obj_rect

    def update_position(self, speed: float) -> None:
        self.y += speed
