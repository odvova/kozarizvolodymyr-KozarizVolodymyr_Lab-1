from random import randint
from pygame import draw


class FallingObject:
    def __init__(self, window_size: list) -> None:
        self.x = randint(0, window_size[0])
        self.y = 0

    def spawn_obj(self, surface, color) -> None:
        draw.rect(surface, color, (self.x, self.y, 20, 20))

    def update_position(self, speed: float) -> None:
        self.y += speed
