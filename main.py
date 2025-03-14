import pygame, sys, pymunk

## I wrote this code by watching Clear Code's YouTube Video

def create_apple(space, pos):
    body = pymunk.Body(1, 50, body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 110)
    space.add(body, shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_img.get_rect(center = (pos_x, pos_y))
        screen.blit(apple_img, apple_rect)

def static_balls(space, pos1):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos1
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape

def draw_static_balls(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0), (pos_x, pos_y), 50)

pygame.init() # pygame initialisation
screen = pygame.display.set_mode((800, 800)) # creating display surface
clock = pygame.time.Clock() # creating the game clock
space = pymunk.Space()
space.gravity = (0,500)
apple_img = pygame.image.load('appple.png')
apples = []


balls = []
balls.append(static_balls(space, (500, 500)))
balls.append(static_balls(space, (300, 700)))
balls.append(static_balls(space, (168, 635)))


# Game Loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            apples.append(create_apple(space, event.pos))

    screen.fill((217,217,217)) ## BG Color
    draw_apples(apples)
    space.step(1/50)
    draw_static_balls(balls)

    pygame.display.update() # rendering the frame
    clock.tick(120) # limits fps to 120
