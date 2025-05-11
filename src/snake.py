import time
import pygame
from pygame.math import Vector2
from random import randint

class Grid:
    def __init__(self):
        self.cell_size = 15
        self.cell_number = 45
        self.dimensions = self.cell_size * self.cell_number
        
        self.rects = None

    def build(self):
        rects = []
        for i in range(self.cell_number):
            #create vertical lines
            xpos = self.cell_size * i
            ypos = 0
            rect = pygame.Rect(xpos, ypos, 1, self.dimensions)
            rects.append(rect)

            #create horizontal lines
            ypos = xpos
            xpos = 0
            rect = pygame.Rect(xpos, ypos, self.dimensions, 2)
            rects.append(rect)
        return rects
    
    def draw(self, screen):
        for rect in self.rects:
            pygame.draw.rect(screen, 'gray31', rect)

class Score:
    def __init__(self, colour, font: pygame.font.Font, xpos, ypos, text):
        self.text = text
        self.colour = colour
        self.font = font
        self.xpos = xpos
        self.ypos = ypos

    def draw(self, screen: pygame.Surface, points):
        top_surface = self.font.render(self.text, True, self.colour)
        top_rect = top_surface.get_rect(center=(self.xpos,self.ypos))

        bottom_surface = self.font.render(points, True, self.colour)
        bottom_rect = bottom_surface.get_rect(center=(self.xpos,self.ypos-30))
        screen.blit(top_surface, top_rect)
        screen.blit(bottom_surface, bottom_rect)

class Snake:
    def __init__(self, colour, grid: Grid):
        
        self.body = [Vector2((i,10)) for i in range(8, 5, -1)]
        print(self.body)
        self.head = self.body[0]
        self.add_block = False
        self.direction = Vector2(1,0)

        self.colour = colour
        self.size = grid.cell_size
        self.points = str(len(self.body) - 3)
        self.grid = grid
    #snakes with lazers???
    # def fire(self):
    #     lazer = pygame.Rect(self.head.x,self.head.y, self.size / 4, self.size / 2)
    #     lazer

    def update(self):
        if self.add_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.add_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        self.points = str(len(self.body) - 3)

    def draw(self, screen):
        for block in self.body:
            xpos = int(block.x * self.size)
            ypos = int(block.y * self.size)
            rect = pygame.Rect(xpos, ypos, self.size, self.size)
            pygame.draw.rect(screen, self.colour, rect)



class GreedySnake(Snake):
    def __init__(self, colour, grid: Grid):
        super().__init__(colour, grid)
        self.body = [Vector2((i,20)) for i in range(8, 5, -1)]

    def decide_direction(self, fruit_pos, obstacles):
        head = self.body[0]
        directions = [Vector2(1, 0), Vector2(-1, 0), Vector2(0, 1), Vector2(0, -1)]
        best_direction = self.direction
        min_distance = float('inf')

        for direction in directions:
            new_pos = head + direction
            if len(self.body) > 1 and new_pos == self.body[1]:
                continue
            if (
                not 0 <= new_pos.x < self.grid.dimensions or
                not 0 <= new_pos.y < self.grid.dimensions or
                new_pos in self.body or
                new_pos in obstacles
            ):
                continue
            dist = (fruit_pos - new_pos).length_squared()
            if dist < min_distance:
                min_distance = dist
                best_direction = direction

        self.direction = best_direction

class Fruit:
    def __init__(self, colour, grid: Grid):
        self.body = None
        self.colour = colour
        self.size = grid.cell_size
        self.boundary = grid.cell_number
    
    def draw(self, screen):
        xpos = int(self.body.x * self.size)
        ypos = int(self.body.y * self.size)
        rect = pygame.Rect(xpos, ypos, self.size, self.size)
        pygame.draw.rect(screen, self.colour, rect)
    
    def randomize(self, player: Snake, ai: Snake):
        new_pos = Vector2(randint(0, self.boundary - 2),randint(0, self.boundary - 2))
        while new_pos in player.body or new_pos in ai.body:
            new_pos = Vector2(randint(0, self.boundary - 2),randint(0, self.boundary - 2))
        self.body = new_pos
  
    

##only Score is called in game loop

##to be implemented
class Title:
    def __init__(self):
        self.text = pygame.font.Font("OpenSans-Regular.ttf", size=150)
        self.string = 'Greedy Snake'
    def draw(self, screen: pygame.Surface, pos):
        surface = self.text.render(self.string, True, 'white')
        xpos = int(pos)
        ypos = int(pos)
        rect = surface.get_rect(center=(xpos,ypos))
        screen.blit(surface, rect)
class StartButton:
    def __init__(self):
        self.text = pygame.font.Font("OpenSans-Regular.ttf", size=100)
class Menu:
    def __init__(self):
        pass
    
    def run(self):
        running = True

