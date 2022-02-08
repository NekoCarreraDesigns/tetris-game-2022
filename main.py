import pygame
import random

pygame.font.init()

s_width = 800
s_height = 700
play_width = 300
play_height = 600
block = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

shapes = [
    [[1, 5, 9,  13], [4, 5, 6, 7]],
    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
    [[1, 4, 5, 6, ], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    [[1, 2, 5, 6]]
]

shape_colors = [(235, 153, 23), (255, 0, 0), (0, 255, 255),
                (11, 123, 15), (0, 0, 255), (145, 45, 100)]


class Piece(object):
    rows = 20
    columns = 10

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shape.index(shape)]
        self.rotation = 0
