from Pieces import *
from itertools import product
import pygame.display as ui

# defines block width and height
block_height = 100
block_width = 100

# defines colours
Dark = (125, 135, 150)
Light = (232, 235, 239)


class Tile():
    """A spot on the board"""

    def __init__(self, game_display, x, y):
        self.game_display = game_display
        self.x = x
        self.y = y

    def Draw(self):
        if self.x % 2 == self.y % 2:
            pygame.draw.rect(self.game_display, Light, (self.x * 100, self.y * 100, block_width, block_height))
        elif self.x % 2 != self.y % 2:
            pygame.draw.rect(self.game_display, Dark, (self.x * 100, self.y * 100, block_width, block_height))


class Board():
    def __init__(self, game_display):
        self.board = dict()
        self.game_display = game_display
        p = Piece
        for x in range(9):
            for y in range(9):
                newspot = Tile(self.game_display, x, y)
                newspot.Draw()
        ui.update()
        self.DrawFirstTime()
        ui.update()

    def DrawFirstTime(self):
        for c in range(9):
            for r in range(9):
                self.board[(c, r)] = None

        for column in range(8):
            self.board[(2, column + 1)] = Pawn(Colors.White, position=(2, column + 1))
            self.board[(7, column + 1)] = Pawn(Colors.Black, position=(7, column + 1))

        self.board[(1, 1)] = Rook(Colors.White, position=(1, 1))
        self.board[(1, 8)] = Rook(Colors.White, position=(1, 8))
        self.board[(8, 1)] = Rook(Colors.Black, position=(8, 1))
        self.board[(8, 8)] = Rook(Colors.Black, position=(8, 8))

        self.board[(1, 2)] = Knight(Colors.White, position=(1, 2))
        self.board[(1, 7)] = Knight(Colors.White, position=(1, 7))
        self.board[(8, 2)] = Knight(Colors.Black, position=(8, 2))
        self.board[(8, 7)] = Knight(Colors.Black, position=(8, 7))

        self.board[(1, 3)] = Bishop(Colors.White, position=(1, 3))
        self.board[(1, 6)] = Bishop(Colors.White, position=(1, 6))
        self.board[(8, 3)] = Bishop(Colors.Black, position=(8, 3))
        self.board[(8, 6)] = Bishop(Colors.Black, position=(8, 6))

        self.board[(1, 4)] = Queen(Colors.White, position=(1, 4))
        self.board[(8, 4)] = Queen(Colors.Black, position=(8, 4))

        self.board[(1, 5)] = King(Colors.White, position=(1, 5))
        self.board[(8, 5)] = King(Colors.Black, position=(8, 5))

        for square in self.board:
            if self.board[square] is None:
                pass
            else:
                piece = self.board[square]
                image = pygame.transform.scale(piece.pic, (100, 100))
                self.game_display.blit(image, piece.coords)

    def GetTile(self, pos) -> Piece:
        if pos[0] < 100 and pos[1] < 100:
            y = 1
            x = 1
        elif pos[0] < 100 and pos[1] > 100:
            y = 1
            x = int(str(pos[1])[:1]) + 1
        elif pos[0] > 100 and pos[1] < 100:
            y = int(str(pos[0])[:1]) + 1
            x = 1
        else:
            y = int(str(pos[0])[:1]) + 1
            x = int(str(pos[1])[:1]) + 1

        return self.board[(x, y)]

    def GetTileXY(self, x, y) -> Piece:
        return self.board[(x, y)]
