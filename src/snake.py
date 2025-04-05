import pygame
from pygame.math import Vector2
from random import randint

from abc import ABC, abstractmethod
from collections import deque #stack for bfs

class Fruit:
    def __init__(self):
        self.body = None
    
    def draw(self, screen, size):
        xpos = int(self.body.x * size)
        ypos = int(self.body.y * size)
        rect = pygame.Rect(xpos, ypos, size, size)
        pygame.draw.rect(screen, 'red', rect)
    
    #need to implement check to prevent fruit spawning on snake
    def randomize(self, num):
        self.body = Vector2(randint(0, num - 2),randint(0, num - 2))
        return self.body
class Snake:
    def __init__(self, colour):
        self.colour = colour
        self.body = [Vector2((i,10)) for i in range(8, 5, -1)]
        self.head = self.body[0]
        self.add_block = False
        self.direction = Vector2(1,0)
        self.score = 0

    #snakes with lazers???
    # def fire(self):
    #     lazer = pygame.Rect(self.head.x,self.head.y, cell_size / 4, cell_size / 2)
    #     lazer

    def update(self, screen):
        if self.add_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.add_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]


    def draw(self, screen, size):
        for index, block in enumerate(self.body):
            xpos = int(block.x * size)
            ypos = int(block.y * size)

            rect = pygame.Rect(xpos, ypos, size, size)
            pygame.draw.rect(screen, self.colour, rect)

    def add_point(self):
        self.score += 1

class AISnake(Snake, ABC):
    def __init__(self, colour):
        super().__init__(colour)
        self.body = [Vector2((i,20)) for i in range(8, 5, -1)]

    @abstractmethod
    def decide_direction(self, fruit_pos, board_size, obstacles, player_snake=None):
        pass

class GreedySnake(AISnake):
    def __init__(self, colour):
        super().__init__(colour)

        #adding turn cooldown to nerf greedy snake
        #cooldown breaks greedy snake so set to 0
        self.cooldown = 0
        self.cooldown_lim = 0

    def decide_direction(self, fruit_pos, board_size, obstacles, player_snake=None):
        head = self.body[0]
        directions = [Vector2(1, 0), Vector2(-1, 0), Vector2(0, 1), Vector2(0, -1)]
        best_direction = self.direction
        min_distance = float('inf')

        for direction in directions:
            new_pos = head + direction
            if len(self.body) > 1 and new_pos == self.body[1]:
                continue
            if (
                not 0 <= new_pos.x < board_size or
                not 0 <= new_pos.y < board_size or
                new_pos in self.body or
                new_pos in obstacles
            ):
                continue
            dist = (fruit_pos - new_pos).length_squared()
            if dist < min_distance:
                min_distance = dist
                best_direction = direction

        self.direction = best_direction

##Greedy snake is too OP. BFS with turn cooldown might be balanced.
##to be implemented
class GreedyBFSSnake(AISnake):
    def __init__(self):
        super().__init__()
        self.queued_direction = None
        self.cooldown_lim = 2

    def decide_direction(self, fruit_pos, board_size, obstacles, player_snake=None):
        pass



##only Score is called in game loop
class Score:
    def __init__(self):
        self.text = pygame.font.Font("../assets/OpenSans-Regular.ttf", size=25)

    def draw(self, screen: pygame.Surface, pos, points):
        surface = self.text.render(points, True, 'white')
        xpos = int(pos - 60)
        ypos = int(pos - 40)
        rect = surface.get_rect(center=(xpos,ypos))
        screen.blit(surface, rect)

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

