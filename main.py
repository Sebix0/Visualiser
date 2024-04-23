import pygame, sys
from StateManager import StateManager
import startMenu, dfs, bfs, selectionMenu
from settings import *



class Game:
  def __init__(self):
    pygame.init()

    self.win = pygame.display.set_mode((winWidth, winHeight))
    self.Clock = pygame.time.Clock()

    self.stateManager = StateManager('startMenu')
    self.startMenu = startMenu.Start(self.stateManager)
    self.selectionMenu = selectionMenu.Menu(self.stateManager)
    self.BFS = bfs.BFS(self.stateManager)
    self.DFS = dfs.DFS(self.stateManager)
    self.states = {
      'startMenu': self.startMenu,
      'selectionMenu': self.selectionMenu,
      'BFS': self.BFS,
      'DFS': self.DFS
    }

  def run(self):
    for event in pygame.event.get():
      self.Clock.tick(FPS)
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      
      self.states[self.stateManager.getState()].eventHandler(event)
    self.states[self.stateManager.getState()].logic()

    self.states[self.stateManager.getState()].draw(self.win)
    pygame.display.update()
  

if __name__ == "__main__":
  game = Game()
  while True:
    game.run()


