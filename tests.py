import unittest
from unittest.mock import patch
import pygame
from movement import MovementHandler
from object import GameObjectFactory, FallingObject


class TestMovementHandler(unittest.TestCase):
    def setUp(self):
        self.movement_handler = MovementHandler(5)

    def test_handle_movement_left(self):
        keys = {pygame.K_LEFT: True}
        player_x = 20
        player_hitbox = pygame.Rect(20, 20, 20, 20)
        self.assertEqual(self.movement_handler.handle_movement(keys, player_x, player_hitbox), 15)

    def test_handle_movement_right(self):
        keys = {pygame.K_RIGHT: True}
        player_x = 20
        player_hitbox = pygame.Rect(20, 20, 20, 20)
        self.assertEqual(self.movement_handler.handle_movement(keys, player_x, player_hitbox), 25)

    def test_handle_movement_no_key(self):
        keys = {}
        player_x = 20
        player_hitbox = pygame.Rect(20, 20, 20, 20)
        self.assertEqual(self.movement_handler.handle_movement(keys, player_x, player_hitbox), 20)


class TestGameObjectFactory(unittest.TestCase):
    def test_create_falling_object(self):
        falling_object = GameObjectFactory.create_falling_object([800, 600])
        self.assertIsInstance(falling_object, FallingObject)
        self.assertEqual(falling_object.x, falling_object.x)
        self.assertEqual(falling_object.y, falling_object.y)
        self.assertIn(falling_object, falling_object.falling_objects)


class TestFallingObject(unittest.TestCase):
    def setUp(self):
        self.falling_object = FallingObject([800, 600])

    @patch('pygame.draw.rect')
    def test_spawn_obj(self, mock_draw_rect):
        surface = pygame.Surface((800, 600))
        color = (255, 255, 255)
        self.assertIsInstance(self.falling_object.spawn_obj(surface, color), pygame.Rect)
        mock_draw_rect.assert_called()

    def test_update_position(self):
        speed = 5
        self.falling_object.update_position(speed)
        self.assertEqual(self.falling_object.y, speed)


if __name__ == '__main__':
    unittest.main()


