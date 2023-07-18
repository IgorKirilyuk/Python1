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
        self.lives = 20
        self.maxlives = 20

    def print_stats(self):
        print('🍺:', self.tank, '/', self.maxtank, sep='', end=' | ')
        print('🏆:', self.score, sep='', end=' | ')
        print('❤️:', self.lives, sep='')

    def move(self, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < self.h and 0 <= ny < self.w:
            self.x, self.y = nx, ny

    def export_data(self):
        return {"score": self.score,
                "lives": self.lives, "maxlives": self.maxlives,
                "x": self.x, "y": self.y,
                "tank": self.tank, "maxtank": self.maxtank}

    def import_data(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 0
        self.maxtank = data["maxtank"] or 1
        self.score = data["score"] or 0
        self.lives = data["lives"] or 20
        self.maxlives = data["maxlives"] or 20

