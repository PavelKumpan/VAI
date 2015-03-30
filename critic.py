class Critic:

    def __init__(self):
        self.previous = [-1]

    def rate(self, actual, endl):
        '''

        '''

        val = 0

        if len(self.previous) >= 2:
            self.previous.pop(0)
        self.previous.append(actual)

        if actual != 0:
            val = 10

            for i in range(len(self.previous) -1, -1, -1):
                if self.previous[i] == actual:
                    val *= 4
                elif self.previous[i] == 0:
                    pass
                elif self.previous[i] == -1:
                    val //= 2
                else:
                    val //= 8

        if actual == 2:
            val *= -1

        if endl == True:
            self.previous = [-1]

        return val

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

                rating += self.rate(playground[i][j], j == width)

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

                rating += self.rate(playground[i][j], i == height)

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

                rating += self.rate(playground[r][c], j == 0)

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

                rating += self.rate(playground[r][c], j == width - 2)

            playerB = 0
            playerA = 0

        return rating