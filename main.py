import pyglet
from GameObject import Snake, Apple
from path_algorithm import DijkstraAlgorithm, AStar


class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame_rate = 1 / 60.0
        n = 30
        m = 30
        self.height_cube = int(1200/n)
        self.width_cube = int(900/m)
        self.game = [0] * n
        for i in range(n):
            self.game[i] = [0] * m

        self.snake = Snake(n, m)
        self.apple = Apple(n, m, self.game)

        path_algo = DijkstraAlgorithm(self.snake, self.apple)
        self.snake.path = path_algo.test()

        self.game[self.apple.x][self.apple.y] = 2

    def draw_polygon(self):
        for x, y in self.snake.body:
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                                 ('v2i', (x*self.height_cube, y*self.width_cube,
                                          x*self.height_cube, y*self.width_cube + self.width_cube,
                                          x*self.height_cube + self.height_cube, y*self.width_cube + self.width_cube,
                                          x*self.height_cube + self.height_cube, y*self.width_cube)))
        x = self.apple.x
        y = self.apple.y
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (x * self.height_cube, y * self.width_cube,
                                      x * self.height_cube, y * self.width_cube + self.width_cube,
                                      x * self.height_cube + self.height_cube, y * self.width_cube + self.width_cube,
                                      x * self.height_cube + self.height_cube, y * self.width_cube)),
                             ('c3B', (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0)))

    def on_draw(self):
        self.clear()
        self.draw_polygon()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.LEFT:
            self.snake.direction = 0
        if symbol == pyglet.window.key.RIGHT:
            self.snake.direction = 1
        if symbol == pyglet.window.key.UP:
            self.snake.direction = 2
        if symbol == pyglet.window.key.DOWN:
            self.snake.direction = 3

    def update(self, dt):
        error = self.snake.move(self.game, self.apple)
        if error:
            print(error)
            self.close()


if __name__ == "__main__":
    window = GameWindow(1200, 900, "Snake", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
