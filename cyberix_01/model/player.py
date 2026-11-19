class Player:

    def __init__(self, x, y, size, speed):

        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

        self.dir_x = 1
        self.dir_y = 0
        self.is_moving = False
    # Move the player
    def move(self, dx, dy):
        self.is_moving = (dx != 0 or dy != 0)
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            factor = 0.7071
        else:
            factor = 1

        self.x += dx * self.speed * factor
        self.y += dy * self.speed * factor

        # Keep the last movement direction
        if dx != 0 or dy != 0:
            self.dir_x = dx
            self.dir_y = dy

    # Keep player inside the game window
    def keep_inside(self, width, height):

        if self.x > width - self.size:
            self.x = width - self.size

        if self.x < 0:
            self.x = 0

        if self.y > height - self.size:
            self.y = height - self.size

        if self.y < 0:
            self.y = 0