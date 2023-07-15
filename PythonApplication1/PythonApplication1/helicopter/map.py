from utils import randbool
from utils import randcell
from utils import randcell2
import os

#	 💩👺🔥😏🗿🦔🌪️🌩️☁️⛈️
# 0-pole 🌼--🌿
# 1-derevo 🌳
# 2-reka 🌊
# 3-hosp 🏥Ы
# 4-upgrade 🛠️
# 5-fire 🔥

CELL_TYPES = "🌼🌳🌊🏥🛠🔥"
TREE_BONUS = 100
HELICO_MAX_TUNK = 3
HELICO_TUNK_PRICE = 500
HELICO_LIVE_PRICE = 500


class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generate_forest(3, 20)
        self.generate_river(3)
        self.generate_river(3)
        self.generate_shop()
        self.generate_hosp()

    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

    def print_map(self, helico, clouds):
        print("🟦" * (self.w + 1))  # 🟩
        for ri in range(self.h):
            print("🟦", end='')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if clouds.cells[ri][ci] == 1:
                    print("☁️", end='')
                elif clouds.cells[ri][ci] == 2:
                    print("🌩️", end='')
                elif helico.x == ri and helico.y == ci:
                    print("🦔", end='')
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end='')
            print("🟦")
        print("🟦" * (self.w + 1))  # 🟩

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_river(self, l):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1

    def generate_shop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def generate_hosp(self):
        while True:
            c = randcell(self.w, self.h)
            cx, cy = c[0], c[1]
            if self.cells[cx][cy] == 0:
                self.cells[cx][cy] = 3
                return

    def add_fire(self):
        f = randcell(self.w, self.h)
        # print(rc)
        fx, fy = f[0], f[1]
        if self.check_bounds(fx, fy) and self.cells[fx][fy] == 1:
            self.cells[fx][fy] = 5
        return self.cells[fx][fy] == 5

    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(5):
            self.add_fire()

    def process_helico(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if c == 2:
            helico.tank = helico.maxtank
        if c == 5 and helico.tank > 0:
            self.cells[helico.x][helico.y] = 1
            helico.tank -= 1
            helico.score += TREE_BONUS
        if c == 4 and helico.maxtank < HELICO_MAX_TUNK and helico.score >= HELICO_TUNK_PRICE:
            helico.maxtank += 1
            helico.score -= HELICO_TUNK_PRICE
        if c == 3 and helico.lives < helico.maxlives and helico.score >= HELICO_LIVE_PRICE:
            helico.lives += 10
            helico.score -= HELICO_TUNK_PRICE
        if d == 2 and helico.lives > 0:
            helico.lives -= 1
            if helico.lives == 0:
                os.system('cls')
                print("GAME OVER, YOU SCORE:", helico.score)
                exit(0)