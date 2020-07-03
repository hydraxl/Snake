from random import choice


class Board:
    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y
        self.snake_head = [0, 0]
        self.snake_body = []
        #any random position except [0, 0] where the snake is
        self.apple = choice([[x, y] for x in range(5) for y in range(5)][1:])

    def __str__(self):
        board = ''
        for y in range(self.y):
            board += '|'
            for x in range(self.x):
                if [x, y] == self.apple:
                    board += 'aa'
                elif [x, y] == self.snake_head:
                    board += 'hh'
                elif [x, y] in self.snake_body:
                    board += 'ss'
                else:
                    board += '  '
            board += '|\n'
        return board


test_board = Board(6, 6)
