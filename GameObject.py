import random
from path_algorithm import DijkstraAlgorithm, AStar


class Apple:
    x = 0
    y = 0

    def __init__(self, width, height, game):
        self.width = width
        self.height = height
        self.set_x_and_y(game)

    def set_x_and_y(self, game):
        while True:
            self.x = random.randint(0, self.width-1)
            self.y = random.randint(0, self.height-1)
            if game[self.x][self.y] == 0:
                game[self.x][self.y] = 2
                # print("x:%d y:%d" % (self.x, self.y))
                break


class Snake:
    direction = 0
    path = list()

    def __init__(self, width, height):
        self.body = [(int(width / 2), int(height / 2))]

    def find_apple(self, apple):
        x_apple = apple.x
        y_apple = apple.y
        x_head, y_head = self.body[-1]
        if x_apple == x_head and y_apple == y_head:
            return True
        return False

    def move(self, game, apple):
        if self.direction == 3:
            x, y = self.body[-1]
            if y-1 < 0:
                y = 29
            else:
                y = y-1
        if self.direction == 2:
            x, y = self.body[-1]
            if y+1 > 29:
                y = 0
            else:
                y = y+1
        if self.direction == 1:
            x, y = self.body[-1]
            if x+1 > 29:
                x = 0
            else:
                x = x + 1
        if self.direction == 0:
            x, y = self.body[-1]
            if x-1 < 0:
                x = 29
            else:
                x = x-1

        game[x][y] = 1
        self.body.append((x, y))
        error = None

        if self.find_apple(apple) is False:
            tail_x, tail_y = self.body[0]
            game[tail_x][tail_y] = 0
            self.body.pop(0)
        else:
            apple.set_x_and_y(game)
            path_algorithm = AStar(self, apple)
            self.path = path_algorithm.test()
            error = path_algorithm.error

        if error is None:
            self.direction = self.path[-1]
            if len(self.path) != 1:
                self.path.pop(-1)
        return error
