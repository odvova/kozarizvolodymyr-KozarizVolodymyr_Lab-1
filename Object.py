from random import randint

import pygame
from pygame import draw


class FallingObject:
    def __init__(self, window_size: list) -> None:
        self.x = randint(0, window_size[0])
        self.y = 0

    def spawn_obj(self, surface, color) -> pygame.Rect:
        obj_rect = pygame.Rect(self.x, self.y, 20, 20)
        draw.rect(surface, color, obj_rect)
        return obj_rect

    def update_position(self, speed: float) -> None:
        self.y += speed
