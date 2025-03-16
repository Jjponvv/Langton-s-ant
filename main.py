import pygame as pg
import numpy as np
import random as r

GRID_SIZE = 101
CELL_SIZE = 10
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

FPS = 1000

DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

class Ant:
    def __init__(self):
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        self.x, self.y = r.randint(0, GRID_SIZE-1), r.randint(0, GRID_SIZE-1)
        self.dir = r.randint(0, 3)
        self.color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))

    def move(self):
        self.grid[self.x, self.y] = 1 - self.grid[self.x, self.y]

        if self.grid[self.x, self.y] == 1:
            self.dir = (self.dir - 1) % 4
        else:
            self.dir = (self.dir + 1) % 4

        self.dx, self.dy = DIRECTIONS[self.dir]

        self.x = (self.x + self.dx) % GRID_SIZE
        self.y = (self.y + self.dy) % GRID_SIZE

pg.init()

sc = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pg.display.set_caption("Langton's ant 🐜")
clock = pg.time.Clock()

ants = [Ant() for _ in range(10)]

run = True
while run:
    clock.tick(FPS)
    sc.fill((0, 0, 0))
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

    for i in ants:
        i.move()

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            for i in ants:
                if i.grid[x, y] == 1:
                    pg.draw.rect(sc, i.color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pg.display.flip()
    