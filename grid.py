import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 15
HEIGHT = 15
SIZE = 30
# This sets the margin between each cell
MARGIN = 5

grid = [[0]*SIZE for i in range(SIZE)]
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [605, 605]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
pressed = False
while not done:
    for event in pygame.event.get():  # User did something
        pos = pygame.mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
        column = pos[0] // (WIDTH + MARGIN)
        row = pos[1] // (HEIGHT + MARGIN)

        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN and not pressed:
            # User clicks the mouse. Get the position
                pressed = True
                # Set that location to one
                grid[row][column] = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = False
        elif pressed and row < SIZE and column < SIZE and row > -1 and column > -1:
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                grid[row][column] = 1
        elif event.type == pygame.KEYDOWN:
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
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()