import time
import sys
import pygame
import asyncio
from snake import Grid, Snake, Score, Fruit, GreedySnake
from pygame.math import Vector2



class Game:
    
    def __init__(self):

        pygame.init()

        self.font = pygame.font.Font("assets/PressStart2P-Regular.ttf")
        self.grid = Grid()
        self.screen = pygame.display.set_mode((self.grid.dimensions, self.grid.dimensions))
        self.clock = pygame.time.Clock()
    

        self.player = Snake(
            colour='aqua',
            grid=self.grid
            )
        
        self.player_score = Score(
            colour='white',
            font=self.font,
            xpos=self.grid.dimensions - 615,
            ypos=self.grid.dimensions - 30,
            text='you'
        )
        
        self.ai = GreedySnake(
            colour='green',
            grid=self.grid
            )
        
        self.ai_score = Score(
            colour='white',
            font=self.font,
            xpos=self.grid.dimensions - 60,
            ypos=self.grid.dimensions - 30,
            text='cpu'
        )
        self.fruit = Fruit(
            colour='red',
            grid=self.grid
        )

        self.fruit.randomize(self.player, self.ai)

        self.running = True


    def draw(self):
            self.screen.fill('black')
            self.player_score.draw(self.screen, self.player.points)
            self.ai_score.draw(self.screen, self.ai.points)

            self.player.draw(self.screen)
            

            self.ai.draw(self.screen)
            

            self.fruit.draw(self.screen)


    def update(self):
        obstacles = self.player.body + self.ai.body[1:]
        self.player.update()
        
        self.ai.decide_direction(self.fruit.body, obstacles=obstacles)
        self.ai.update()
    
    def check_munch(self):
        if self.player.body[0].x == self.fruit.body.x and self.player.body[0].y == self.fruit.body.y:
            self.player.add_block = True
            self.fruit.randomize(self.player, self.ai)
        if self.ai.body[0].x == self.fruit.body.x and self.ai.body[0].y == self.fruit.body.y:
            self.ai.add_block = True
            self.fruit.randomize(self.player, self.ai)

    def check_input(self, event):
        up, down, left, right = (Vector2(0,-1), Vector2(0,1), Vector2(-1,0), Vector2(1,0))
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            if not self.player.direction == down:
                self.player.direction = up
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            if not self.player.direction == up:
                self.player.direction = down
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            if not self.player.direction == right:
                self.player.direction = left
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            if not self.player.direction == left:
                self.player.direction = right

    def check_player_death(self):
        if (
            not 0 <= self.player.body[0].x < self.grid.cell_number or 
            not 0 <= self.player.body[0].y < self.grid.cell_number
        ):
            print('player-boundary')
            self.player = Snake(
                            colour='aqua',
                            grid=self.grid
                        )
        if self.player.body[0] in self.ai.body:
            print('player-crash')
            self.player = Snake(
                            colour='aqua',
                            grid=self.grid
                        )
        for block in self.player.body[1:]:
            if block == self.player.body[0]:
                print('player-suicide')
                self.player = Snake(
                            colour='aqua',
                            grid=self.grid
                        )
    def check_ai_death(self):
        if (
            not 0 <= self.ai.body[0].x < self.grid.cell_number or 
            not 0 <= self.ai.body[0].y < self.grid.cell_number
        ):
            print('ai-boundary')
            self.ai = GreedySnake(
                            colour='green',
                            grid=self.grid
                        )
        if self.ai.body[0] in self.player.body:
            print('ai-crash')
            self.ai = GreedySnake(
                            colour='green',
                            grid=self.grid
                        )
        for block in self.ai.body[1:]:
            if block == self.ai.body[0]:
                print('ai-suicide')
                self.ai = GreedySnake(
                            colour='green',
                            grid=self.grid
                        )

    def stamp_death(self, msg):
        self.death_time = time.time()
        print(msg)
        print(self.death_time - self.spawn_time)
        self.spawn_time = self.death_time


async def main():

    game = Game()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 80)


    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)
            if event.type == SCREEN_UPDATE:
                game.update()

            game.check_munch()

            if event.type == pygame.KEYDOWN:
                game.check_input(event)

            game.check_ai_death()
            game.check_player_death()

        game.draw()
        
        pygame.display.update()
        game.clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())