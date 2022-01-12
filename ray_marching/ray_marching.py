import pygame, sys, os, random, math
from numba import njit

#----------------Setup pygame/window----------------#
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Ray Marching')

WINDOW_SIZE = (1200, 800)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((1200, 800))
#----------------Setup pygame/window----------------#

click = True
shapes = []
dist = 0
point = [190, 630]
outline = []
angle = -math.pi*(7/10)
step = 2

shapes.append(('circle', (200, 200), 50))
shapes.append(('circle', (250, 750), 50))
shapes.append(('circle', (1000, 600), 150))
shapes.append(('rect', (800, 180), (100, 150)))
shapes.append(('rect', (600, 400), (100, 80)))

shapes.append(('rect', (600, 0), (1200, 1)))
shapes.append(('rect', (1200, 400), (1, 800)))
shapes.append(('rect', (600, 800), (1200, 1)))
shapes.append(('rect', (0, 400), (1, 800)))

@njit(fastmath=True)
def rect_dist(center, point, size):
    x, y = center
    px, py = point
    width, height = size

    dx = max(abs(px - x) - width / 2, 0)
    dy = max(abs(py - y) - height / 2, 0)
    return math.sqrt(dx * dx + dy * dy)

def ray_march(point, angle, shapes, outline):
    # angle = math.atan2(point[1]-my, point[0]-mx)+math.pi
    temp_point = point.copy()

    dist = 2
    for i in range(30):
        dist = find_dist_to_shapes(temp_point, shapes)
        if dist < 1000:
            pygame.draw.circle(display, (255, 255, 255), (temp_point[0], temp_point[1]), dist, 1)
        if dist < 3:
            if find_dist_to_shapes(temp_point, shapes) < 3:
                if temp_point not in outline:
                    if len(outline) > 1:
                        if int(temp_point[0]) == int(outline[-1][0]) or int(temp_point[1]) == int(outline[-1][1]):
                            outline.append(temp_point)
                            outline.pop(-1)
                        else:
                            outline.append(temp_point)
                    else:
                        outline.append(temp_point)
        temp_point[0] = temp_point[0]+(dist-1)*math.cos(angle)
        temp_point[1] = temp_point[1]+(dist-1)*math.sin(angle)
        pygame.draw.line(display, (200, 200, 200), point, temp_point)

def find_dist_to_shapes(point, shapes):
    dist = 0
    for shape in shapes:
        if shape[0] == 'circle':
            dist_from_point = math.sqrt((abs(point[0]-shape[1][0])**2) + (abs(point[1]-shape[1][1])**2)) - shape[2]
        if shape[0] == 'rect':
            dist_from_point = rect_dist(shape[1], (point[0], point[1]), shape[2])

        if dist != 0:
            if dist_from_point < dist:
                dist = dist_from_point
        else:
            dist = dist_from_point
        
    return dist

# while angle < math.pi*(13/10): # Auto (Comment out Visual)
#     if angle < math.pi*(13/10): #---#
#         angle += (math.pi/360)/step #---#
#     ray_march(point, angle, shapes, outline) #---#

while True:
    display.fill((20, 20, 20))

    if angle < math.pi*(13/10): # Visual (Comment out Auto)
        angle += (math.pi/360)/step #---#
    ray_march(point, angle, shapes, outline) #---#

    pygame.draw.circle(display, (255, 255, 255), (point[0], point[1]), 8)

    if shapes and click:
        for shape in shapes:
            if shape[0] == 'circle':
                pygame.draw.circle(display, (50, 50, 50), shape[1], shape[2])
            if shape[0] == 'rect':
                temp_rect = pygame.Rect(shape[1][0]-shape[2][0]/2, shape[1][1]-shape[2][1]/2, shape[2][0], shape[2][1])
                pygame.draw.rect(display, (50, 50, 50), temp_rect)

    if outline:
        for i, spot in sorted(enumerate(outline), reverse=True):
            if find_dist_to_shapes(spot, shapes) > 2:
                outline.pop(i)
            # pygame.draw.circle(display, (255, 0, 0), (spot[0], spot[1]), 2)
        if len(outline) > 3:
            pygame.draw.polygon(display, (255, 0, 0), outline, 2)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = not click
            if event.button == 4:
                if step > .4:
                    step -= .2
            if event.button == 5:
                if step < 8:
                    step += .2

    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    mainClock.tick(60)