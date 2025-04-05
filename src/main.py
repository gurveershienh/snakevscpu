import sys
import pygame
from snake import Snake, Score, Fruit, GreedySnake, GreedyBFSSnake, AISnake
from pygame.math import Vector2

class Game:
    
    def __init__(self):

        pygame.init()
        self.cell_size = 15
        self.cell_number = 45
        self.screen_len = self.cell_size * self.cell_number
        self.screen = pygame.display.set_mode((self.screen_len, self.screen_len))
        self.clock = pygame.time.Clock()
    

        self.snake = Snake('green')
        self.fruit = Fruit()
        self.score = Score()
        self.ai_snake = GreedySnake('orange')
        self.running = True
        self.points = str(len(self.snake.body) - 3)
    def run(self):
  
        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE, 80)

        self.fruit.randomize(self.cell_number)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(1)
                if event.type == SCREEN_UPDATE:
                    self.update()

                self.check_munch()

                if event.type == pygame.KEYDOWN:
                    self.check_input(event)

                self.check_death()

            self.points = str(len(self.snake.body) - 3) 
            self.draw()
            
            pygame.display.update()
            self.clock.tick(60)

    def draw(self):
            self.screen.fill('black')
            self.snake.draw(self.screen, self.cell_size)
            self.ai_snake.draw(self.screen, self.cell_size)
            self.fruit.draw(self.screen, self.cell_size)
            self.score.draw(self.screen, self.screen_len, self.points)

    def update(self):
        obstacles = self.snake.body + self.ai_snake.body[1:]
        self.snake.update(self.screen)
        if self.ai_snake.cooldown == 0:
            self.ai_snake.decide_direction(self.fruit.body, self.cell_number, obstacles=obstacles)
            self.ai_snake.cooldown = self.ai_snake.cooldown_lim
        else:
            future_move = self.ai_snake.body[0] + self.ai_snake.direction
            if future_move != self.fruit.body:
                self.ai_snake.cooldown -= 1
        self.ai_snake.update(self.screen)
    
    def check_munch(self):
        if self.snake.body[0].x == self.fruit.body.x and self.snake.body[0].y == self.fruit.body.y:
            print('munch')
            self.snake.add_block = True
            self.fruit.randomize(self.cell_number)
        if self.ai_snake.body[0].x == self.fruit.body.x and self.ai_snake.body[0].y == self.fruit.body.y:
            print('munch')
            self.ai_snake.add_block = True
            self.fruit.randomize(self.cell_number)

    def check_input(self, event):
        up, down, left, right = (Vector2(0,-1), Vector2(0,1), Vector2(-1,0), Vector2(1,0))
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            print('UP')
            print('------------------------')
            if not self.snake.direction == down:
                self.snake.direction = up
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            print('DOWN')
            print('------------------------')
            if not self.snake.direction == up:
                self.snake.direction = down
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            print('LEFT')
            print('------------------------')
            if not self.snake.direction == right:
                self.snake.direction = left
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            print('RIGHT')
            print('------------------------')
            if not self.snake.direction == left:
                self.snake.direction = right

    def check_death(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.snake = Snake('green')
        if self.snake.body[0] in self.ai_snake.body:
            self.ai_snake.add_block = True
            self.snake = Snake('green')
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.snake = Snake('green')
        if not 0 <= self.ai_snake.body[0].x < self.cell_number or not 0 <= self.ai_snake.body[0].y < self.cell_number:
            self.ai_snake = GreedySnake('orange')
        if self.ai_snake.body[0] in self.snake.body:
            self.snake.add_block = True
            self.ai_snake = GreedySnake('orange')
        for block in self.ai_snake.body[1:]:
            if block == self.ai_snake.body[0]:
                self.ai_snake = GreedySnake('orange')

    ##to implement random spawning 
    def spawn_snakes(player, snakes):
        pass
if __name__ == '__main__':
    game = Game()
    game.run()