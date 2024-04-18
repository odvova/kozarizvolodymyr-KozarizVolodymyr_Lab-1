import sys
import pygame

WHITE = (233, 229, 0)


class DeathMenu:
    """
    A class to represent the death menu.

    Attributes
    ----------
    surface : pygame.Surface
        The surface to draw the death menu on.
    width : int
        The width of the surface.
    height : int
        The height of the surface.
    font : pygame.font.Font
        The font used to render the text.
    menu_font : pygame.font.Font
        The font used to render the menu text.

    Methods
    -------
    run()
        Run the death menu.
    """
    def __init__(self, surface) -> None:
        self.surface = surface
        self.width, self.height = pygame.display.get_surface().get_size()
        self.font = pygame.font.Font('Images/Backgrounds/RetroGamingFont.ttf', 48)
        self.menu_font = pygame.font.Font('Images/Backgrounds/RetroGamingFont.ttf', 36)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return  # Restart game

            self.surface.fill((0, 0, 0))
            text = self.font.render("You died!", True, WHITE)
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2 - 50))
            self.surface.blit(text, text_rect)
            menu_text = self.menu_font.render("Press 'r' to restart", True, WHITE)
            menu_text_rect = menu_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
            self.surface.blit(menu_text, menu_text_rect)
            pygame.display.update()


