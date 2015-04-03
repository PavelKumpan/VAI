class CostFunction:

    def __init__(self):
        self.last = -1
        self.defaultCost = 2
        self.agresivity = 4 # 1 - 10
        self.agresivityLimit = 10
        self.stepWeight = 2

    def cellCost(self, cell, player):
        print(cell)
        if cell == 0:
            return 0
        if cell == player:
            return self.defaultCost
        else:
            return -1 * self.defaultCost
        return 0

    def cost(self, playground, row, col, n, player):
        if playground[row][col] != 0:           # in case of this cell is not empty
            return 0

        width = len(playground[0])
        height = len(playground)
        cost = 0

        print(playground)
        k = 0

        for i in range(col - 1, max(col - n, -1), -1): # left
            cell = playground[row][i]
            c = self.cellCost(cell, player)
            cost += c + k
            k += self.stepWeight
            if c <= 0:
                break
        k = 0

        for i in range(col + 1, min(col + n, width)): # right
            cell = playground[row][i]
            c = self.cellCost(cell, player)
            cost += c + k
            k += self.stepWeight
            if c <= 0:
                break
        k = 0

        for j in range(row - 1, max(row - n, -1), -1): # up
            cell = playground[j][col]
            c = self.cellCost(cell, player)
            cost += c + k
            k += self.stepWeight
            if c <= 0:
                break
        k = 0

        for j in range(row + 1, min(row + n, height)): # down
            cell = playground[j][col]
            c = self.cellCost(cell, player)
            cost += c + k
            k += self.stepWeight
            if c <= 0:
                break
        k = 0

        for i in range(1, n):   # left down
            if (col - i) < 0 or (row + i) >= height:
                break
            cell = playground[row + i][col - i]
            c = self.cellCost(cell, player)
            cost += c + k
            k += self.stepWeight
            if c <= 0:
                break
        k = 0

        for i in range(1, n):   # right down
            if (col + i) >= width or (row + i) >= height:
                break
            cell = playground[row + i][col + i]
            c = self.cellCost(cell, player)
            cost += c + k
            k += self.stepWeight
            if c <= 0:
                break
        k = 0

        for i in range(1, n):   # left up
            if (col - i) < 0 or (row - i) < 0:
                break
            cell = playground[row - i][col - i]
            c = self.cellCost(cell, player)
            cost += c + k
            k += self.stepWeight
            if c <= 0:
                break
        k = 0

        for i in range(1, n):   # right up
            if (row - i) < 0 or (col + i) >= width:
                break
            cell = playground[row - i][col + i]
            c = self.cellCost(cell, player)
            cost += c + k
            k += self.stepWeight
            if c <= 0:
                break

        return cost

    def evaluate(self, playground, n, player):

        width = len(playground[0])
        height = len(playground)
        costMatrix = [[0 for x in range(width)] for y in range(height)]

        for i in range(0, height):
            for j in range(0, width):
                costMatrix[i][j] =  self.agresivity * self.cost(playground, i, j, n, player) + (self.agresivityLimit - self.agresivity) * self.cost(playground, i, j, n, 2 - (player + 1) % 2)

        return costMatrix


    def test(self, playground, n):
        '''
        Check if one of players has N marks in one line
        :type playground: list
        :type n: int
        '''
        rating = 0
        winPlayerA = 2**16
        winPlayerB = -2**16
        playerA = 0
        playerB = 0

        height = len(playground)
        width = len(playground[0])

        # horizontal searching
        for i in range(0, height):
            for j in range(0, width):
                if playground[i][j] == 1:   # player A has this cell
                    playerA += 1
                    playerB = 0
                elif playground[i][j] == 2:
                    playerA = 0
                    playerB += 1
                else:
                    playerA = 0
                    playerB = 0

                if playerA >= n:
                    return winPlayerA
                elif playerB >= n:
                    return winPlayerB

            playerB = 0
            playerA = 0

        self.previous = [-1]

        # vertical searching
        for j in range(0, width):
            for i in range(0, height):
                if playground[i][j] == 1:   # player A has this cell
                    playerA += 1
                    playerB = 0
                elif playground[i][j] == 2:
                    playerA = 0
                    playerB += 1
                else:
                    playerA = 0
                    playerB = 0

                if playerA >= n:
                    return winPlayerA
                elif playerB >= n:
                    return winPlayerB

            playerB = 0
            playerA = 0

        self.previous = [-1]

        # diagonal searching
        for i in range(0, height * 2):
            for j in range(i, -1, -1):
                r = i - j
                c = j
                if r >= height or c >= width:
                    continue
                if playground[r][c] == 1:   # player A has this cell
                    playerA += 1
                    playerB = 0
                elif playground[r][c] == 2:
                    playerA = 0
                    playerB += 1
                else:
                    playerA = 0
                    playerB = 0

                if playerA >= n:
                    return winPlayerA
                elif playerB >= n:
                    return winPlayerB

            playerB = 0
            playerA = 0

        self.previous = [-1]

        # diagonal searching
        for i in range(0, height * 2):
            for j in range(width - 1 - i, width - 1):
                r = i - (width - 1 - j)
                c = j
                if r >= height or c >= width:
                    continue

                if playground[r][c] == 1:   # player A has this cell
                    playerA += 1
                    playerB = 0
                elif playground[r][c] == 2:
                    playerA = 0
                    playerB += 1
                else:
                    playerA = 0
                    playerB = 0

                if playerA >= n:
                    return winPlayerA
                elif playerB >= n:
                    return winPlayerB

            playerB = 0
            playerA = 0

        return rating