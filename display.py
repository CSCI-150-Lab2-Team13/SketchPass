import pygame
def display_grid(grid):
    # Initialize pygame
    pygame.init()
    SIZE = len(grid) #As all grids will be squares
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 15
    HEIGHT = 15
    # This sets the margin between each cell
    MARGIN = 1

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [(SIZE * (MARGIN + WIDTH)) + MARGIN, (SIZE * (MARGIN + HEIGHT)) + MARGIN]
    screen = pygame.display.set_mode(WINDOW_SIZE)
     
    # -------- Main Program Loop -----------
        # Set the screen background
    screen.fill(BLACK)
    done = False
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