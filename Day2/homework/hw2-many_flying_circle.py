import pygame
import random as r

class Circle:
    """
    Circle class
    """
    def __init__(self, radius, x, y, color, vx, vy) -> None:
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.vx = vx
        self.vy = vy

    def draw(self, screen) -> None:
        """
        Draw circle at (x, y)
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, window_width, window_height) -> None:
        """
        Move the circle by shift_x and shift_y
        """
        if self.x > window_width - self.radius or self.x < self.radius:
            self.vx = -self.vx
        if self.y > window_height - self.radius or self.y < self.radius:
            self.vy = -self.vy

        self.x += self.vx
        self.y += self.vy


if __name__ == "__main__":
    window_width = 500
    window_height = 500

    N = 20

    circles = []
    for i in range(N):
        radius = r.randint(10, 40)
        x = r.randint(radius, window_width-radius)
        y = r.randint(radius, window_height-radius)
        vx = r.randint(-5, 5)
        vy = r.randint(-5, 5)
        R = r.randint(0, 255)
        G = r.randint(0, 255)
        B = r.randint(0, 255)
        circles.append(Circle(radius, x, y, (R,G,B), vx, vy))

    pygame.init()

    screen = pygame.display.set_mode((window_width, window_height)) # set screen size
    pygame.display.set_caption("Multiple Flying Circle") # set the title
    clock = pygame.time.Clock() # Clock, I guess.

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        screen.fill((255, 255, 255)) # fill with white

        for circle in circles:
            circle.move(window_width, window_height)
            circle.draw(screen)

        pygame.display.flip()

        clock.tick(60) # set to 144 fps

    pygame.quit()

# End of file
