#Rectangle class for the squares on the screen
import pygame as pg
import random
import time

WIN_WIDTH = 1200
WIN_HEIGHT = 980

class Rectangle:
    def __init__(self, width = 20, height = 20, colour = (0, 255, 0)):
        self.x = random.randrange(0, WIN_WIDTH)
        self.y = random.randrange(0, WIN_HEIGHT)
        self.width = width
        self.height = height
        self.left = self.x - self.width/2
        self.top = self.y - self.height/2
        self.right = self.x + self.width/2
        self.bottom = self.y + self.height/2
        self.colour = colour
        
    def draw(self, screen):
        pg.draw.rect(screen, self.colour, (self.left, self.top, self.width, self.height))
    
    def collision(self, mouse_pos):
        return (mouse_pos[0] <= self.right and
                mouse_pos[0] >= self.left and
                mouse_pos[1] <= self.bottom and
                mouse_pos[1] >= self.top)


class Timer:
    def __init__(self, positionY = 100):
        self.x = 100
        self.y = positionY
        self.timer_pos = (self.x, self.y)
        self.split_timer_pos = (self.x + 250, self.y)
        self.minutes = 0
        self.seconds = 0
        self.millis = 0
        self.split_minutes = 0
        self.split_seconds = 0
        self.split_millis = 0
        self.start_time = time.time()
        self.end_time = 0
        self.font = pg.freetype.SysFont(None, 28)
        self.font.origin = True
        self.split = False
        
        
    def CalcSplit(self):
        time_lapsed = self.end_time - self.start_time
        self.split_minutes = time_lapsed // 60
        self.split_seconds = time_lapsed
        self.split_millis = self.split_seconds * 1000
        self.split = True
        
    def CalcTime(self, game_start_time):
        current_time = time.time()
        time_lapsed = current_time - game_start_time
        self.minutes = time_lapsed // 60
        self.seconds = time_lapsed
        self.millis = self.seconds * 1000


    def setEndTime(self):
        self.end_time = time.time()
        
    def draw(self, screen):
        if self.split:
            split_out='{minutes:02d}:{seconds:02d}:{millis:02d}'.format(minutes=int(self.split_minutes), millis=int(self.split_millis), seconds=int(self.split_seconds))
            self.font.render_to(screen, self.split_timer_pos, split_out, pg.Color('chartreuse2'))
            
        out='{minutes:02d}:{seconds:02d}:{millis:02d}'.format(minutes=int(self.minutes), millis=int(self.millis), seconds=int(self.seconds))
        self.font.render_to(screen, self.timer_pos, out, pg.Color('dodgerblue'))
        
   
        
        
        