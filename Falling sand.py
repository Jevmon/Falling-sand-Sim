import pygame
import keyboard

WINDOW = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
WIDTH, HEIGHT = [int(x) for x in WINDOW.get_size()]
SAND_SIZE = 5
clock = pygame.time.Clock()
color = (126,126,0)

def quit():
    global running
    running = False

class Sand:
    def __init__(self, Y, X, color):
        self.Y = Y
        self.X = X
        self.color = color
    
    def handle_falling(self):
        global grid
        try:
            if self.Y < HEIGHT/SAND_SIZE and not isinstance(grid[self.Y+1][self.X], Sand):
                grid[self.Y][self.X] = None
                self.Y+=1
                grid[self.Y][self.X] = self
        except:
            pass

grid = [[None for _ in range(int(WIDTH/SAND_SIZE))] for _2 in range(int(HEIGHT/SAND_SIZE))]

def create_map(grid):

    WINDOW.fill((0,0,0))

    for layer in grid:
        for pixel in layer:
            if isinstance(pixel, Sand):
                pygame.draw.rect(WINDOW, pixel.color, (pixel.X*SAND_SIZE, pixel.Y*SAND_SIZE, SAND_SIZE, SAND_SIZE))

    pygame.display.flip()


def handle_simulation():
    global grid
    for layer in reversed(grid):
        for pixel in reversed(layer):
            if isinstance(pixel, Sand):
                pixel.handle_falling()
    create_map(grid)

def create_sand(x,y):
    global grid
    try:
        if not isinstance(grid[y][x], Sand):
            grid[y][x] = Sand(Y=y,X=x,color=color)
    except IndexError:
        pass

def clear():
    global grid
    grid = [[None for _ in range(int(WIDTH/SAND_SIZE))] for _2 in range(int(HEIGHT/SAND_SIZE))]
    WINDOW.fill((0,0,0))

keyboard.add_hotkey('escape', quit)
keyboard.add_hotkey('space', clear)
keyboard.add_hotkey('1', lambda:globals().__setitem__('color', (126,126,0)))
keyboard.add_hotkey('2', lambda:globals().__setitem__('color', (200,100,0)))
keyboard.add_hotkey('3', lambda:globals().__setitem__('color', (200,0,0)))
keyboard.add_hotkey('4', lambda:globals().__setitem__('color', (0,200,0)))
keyboard.add_hotkey('5', lambda:globals().__setitem__('color', (0,100,200)))
keyboard.add_hotkey('6', lambda:globals().__setitem__('color', (0,0,200)))
keyboard.add_hotkey('7', lambda:globals().__setitem__('color', (200,0,255)))
keyboard.add_hotkey('8', lambda:globals().__setitem__('color', (255,0,100)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

    if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos()
        create_sand(int(x/SAND_SIZE),int(y/SAND_SIZE))
        create_sand(int(x/SAND_SIZE)+1,int(y/SAND_SIZE))
        create_sand(int(x/SAND_SIZE)-1,int(y/SAND_SIZE))
        create_sand(int(x/SAND_SIZE),int(y/SAND_SIZE)+1)
        create_sand(int(x/SAND_SIZE),int(y/SAND_SIZE)-1)

    handle_simulation()
