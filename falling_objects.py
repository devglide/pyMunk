import pygame, sys, pymunk
from pygame.constants import MOUSEBUTTONDOWN
from pygame.transform import scale


def create_obj(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)   #mass, inertia, body-type
    body.position = (pos)
    shape = pymunk.Circle(body, 80)
    space.add(body, shape)
    return shape

def draw_objs(objs):
    for obj in objs:
        pos_x = int(obj.body.position.x)
        pos_y = int(obj.body.position.y)
        pygame.draw.circle(screen, (0,0,0), (pos_x,pos_y), 80)

def static_ball(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,50)
    space.add(body,shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, (0,0,0), (pos_x,pos_y),50)
        


pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock() #create game clock
space = pymunk.Space()
space.gravity = (0, 100) #horizontal and vertical gravity value
objs = []


balls = []
balls.append(static_ball(space, (500,500)))
balls.append(static_ball(space, (250,200)))

while True:
    for event in pygame.event.get():   # checking for user input
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            objs.append(create_obj(space, event.pos))
    
    screen.fill((217, 217,217))
    draw_objs(objs)
    draw_static_ball(balls)
    space.step(1/50) #pymonk recommendation
    pygame.display.update() #rendering the frame
    clock.tick(120)