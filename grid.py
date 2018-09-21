import pygame
def create_grid(SIZE):
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

     
    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 15
    HEIGHT = 15

    # This sets the margin between each cell
    MARGIN = 1

    grid = [[0]*SIZE for i in range(SIZE)]
    #pts = []
    # Initialize pygame
    pygame.init()
     
    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [(SIZE * (MARGIN + WIDTH)) + MARGIN, (SIZE * (MARGIN + HEIGHT)) + MARGIN]
    screen = pygame.display.set_mode(WINDOW_SIZE)
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    #clock = pygame.time.Clock()
     
    # -------- Main Program Loop -----------

    while not done:
        for event in pygame.event.get():  # User did something
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif pygame.mouse.get_pressed()[0] and row < SIZE and column < SIZE and row > -1 and column > -1:
                    grid[row][column] = 1
                    #pts.append([row,col])
                    continue
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if sum(map(sum, grid)) > 20:
                        return grid
                        #return pts
                        #return (','.join(str(col) for row in grid for col in row)) #Convert to string
                if event.key == pygame.K_c:
                    grid = [[0]*SIZE for i in range(SIZE)]
     
        # Set the screen background
        screen.fill(BLACK)
     
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
        #clock.tick(60)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
    return 1