import pygame
def display_grid(grid):
    # Initialize pygame
    pygame.init()
    SIZE = len(grid) #As all grids will be squares
    # Define some colors
    WHITE = (255, 255, 255)

    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0,0,255)
    PURPLE = (142,68,173)
    ORANGE = (230,126,34)
    GREY = (127,140,141)
    TUQUOISE = (52, 231, 228)
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 25
    HEIGHT = 25
    # This sets the margin between each cell
    MARGIN = 5

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [(SIZE * (MARGIN + WIDTH)) + MARGIN, (SIZE * (MARGIN + HEIGHT)) + MARGIN]
    screen = pygame.display.set_mode(WINDOW_SIZE)
     
    # -------- Main Program Loop -----------
        # Set the screen background
    screen.fill(BLACK)
    done = False
    colors = [BLACK, GREEN, RED, BLUE, PURPLE, ORANGE, GREY, TUQUOISE]
    set_color = 0
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        # Draw the grid
        for row in range(SIZE):
            for column in range(SIZE):
                color = WHITE
                if grid[row][column] == 1:
                    color = BLACK
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
    
                # Limit to 60 frames per second
        clock.tick(60)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    pygame.quit()