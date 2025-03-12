from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        grassBlock = loader.loadModel('assets/grass-block.glb')
        grassBlock.reparentTo(render)

game = Game()
game.run()
