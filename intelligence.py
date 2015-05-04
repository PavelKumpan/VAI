import costfunction
import copy

class Intelligence:
    open = []
    closed = []

    def __init__(self, goal = 5):
        self.cost_function = costfunction.CostFunction()
        self.goal = goal
        self.depth = 3

    def cell_test(self, grid, row, col, width, height):
        if grid[row][col] != 0:
            return False


        neighborhood = grid[min(row + 1, height-1)][min(col + 1, width-1)] + \
                       grid[min(row + 1, height-1)][col] + \
                       grid[min(row + 1, height-1)][max(col - 1, 0)] + \
                       grid[row][max(col - 1, 0)] + \
                       grid[row][min(col + 1, width-1)] + \
                       grid[max(row - 1, 0)][min(col + 1, width-1)] + \
                       grid[max(row - 1, 0)][col] + \
                       grid[max(row - 1, 0)][max(col - 1, 0)]

        return not neighborhood == 0

    def step(self, grid, player, level, alpha, beta):
        width = len(grid[0])
        height = len(grid)
        move = None
        cut = False
        v = (-1)**player * 2**16

        for row in range(0, height):
            for col in range(0, width):
                if not self.cell_test(grid, row, col, width, height):
                    continue

                v = self.cost_function.cost(grid, row, col, self.goal, player) * (-1)**(player+1)
                if level < self.depth:
                    grid[row][col] = player
                    v += self.step(grid, 1 + (player % 2), level+1, alpha, beta)
                    grid[row][col] = 0


                if player == 1:    # maximizer
                    if v > alpha:
                        alpha = v
                        move = (row, col)
                else:              # minimizer
                    if v < beta:
                        beta = v
                        move = (row, col)

                if alpha > beta:
                    cut = True
                    break
                ############
            if cut:
                break

        if level == 1:
            return move
        else:
            return v

    def alpha_beta(self, grid, player):
        return self.step(grid, player, 1, -1 * 2**16, 2**16)