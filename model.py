class Model:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for x in range(self.cols)] for y in range(self.rows)]

    def player_click(self, row, col, player):
        if row < len(self.data) and col < len(self.data[0]):
            if self.data[row][col] == 0:
                self.data[row][col] = player
                return 1
        else:
            return 0

    def get(self, row, col):
        return self.data[row][col]