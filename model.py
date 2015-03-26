class Model:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for x in range(self.cols)] for y in range(self.rows)]

    def player_click(self, x, y, player):
        if x < len(self.data) and y < len(self.data[0]):
            if self.data[x][y] == 0:
                self.data[x][y] = player
                return 1
        else:
            return 0

    def get(self, x, y):
        return self.data[x][y]