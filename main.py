import pymunk.pygame_util
import pymunk
import pygame
import random
import math
import sys
import os

pygame.init()

# display settings
WIN_WIDTH = 1200
WIN_HEIGHT = 816
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("Physic Simulation")

pygame.display.set_icon(pygame.image.load(
    os.path.join("graphics", "atom.png")).convert_alpha())

# colors
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
BLUE = (0, 0, 255, 255)
GRAY = (48, 48, 48, 255)
BLACK = (0, 0, 0, 255)

# setting up space
pymunk.pygame_util.positive_y_is_up = False
space = pymunk.Space()
space.gravity = (0, 781)

draw_options = pymunk.pygame_util.DrawOptions(WIN)


def circle(color, mass, elasticity, friction, radius, pos_x, pos_y, body_type):
    body = pymunk.Body(body_type=body_type)
    body.position = (pos_x, pos_y)

    shape = pymunk.Circle(body, radius)
    shape.color = color
    shape.mass = mass
    shape.elasticity = elasticity
    shape.friction = friction

    space.add(body, shape)


def rect(colour, mass, elasticity, friction, width, height, pos_x, pos_y, body_type):
    body = pymunk.Body(body_type=body_type)
    body.position = (pos_x, pos_y)

    shape = pymunk.Poly.create_box(body, (width, height))
    shape.color = colour
    shape.mass = width * height
    shape.elasticity = elasticity
    shape.friction = friction

    space.add(body, shape)


def sagment(colour, mass, elasticity, friction, radius, start_pos, end_pos, body_type):
    body = pymunk.Body(body_type=body_type)

    shape = pymunk.Segment(body, start_pos, end_pos, radius)
    shape.color = colour
    shape.mass = mass
    shape.elasticity = elasticity
    shape.friction = friction

    space.add(body, shape)


def pivot(mass, friction, radius, length_left, length_right, pos):
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = pos

    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Segment(body, length_left, length_right, radius)
    shape.mass = mass
    shape.friction = friction

    rotation_center_joint = pymunk.PinJoint(
        body, rotation_center_body, (0, 0), (0, 0))

    space.add(shape, body, rotation_center_joint)


def main():

    # windown borders
    rect(BLACK, 1, 0.8, 0.4, WIN_WIDTH, 24,
         WIN_WIDTH / 2, WIN_HEIGHT - 12, pymunk.Body.STATIC)
    rect(BLACK, 1, 0.8, 0.4, WIN_WIDTH,
         24, WIN_WIDTH / 2, 12, pymunk.Body.STATIC)
    rect(BLACK, 1, 0.8, 0.4, 24, WIN_HEIGHT,
         12, WIN_HEIGHT / 2, pymunk.Body.STATIC)
    rect(BLACK, 1, 0.8, 0.4, 24, WIN_HEIGHT,
         WIN_WIDTH - 12, WIN_HEIGHT / 2, pymunk.Body.STATIC)

    sagment(RED, 100, 0.8, 0.4, 10, (48, 144), (222, 170), pymunk.Body.STATIC)
    sagment(RED, 100, 0.8, 0.4, 10, (180, 255), (365, 198), pymunk.Body.STATIC)
    sagment(RED, 100, 0.8, 0.4, 10, (48, 274), (222, 331), pymunk.Body.STATIC)
    sagment(BLACK, 100, 0.8, 0.4, 10, (222, 331),
            (595, 331), pymunk.Body.STATIC)
    sagment(BLACK, 100, 0.8, 0.4, 10, (685, 144),
            (800, 144), pymunk.Body.STATIC)
    sagment(BLACK, 100, 0.8, 0.4, 10, (818, 364),
            (818, 580), pymunk.Body.STATIC)
    sagment(BLACK, 100, 0.8, 0.4, 10, (680, 388),
            (680, 580), pymunk.Body.STATIC)
    sagment(BLACK, 100, 0.8, 0.4, 10, (592, 477),
            (100, 477), pymunk.Body.STATIC)
    sagment(BLACK, 100, 0.8, 0.4, 10, (592, 477),
            (592, 600), pymunk.Body.STATIC)
    sagment(BLACK, 100, 0.8, 0.4, 10, (900, 700),
            (502, 640), pymunk.Body.STATIC)
    sagment(BLACK, 100, 0.8, 0.4, 10, (100, 640),
            (502, 640), pymunk.Body.STATIC)
    sagment(BLACK, 100, 0.8, 0.4, 10, (0, 740),
            (900, WIN_HEIGHT), pymunk.Body.STATIC)
    sagment(BLACK, 100, 0.8, 0.4, 10, (WIN_WIDTH - 24, 340),
            (WIN_WIDTH - 32, 340), pymunk.Body.STATIC)
    sagment(BLACK, 100, 0.8, 0.4, 10, (WIN_WIDTH, 300),
            (WIN_WIDTH - 20, 200), pymunk.Body.STATIC)

    circle(WHITE, math.pi * 16 ** 2, 0.8, 0.4, 16, 64, 28, pymunk.Body.DYNAMIC)
    circle(WHITE, math.pi * 32 ** 2, 0.8, 0.4,
           32, 685, 110, pymunk.Body.DYNAMIC)
    circle(WHITE, math.pi * 26 ** 2, 0.8, 0.4,
           26, 120, 443, pymunk.Body.DYNAMIC)

    x = 740
    y = 380
    z = 30
    for i in range(5):
        circle(BLACK, math.pi * 8 ** 2, 0.8, 0.4, 8, x, y, pymunk.Body.STATIC)
        z = z * -1
        x = x - z
        y = y + 48

    x = 300
    y = 294
    z = 64
    for i in range(6):
        x = x + 48
        z = z + 32
        y = y - 20
        rect(BLUE, math.pi * (12 * 64) ** 2, 0.4,
             1, 12, z, x, y, pymunk.Body.DYNAMIC)

    x = 637
    for i in range(10):
        x = x - 48
        rect(BLUE, math.pi * (12 * 32) ** 2, 0.4, 1,
             12, 64, x, 434, pymunk.Body.DYNAMIC)

    pivot(10000, 0.8, 5, (-194, 0), (194, 0), (977, 300))
    pivot(1000, 0.8, 5, (-60, 0), (125, 0), (140, 600))
    pivot(1000, 0.8, 5, (-100, 0), (100, 0), (340, 586))

    for i in range(25):
        circle((random.randint(0, 255), random.randint(0, 255), random.randint(
            0, 255), 255), 10, 0.4, 1, 8, WIN_WIDTH - 48, 48, pymunk.Body.DYNAMIC)

    for i in range(24):
        circle((random.randint(0, 255), random.randint(0, 255), random.randint(
            0, 255), 255), 10, 0.4, 0.4, 8, 244, 500, pymunk.Body.DYNAMIC)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WIN.fill(GRAY)  # draw the background

        space.step(0.002)  # updating the physics

        space.debug_draw(draw_options)  # drawing the shapes

        pygame.display.update()  # updating the display


if __name__ == "__main__":
    main()
