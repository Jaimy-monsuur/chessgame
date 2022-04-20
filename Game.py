import pygame
import pygame.display as ui
from ChessBoard import *

# defines the width and height of the display
display_width = 800
display_height = 800


class ChessGame():
    def __init__(self):
        self.GameBoard = None
        self.square = None
        self.Selected_Tile = None

    def Start(self):
        """starts the game"""
        pygame.init()

        # Set up the drawing window
        game_display = pygame.display.set_mode((display_width, display_height))
        ui.update()
        self.GameBoard = Board(game_display)
        # Run until the user asks to quit
        running = True
        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.square is not None:
                        snd = self.GameBoard.GetTile(pos)
                        print(snd, "snd")
                        snd = self.square
                        self.square = None
                    else:
                        self.square = self.GameBoard.GetTile(pos)
                    if self.square is not None:
                        print(self.square.rank, self.square.color)

            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()
