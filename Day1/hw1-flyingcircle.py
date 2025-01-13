"""Flying circle with pygame"""
import pygame

class Circle:
    """
    Circle class
    """
    def __init__(self, radius, x, y, color) -> None:
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen) -> None:
        """
        Draw circle at (x, y)
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, shift_x, shift_y) -> None:
        """
        Move the circle by shift_x and shift_y
        """
        self.x += shift_x
        self.y += shift_y

if __name__ == "__main__":
    window_width = 500
    window_height = 500

    color = (0, 255, 0)
    c = Circle(10, 10, 50, color)

    pygame.init()

    screen = pygame.display.set_mode((window_width, window_height)) # set screen size
    pygame.display.set_caption("Flying Circle") # set the title
    clock = pygame.time.Clock() # Clock, I guess.

    vx = 1
    vy = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        print(f"x:{c.x}, y:{c.y}") # print current position

        if c.x > window_width - c.radius or c.x < c.radius:
            vx = -vx
        if c.y > window_height - c.radius or c.y < c.radius:
            vy = -vy

        screen.fill((255, 255, 255)) # fill with white

        c.move(vx,vy)
        c.draw(screen)

        pygame.display.flip()

        clock.tick(60) # set to 60 fps

    pygame.quit()

# End of file
