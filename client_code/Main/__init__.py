from ._anvil_designer import MainTemplate #type: ignore
from anvil import *

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
  
  