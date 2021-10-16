from ._anvil_designer import MainTemplate #type: ignore
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import Game, AI

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

  def displayBoard(self):
    # Display the cells in the grid
    for row in range(self.GAME_SIZE):
        for col in range(self.GAME_SIZE):
          self.buttonGrid[row][col].text = str(Game.board[row][col]) if Game.board[row][col] else ''
    
    # Disply the updated score
    self.scoreLabel.text = f'Score: {Game.score}'
  
  def runGame(self, playerIsHuman):
    Game.addNewNum(Game.board, False)
    Game.addNewNum(Game.board, True)
    if not playerIsHuman:
      AI.startAI()
  
  def keypress(self, key):
    global gameOver, board, score
    # Called when a key is pressed
    # Don't do anything if the game is over
    if Game.gameOver or key not in Game.KEY_FUNCTIONS:
        return

    # Call the function corresponding to the key
    Game.board, Game.score, Game.flag = Game.KEY_FUNCTIONS[key](Game.board, Game.score)
    if Game.flag:
        Game.addNewNum(Game.board, True)
        Game.checkGameOver(Game.board)

  def onStartClick(self, **event_args):
    """This method is called when the button is clicked"""
    self.runGame(not self.botCheckBox.checked)

