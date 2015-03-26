import  opponent



class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.opponent = opponent.Opponent()


    def click(self, x, y, player):
        if self.model.player_click(x, y, player):
            self.view.render(self.model.data)

            if player == 1:
                m = self.opponent.move()
                print(m)
                self.click(m[0], m[1], 2)