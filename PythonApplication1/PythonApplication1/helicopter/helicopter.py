from utils import randcell

class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        print(rc)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.w = w
        self.h = h
        self.maxtank = 1
        self.tank = 0
        self.score = 0

    def print_stats(self):
        print('🍺:', self.tank, '/', self.maxtank, sep='', end=' | ')
        print('🏆:' , self.score, sep='')
    def move(self, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < self.h and 0 <= ny < self.w:
            self.x, self.y = nx, ny


