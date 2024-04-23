import pygame, sys
import heading
from settings import *

class Start: # do this first
  def __init__(self, stateManager):
    self.stateManager = stateManager

    self.title = heading.Heading("Visualiser", (116, 0), (768, 256))
    self.startButton = heading.Heading("Start", (308, 280), (384, 192), textColor=(0, 255, 200), bgColor=(50, 200, 50))
    self.quitButton = heading.Heading("Quit", (308, 540), (384, 192), textColor=(200, 50, 50), bgColor=(255, 100, 100))
  

  def logic(self):
    if self.startButton.hover():
      if self.startButton.bgColor != (255, 193, 7):
        self.startButton.bgColor = (255, 193, 7)
    else:
      if self.startButton.bgColor == (255, 193, 7):
        self.startButton.bgColor = (50, 200, 50)
    if self.quitButton.hover():
      if self.quitButton.bgColor != (255, 34, 34):
        self.quitButton.bgColor = (255, 34, 34)
    else:
      if self.quitButton.bgColor == (255, 34, 34):
        self.quitButton.bgColor = (255, 100, 100)

  def eventHandler(self, event):
    if self.quitButton.onClick(event):
      pygame.quit()
      sys.exit()
    
    if self.startButton.onClick(event):
      self.stateManager.setState('selectionMenu')

  def draw(self, win):
    win.fill((200, 200, 200))
    self.title.drawHeading(win)
    self.startButton.drawHeading(win)
    self.quitButton.drawHeading(win)