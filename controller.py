import intelligence
import costfunction

class Controller:

    intelligence

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.intelligence = intelligence.Intelligence()
        self.costFunction = costfunction.CostFunction()
        self.player = []

    def click(self, row, col, player):
        self.model.player_click(row, col, player)
        costs = self.costFunction.evaluate(self.model.data, 5, 2 - (player + 1) % 2)
        self.view.render(self.model.data, costs)
        self.player.append((row, col, player))
