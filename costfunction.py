from random import random


class CostFunction:
    def __init__(self):
        self.last = 0
        self.score = {
            'opponentEnd': 5,
            'emptyEnd': 10,
            'default': 15,
            'line': 20,
            'stepIncrement': 3}
        self.aggressiveness = 0.3 # 1 - 10
        self.player_wins = 2**16
        self.in_line_a = 0
        self.in_line_b = 0
        self.neighbor = 0

    def dirCost(self, rows, cols, grid, player, n):
        cost = 0
        k = 1

        if len(rows) == 0 or len(cols) == 0:
            return 0

        self.neighbor = grid[rows[0]][cols[0]]
        if self.neighbor != 0:
            for i in range(0, min(len(rows), len(cols))):
                cell = grid[rows[i]][cols[i]]

                if cell != self.neighbor:
                    if cell == 0:
                        cost += self.score['emptyEnd']
                    else:
                        cost += self.score['opponentEnd']
                    break
                else:
                    cost += k * self.score['default']

                if cell == player:
                    self.in_line_a += 1
                elif cell != 0:
                    self.in_line_b += 1

                k *= self.score['stepIncrement']

        if self.neighbor == player:
            cost *= self.aggressiveness
        else:
            cost *= (1 - self.aggressiveness)
        if cost is None:
            cost = 0
        return cost

    def cost(self, grid, row, col, n, player):
        if grid[row][col] != 0:           # in case of this cell is not empty
            return 0
        last = 0
        width = len(grid[0])
        height = len(grid)
        cost = 0
        self.in_line_a = 0
        self.in_line_b = 0

        #####----------------------------------------------------

        cols = range(col - 1, max(col - n, -1), -1)     # left
        rows = [row for i in range(len(cols))]
        cost += self.dirCost(rows, cols, grid, player, n)

        cols = range(col + 1, min(col + n, width))      # right
        rows = [row for i in range(len(cols))]
        cost += self.dirCost(rows, cols, grid, player, n)

        if max(self.in_line_a + 1, self.in_line_b + 1) >= n :
            return self.player_wins
        cost += self.in_line_a * self.aggressiveness * self.score['line']
        cost += self.in_line_a * (1 - self.aggressiveness) * self.score['line']
        self.in_line_a = 0
        self.in_line_b = 0

        #####----------------------------------------------------

        rows = range(row - 1, max(row - n, -1), -1)     # down
        cols = [col for i in range(len(rows))]
        cost += self.dirCost(rows, cols, grid, player, n)

        rows = range(row + 1, min(row + n, height))     # up
        cols = [col for i in range(len(rows))]
        cost += self.dirCost(rows, cols, grid, player, n)

        if max(self.in_line_a + 1, self.in_line_b + 1) >= n :
            return self.player_wins
        cost += self.in_line_a * self.aggressiveness * self.score['line']
        cost += self.in_line_a * (1 - self.aggressiveness) * self.score['line']
        self.in_line_a = 0
        self.in_line_b = 0

        #####----------------------------------------------------

        cols = range(col - 1, max(col - n, -1), -1)     # left
        rows = range(row - 1, max(row - n, -1), -1)     # down
        cost += self.dirCost(rows, cols, grid, player, n)

        cols = range(col + 1, min(col + n, width))      # right
        rows = range(row + 1, min(row + n, height))     # up
        cost += self.dirCost(rows, cols, grid, player, n)

        if max(self.in_line_a + 1, self.in_line_b + 1) >= n :
            return self.player_wins
        cost += self.in_line_a * self.aggressiveness * self.score['line']
        cost += self.in_line_a * (1 - self.aggressiveness) * self.score['line']
        self.in_line_a = 0
        self.in_line_b = 0

        #####----------------------------------------------------

        cols = range(col - 1, max(col - n, -1), -1)     # left
        rows = range(row + 1, min(row + n, height))     # up
        cost += self.dirCost(rows, cols, grid, player, n)

        cols = range(col + 1, min(col + n, width))      # right
        rows = range(row - 1, max(row - n, -1), -1)     # down
        cost += self.dirCost(rows, cols, grid, player, n)

        if max(self.in_line_a + 1, self.in_line_b + 1) >= n :
            return self.player_wins
        cost += self.in_line_a * self.aggressiveness * self.score['line']
        cost += self.in_line_a * (1 - self.aggressiveness) * self.score['line']
        self.in_line_a = 0
        self.in_line_b = 0

        return cost + 1 / (1 + ((row - width / 2)**2 + (col - height / 2)**2)) + random()


    def evaluate(self, grid, n, player):

        width = len(grid[0])
        height = len(grid)
        costMatrix = [[0 for x in range(width)] for y in range(height)]

        for i in range(0, height):
            for j in range(0, width):
                costMatrix[i][j] =  self.cost(grid, i, j, n, player)

        return costMatrix


    def test(self, grid, n):
        '''
        Check if one of players has N marks in one line
        :type grid: list
        :type n: int
        '''
        rating = 0
        winPlayerA = 2**16
        winPlayerB = -2**16
        playerA = 0
        playerB = 0

        height = len(grid)
        width = len(grid[0])

        five_a = []
        five_b = []

        # horizontal searching
        for i in range(0, height):
            for j in range(0, width):
                if grid[i][j] == 1:   # player A has this cell
                    playerA += 1
                    playerB = 0
                    five_b.clear()
                    five_a.append((i, j))
                elif grid[i][j] == 2:
                    playerA = 0
                    playerB += 1
                    five_a.clear()
                    five_b.append((i, j))
                else:
                    playerA = 0
                    playerB = 0
                    five_a.clear()
                    five_b.clear()

                if playerA >= n:
                    return {"winner": 1, "cells": five_a}
                elif playerB >= n:
                    return {"winner": 2, "cells": five_b}

            playerB = 0
            playerA = 0
            five_a.clear()
            five_b.clear()

        self.previous = [-1]

        # vertical searching
        for j in range(0, width):
            for i in range(0, height):
                if grid[i][j] == 1:   # player A has this cell
                    playerA += 1
                    playerB = 0
                    five_b.clear()
                    five_a.append((i, j))
                elif grid[i][j] == 2:
                    playerA = 0
                    playerB += 1
                    five_a.clear()
                    five_b.append((i, j))
                else:
                    playerA = 0
                    playerB = 0
                    five_a.clear()
                    five_b.clear()

                if playerA >= n:
                    return {"winner": 1, "cells": five_a}
                elif playerB >= n:
                    return {"winner": 2, "cells": five_b}

            playerB = 0
            playerA = 0
            five_a.clear()
            five_b.clear()

        self.previous = [-1]

        # diagonal searching
        for i in range(0, height * 2):
            for j in range(i, -1, -1):
                r = i - j
                c = j
                if r >= height or c >= width:
                    continue
                if grid[r][c] == 1:   # player A has this cell
                    playerA += 1
                    playerB = 0
                    five_b.clear()
                    five_a.append((r, c))
                elif grid[r][c] == 2:
                    playerA = 0
                    playerB += 1
                    five_a.clear()
                    five_b.append((r, c))
                else:
                    playerA = 0
                    playerB = 0
                    five_a.clear()
                    five_b.clear()

                if playerA >= n:
                    return {"winner": 1, "cells": five_a}
                elif playerB >= n:
                    return {"winner": 2, "cells": five_b}

            playerB = 0
            playerA = 0
            five_a.clear()
            five_b.clear()

        self.previous = [-1]

        # diagonal searching
        for i in range(0, height * 2):
            for j in range(width - 1 - i, width - 1):
                r = i - (width - 1 - j)
                c = j
                if r >= height or c >= width:
                    continue

                if grid[r][c] == 1:   # player A has this cell
                    playerA += 1
                    playerB = 0
                    five_b.clear()
                    five_a.append((r, c))
                elif grid[r][c] == 2:
                    playerA = 0
                    playerB += 1
                    five_a.clear()
                    five_b.append((r, c))
                else:
                    playerA = 0
                    playerB = 0
                    five_a.clear()
                    five_b.clear()

                if playerA >= n:
                    return {"winner": 1, "cells": five_a}
                elif playerB >= n:
                    return {"winner": 2, "cells": five_b}

            playerB = 0
            playerA = 0
            five_a.clear()
            five_b.clear()

        return {"winner": 0, "cells": []}