import pygame

from const import *
from board import Board
from dragger import Dragger

class Game:
    
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
    #Show Methods
    
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row + col)%2 == 0:
                    color = (234, 235, 200) #Light Green
                else:
                    color = (119, 154, 88)    #Dark Green
                    
                rec = (col * SQRSZ, row * SQRSZ, SQRSZ, SQRSZ)    
                pygame.draw.rect(surface, color, rec)
                
                
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLUMNS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQRSZ + SQRSZ // 2, row * SQRSZ + SQRSZ //2
                    
                        piece.texture_rec = img.get_rect(center = img_center)
                        surface.blit(img, piece.texture_rec)
    
    
    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
             
            for move in piece.moves:
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                
                
                
                
                
                
                
                        