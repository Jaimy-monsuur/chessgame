import pygame
from enum import Enum
from pygame import color


class Colors(Enum):
    White = 1
    Black = 2


class Pieces(Enum):
    Pawn = 1
    Bishop = 2
    Knight = 3
    Rook = 4
    Queen = 5
    King = 6


class Piece():
    rank = ""

    def __init__(self, color, position):
        self.coords = None
        self.pic = None
        self.color = color
        self.set_coords(position)

    def set_coords(self, pos):

        """Map position of piece to coordinate on the screen"""
        y = pos[0]
        x = pos[1]
        x = (x - 1) * 100
        y = y * 100 - 100

        coords = (int(x), int(y))
        self.coords = coords

    def GetPic(self):
        if self.color == Colors.White:
            if self.rank == Pieces.Pawn:
                self.pic = pygame.image.load('pieces_pics\wp.png')
            elif self.rank == Pieces.Bishop:
                self.pic = pygame.image.load('pieces_pics\wb.png')
            elif self.rank == Pieces.Knight:
                self.pic = pygame.image.load('pieces_pics\wn.png')
            elif self.rank == Pieces.Rook:
                self.pic = pygame.image.load('pieces_pics\wr.png')
            elif self.rank == Pieces.Queen:
                self.pic = pygame.image.load('pieces_pics\wq.png')
            elif self.rank == Pieces.King:
                self.pic = pygame.image.load('pieces_pics\wk.png')
        else:
            if self.rank == Pieces.Pawn:
                self.pic = pygame.image.load('pieces_pics\\bp.png')
            elif self.rank == Pieces.Bishop:
                self.pic = pygame.image.load('pieces_pics\\bb.png')
            elif self.rank == Pieces.Knight:
                self.pic = pygame.image.load('pieces_pics\\bn.png')
            elif self.rank == Pieces.Rook:
                self.pic = pygame.image.load('pieces_pics\\br.png')
            elif self.rank == Pieces.Queen:
                self.pic = pygame.image.load('pieces_pics\\bq.png')
            elif self.rank == Pieces.King:
                self.pic = pygame.image.load('pieces_pics\\bk.png')


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.rank = Pieces.Pawn
        super().GetPic()


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.rank = Pieces.Bishop
        super().GetPic()


class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.rank = Pieces.Knight
        super().GetPic()


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.rank = Pieces.Rook
        super().GetPic()


class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.rank = Pieces.Queen
        super().GetPic()


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.rank = Pieces.King
        super().GetPic()
