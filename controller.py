from random import choice

UP = 'u'
DOWN = 'd'
LEFT = 'l'
RIGHT = 'r'

LOSS = 'lose'
WIN = 'win'
PLAY = 'play'

def update_frame(board, direction):
    #sets new pos to the head position moved in the direction by 1
    new_pos = []
    if direction is UP:
        new_pos = [board.snake_head[0], board.snake_head[1] - 1]
    elif direction is DOWN:
        new_pos = [board.snake_head[0], board.snake_head[1] + 1]
    elif direction is LEFT:
        new_pos = [board.snake_head[0] - 1, board.snake_head[1]]
    elif direction is RIGHT:
        new_pos = [board.snake_head[0] + 1, board.snake_head[1]]

    if direction is not None:
        #if the new position touches the snake or goes out of bounds, game over
        if new_pos in board.snake_body:
            return LOSS
        elif new_pos[0] < 0:
            return LOSS
        elif new_pos[0] >= board.x:
            return LOSS
        elif new_pos[1] < 0:
            return LOSS
        elif new_pos[1] >= board.y:
            return LOSS

        #updates snake body with new position
        board.snake_body = [board.snake_head] + board.snake_body
        board.snake_head = new_pos

        #if the apple is touched, moves the apple somewhere else and increases the snake size by 1
        if board.snake_head == board.apple:
            #list of all positions not occupied by the snake
            snakeless_spots = []
            for x in range(board.x):
                for y in range(board.y):
                    if not ([x, y] in board.snake_body or [x, y] == board.snake_head):
                        snakeless_spots.append([x, y])

            if snakeless_spots == []:
                return WIN
            board.apple = choice(snakeless_spots)
        else:
            del board.snake_body[-1]

    return PLAY
