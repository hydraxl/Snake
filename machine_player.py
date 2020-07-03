import controller

#Moves through every square repeatedly
#only works if either the board's y size is even

class test_ai:
    def __init__(self, board):
        self.environment = board

    def output(self):
        if self.environment.y % 2 != 0:
            raise ValueError("Board y cannot be odd when using test AI")
        if self.environment.snake_head == [0, 0]:
            return controller.RIGHT
        elif self.environment.snake_head[0] == 0:
            return controller.UP
        elif (self.environment.snake_head[1] % 2 == 0) and (self.environment.snake_head[0] < self.environment.x - 1):
            return controller.RIGHT
        elif (self.environment.snake_head[1] % 2 != 0) and (self.environment.snake_head[0] != 1):
            return controller.LEFT
        elif (self.environment.snake_head[1] == self.environment.y - 1) and (self.environment.snake_head[0] == 1):
            return controller.LEFT
        else:
            return controller.DOWN

class QLearningPlayer:
    def __init__(self, board):
        self.actions = [controller.LEFT, controller.RIGHT, controller.UP, controller.DOWN]
        self.environment = model.Board
        self.state = board

    def output(self):
        'Returns action a based on current state'
