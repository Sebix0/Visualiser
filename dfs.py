import pygame, Grid
from settings import *

class DFS: # do this after start menu
  def __init__(self, stateManager):
    self.stateManager = stateManager

    self.Grid = Grid.Grid(1000, 1000, cellSize)
    self.visited = []
    self.stack = []


  def logic(self):
    pass

  def eventHandler(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        self.stateManager.setState(self.stateManager.prevState)
    

  def draw(self, win):
    win.fill((220, 220, 220))
    self.Grid.draw(win, (50, 50, 50))