import time
import sys
import pygame
from snake import Grid, Snake, Score, Fruit, GreedySnake
from pygame.math import Vector2

class Game:
    
    def __init__(self):

        pygame.init()


        self.grid = Grid()
        self.screen = pygame.display.set_mode((self.grid.dimensions, self.grid.dimensions))
        self.clock = pygame.time.Clock()
    

        self.player = Snake(
            colour='aqua',
            grid=self.grid
            )
        
        self.ai = GreedySnake(
            colour='green',
            grid=self.grid
            )
        
        self.fruit = Fruit(
            colour='red',
            grid=self.grid
        )

        self.score = Score(
            colour='white',
            font="../assets/OpenSans-Regular.ttf",
            grid=self.grid
        )


        self.running = True
        self.points = str(len(self.player.body) - 3)

    def run(self):
  
        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE, 80)

        self.fruit.randomize(self.player, self.ai)

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
            self.player.draw(self.screen)
            self.ai.draw(self.screen)
            self.fruit.draw(self.screen)
            self.score.draw(self.screen, self.points)

    def update(self):
        obstacles = self.snake.body + self.ai.body[1:]
        self.snake.update(self.screen)
        
        self.ai_snake.decide_direction(self.fruit.body, self.cell_number, obstacles=obstacles)
        self.ai_snake.cooldown = self.ai_snake.cooldown_lim
        self.ai_snake.update(self.screen)
    
    def check_munch(self):
        if self.player.body[0].x == self.fruit.body.x and self.player.body[0].y == self.fruit.body.y:
            self.snake.add_block = True
            self.fruit.randomize(self.cell_number)
        if self.ai_snake.body[0].x == self.fruit.body.x and self.ai_snake.body[0].y == self.fruit.body.y:
            self.ai_snake.add_block = True
            self.fruit.randomize(self.cell_number)

    def check_input(self, event):
        up, down, left, right = (Vector2(0,-1), Vector2(0,1), Vector2(-1,0), Vector2(1,0))
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            if not self.snake.direction == down:
                self.snake.direction = up
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            if not self.snake.direction == up:
                self.snake.direction = down
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            if not self.snake.direction == right:
                self.snake.direction = left
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            if not self.snake.direction == left:
                self.snake.direction = right

    def check_death(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.snake = Snake('aqua')
        if self.snake.body[0] in self.ai_snake.body:
            self.snake = Snake('aqua')
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.snake = Snake('aqua')
        if not 0 <= self.ai_snake.body[0].x < self.cell_number or not 0 <= self.ai_snake.body[0].y < self.cell_number:
            self.ai_snake = GreedySnake('green')
            self.stamp_death('AI snake death')
        if self.ai_snake.body[0] in self.snake.body:
            self.ai_snake = GreedySnake('green')
            self.stamp_death('AI snake death')
        for block in self.ai_snake.body[1:]:
            if block == self.ai_snake.body[0]:
                self.ai_snake = GreedySnake('green')
                self.stamp_death('AI snake death')

    def stamp_death(self, msg):
        self.death_time = time.time()
        print(msg)
        print(self.death_time - self.spawn_time)
        self.spawn_time = self.death_time

    ##to implement random spawning 
    def spawn_snakes(player, snakes):
        pass
if __name__ == '__main__':
    game = Game()
    game.run()