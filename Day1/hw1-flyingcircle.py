import pygame

class Circle:
    """
    Circle class
    """
    def __init__(self, radius, x, y, width=100, height=100) -> None:
        self.radius = radius
        self.x = x
        self.y = y
        self.window_width = width
        self.window_height = height

    def draw(self, screen) -> None:
        """
        Draw circle at (x, y)
        """
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), self.radius)

    def move(self, shift_x, shift_y) -> None:
        """
        Move the circle by shift_x and shift_y
        """
        self.x += shift_x
        self.y += shift_y

if __name__ == "__main__":
    window_width = 500
    window_height = 500

    c = Circle(10, 10, 50, window_width, window_height)

    pygame.init()

    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Flying Circle")
    clock = pygame.time.Clock()

    vx = 1
    vy = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        if c.x == c.window_width or c.x == 0:
            vx = -vx
        if c.y == c.window_height or c.y == 0:
            vy = -vy

        print(f"x:{c.x}, y:{c.y}")
        screen.fill((255, 255, 255))
        c.move(vx,vy)
        c.draw(screen)
        pygame.display.flip()
        clock.tick(144)

    pygame.quit()