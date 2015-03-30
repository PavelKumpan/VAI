class Intelligence:

    open = []
    closed = []

    def __init__(self):
        pass

    def expand(self, graph):
        pass

    '''
    Alpha-Beta tree prunning
    '''
    def prunning(self, alpha, beta, graph):
        pass

    def test(self, playground, n):
        '''
        Check if one of players has N marks in one line
        :type playground: list
        :type n: int
        '''

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

                if playerA >= n:
                    return 1
                elif playerB >= n:
                    return 2

            playerB = 0
            playerA = 0

        # vertical searching
        for j in range(0, width):
            for i in range(0, height):
                if playground[i][j] == 1:   # player A has this cell
                    playerA += 1
                    playerB = 0
                elif playground[i][j] == 2:
                    playerA = 0
                    playerB += 1

                if playerA >= n:
                    return 1
                elif playerB >= n:
                    return 2

            playerB = 0
            playerA = 0

        # diagonal searching
        for i in range(0, height):
            for j in range(i, -1, -1):

                if playground[i - j][j] == 1:   # player A has this cell
                    playerA += 1
                    playerB = 0
                elif playground[i - j][j] == 2:
                    playerA = 0
                    playerB += 1

                if playerA >= n:
                    return 1
                elif playerB >= n:
                    return 2

            playerB = 0
            playerA = 0

        # diagonal searching
        for i in range(0, height):
            for j in range(width - 1 - i, width - 1):
                if playground[i - (width - 1 - j)][j] == 1:   # player A has this cell
                    playerA += 1
                    playerB = 0
                elif playground[i - (width - 1 - j)][j] == 2:
                    playerA = 0
                    playerB += 1

                if playerA >= n:
                    return 1
                elif playerB >= n:
                    return 2

            playerB = 0
            playerA = 0

        return 0