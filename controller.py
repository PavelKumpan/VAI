import opponent
import intelligence

class Controller:

    intelligence

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.opponent = opponent.Opponent()
        self.intelligence = intelligence.Intelligence()

        self.player = []

    def click(self, x, y, player):
        self.model.player_click(x, y, player)
        self.view.render(self.model.data)
        self.player.append((x, y, player))

        print(self.intelligence.testPlayState(self.player, 5))