from ._anvil_designer import MainTemplate #type: ignore
from anvil import *
import Game

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.GAME_SIZE = 4
    self.buttonGrid = []
    for i in range(self.GAME_SIZE):
      self.buttonGrid.append([])
      for j in range(self.GAME_SIZE):
        self.buttonGrid[i].append(getattr(self, f'button{i}{j}'))
        self.buttonGrid[i][j].text = ' '
    
    Game.displayBoard = self.displayBoard
    self.runGame(not self.botCheckBox.checked)

  def displayBoard(self):
    # Display the cells in the grid
    for row in range(self.GAME_SIZE):
        for col in range(self.GAME_SIZE):
            self.buttonGrid[row][col].text = str(Game.board[row][col]) if Game.board[row][col] else ''
    
    # Disply the updated score
    #scoreLabel.configure(text = f'Score: {score}')
  
  def runGame(self, playerIsHuman):
    Game.addNewNum(Game.board, False)
    Game.addNewNum(Game.board, True)