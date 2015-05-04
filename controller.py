import intelligence
import costfunction

class Controller:

    intelligence

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.intelligence = intelligence.Intelligence()
        self.cost_function = costfunction.CostFunction()

    def winner_test(self, test):
        if test['winner'] != 0:
            if self.view.end():
                self.view.close()
                quit()
            else:
                self.model.clear()
                self.view.clear()
                if self.view.player == 2:
                    self.click(None, None, 2)
                return 1
        return 0

    def click(self, row, col, player):
        if self.model.player_click(row, col, player) != 1:
            return

        test = self.cost_function.test(self.model.data, 5)
        self.view.render(self.model.data, self.model.data, test['cells'])

        if self.winner_test(test) == 1:
            return

        player = 1 + (player % 2)

        costs = self.cost_function.evaluate(self.model.data, 5, player)
        row_col = self.intelligence.alpha_beta(self.model.data, player)
        if not isinstance(row_col, tuple):
            row_col = (4, 7)
        self.model.player_click(row_col[0], row_col[1], player)
        test = self.cost_function.test(self.model.data, 5)
        self.view.render(self.model.data, costs, test["cells"])

        self.winner_test(test)



