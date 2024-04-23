import pygame
from settings import *

class Heading:
  def __init__(self, text, pos, size, textSize=128, textColor=(0,0,0), bgColor=None):
    self.text = text
    self.size = size
    self.pos = pos
    self.textColor = textColor
    self.bgColor = bgColor
    self.font = pygame.font.SysFont('roboto', textSize)
    self.fontSurface = self.font.render(self.text, False, self.textColor)
    self.rect = pygame.Rect(self.pos, self.size)

  def drawHeading(self, win):
    if self.bgColor != None:
      pygame.draw.rect(win, self.bgColor, self.rect)
    win.blit(self.fontSurface, (self.rect.x + self.rect.width//2 - self.fontSurface.get_width()//2, self.rect.y + self.rect.height//2 - self.fontSurface.get_height()//2))

  def changeText(self, text):
    self.text = text
    self.fontSurface = self.font.render(self.text, False, self.textColor)

  def changeFontSize(self, size):
    self.font = pygame.font.SysFont('roboto', size)
    self.changeText(self.text)

  def onClick(self, event):
    if event.type == pygame.MOUSEBUTTONUP:
      return self.hover()

  def hover(self):
    mousePos = pygame.mouse.get_pos()
    if self.rect.collidepoint(mousePos):
      return True

  def centerX(self):
    self.pos = (winWidth//2 - self.size[0]//2 , self.pos[1])
    self.rect.topleft = self.pos
    print(self.pos)
    print(self.fontSurface.get_rect().topleft)

  def centerY(self):
    self.pos = (self.pos[0], winHeight//2 - self.size[1]//2)
    self.rect.topleft = self.pos
    print(self.pos)
    print(self.fontSurface.get_rect().topleft)

  def center(self):
    self.centerX()
    self.centerY()
