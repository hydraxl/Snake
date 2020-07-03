import pygame
import time
import model
import controller
import machine_player

grid_x = 30
grid_y = 30

#board = model.test_board
board = model.Board(grid_x, grid_y)

WHITE = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()

square_size = 20

gameDisplay = pygame.display.set_mode((square_size * grid_x, square_size * grid_y))
pygame.display.set_caption("Snake")

#delay between frame updates
frame_delay = .1

crashed = False
direction = None
game_state = controller.PLAY
ai = machine_player.test_ai(board)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_w or event.key == pygame.K_UP):
            direction = controller.UP
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_s or event.key == pygame.K_DOWN):
            direction = controller.DOWN
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_a or event.key == pygame.K_LEFT):
            direction = controller.LEFT
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
            direction = controller.RIGHT

    #Game Logic
    #direction = ai.output()

    if game_state is controller.PLAY:
        game_state = controller.update_frame(board, direction)
    elif game_state is controller.WIN:
        print("You Won!")
        board.__init__(grid_x, grid_y)
        direction = None
        game_state = controller.PLAY
    else:
        print("You Lost!")
        board.__init__(grid_x, grid_y)
        direction = None
        game_state = controller.PLAY
    #Drawing Screen
    for x in range(grid_x):
        for y in range(grid_y):
            color = BLACK
            if [x, y] == board.apple:
                color = RED
            elif [x, y] == board.snake_head:
                color = LIGHT_GREY
            elif [x, y] in board.snake_body:
                color = WHITE
            pygame.draw.rect(gameDisplay, color, [square_size*x, square_size*y, square_size, square_size])
    pygame.display.update()
    #clock.tick(60)
    time.sleep(frame_delay)
