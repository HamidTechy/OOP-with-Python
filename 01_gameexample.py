class Remote:

    def isleftpressed(self):
        pass


class Player:

    def moveleft(self):
        pass

    def moveright(self):
        pass

    def moveforward(self):
        pass

    def movebackward(self):
        pass


remote1 = Remote()
player1 = Player()
if remote1.isleftpressed():
    player1.moveleft()
