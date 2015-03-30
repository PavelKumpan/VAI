import node
import critic

class Intelligence:

    open = []
    closed = []

    def __init__(self):
        self.critic = critic.Critic()

    def expand(self, graph):
        pass

    def alphabeta(self, alpha, beta, node):
        '''
        :type node node.Node
        '''
        if node.level == 0:
            alpha = 2**15
            beta = -2**15

        if len(node.descendants) == 0:  # leaf
            return self.rating(node.state)

        i = 0
        all = []

        for i in range(0, len(node.descendants)):
            alpha = max(alpha, max(all))
            beta = min(beta, min(all))
            all.append(self.alphabeta(alpha, beta, node.descendants[i]))

            if beta > alpha and node.type == 'OR':
                return alpha
            elif beta < alpha and node.type == 'AND':
                return beta

        return alpha if (node.type == 'OR') else beta

    def testPlayState(self, playState, n):
        minX = 2**15
        minY = 2**15
        maxX = 0
        maxY = 0

        for cell in playState:
            minX = min(minX, cell[0])
            minY = min(minY, cell[1])
            maxX = max(maxX, cell[0])
            maxY = max(maxY, cell[1])

        minX = min(minX - 2, 0)
        minY = min(minY - 2, 0)
        minX = min(minX + 2, 0)
        minY = min(minY + 2, 0)

        width = maxX - minX + 1
        height = maxY - minY + 1

        width = max(width, height)
        height = max(width, height)

        playground = [[0 for x in range(width)] for y in range(height)]

        for cell in playState:
            playground[cell[0] - minX][cell[1] - minY] = cell[2]

        return self.critic.test(playground, n)