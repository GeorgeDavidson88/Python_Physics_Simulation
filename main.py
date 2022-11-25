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
    return body


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

    # sagments
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

    circle(WHITE, math.pi * 16 ** 2, 0.8, 0.4, 16, 64, 28, pymunk.Body.DYNAMIC)
    circle(WHITE, math.pi * 32 ** 2, 1, 0.4, 32, 685, 110, pymunk.Body.DYNAMIC)
    circle(WHITE, math.pi * 26 ** 2, 1, 0.4, 26, 120, 443, pymunk.Body.DYNAMIC)
    circle(BLACK, math.pi * 8 ** 2, 0.8, 0.4, 8, 740, 380, pymunk.Body.STATIC)
    circle(BLACK, math.pi * 8 ** 2, 0.8, 0.4, 8, 769, 425, pymunk.Body.STATIC)
    circle(BLACK, math.pi * 8 ** 2, 0.8, 0.4, 8, 730, 480, pymunk.Body.STATIC)
    circle(BLACK, math.pi * 8 ** 2, 0.8, 0.4, 8, 769, 525, pymunk.Body.STATIC)
    circle(BLACK, math.pi * 8 ** 2, 0.8, 0.4, 8, 730, 580, pymunk.Body.STATIC)
    circle(WHITE, math.pi * 32 ** 2, 0.8, 0.4, 32,
           WIN_WIDTH - 24, 360, pymunk.Body.STATIC)

    rect(BLUE, math.pi * (12 * 64) ** 2, 0.4, 1,
         12, 64, 349, 294, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 96) ** 2, 0.4, 1,
         12, 96, 397, 294, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 128) ** 2, 0.4, 1,
         12, 128, 445, 294, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 160) ** 2, 0.4, 1,
         12, 160, 493, 246, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 192) ** 2, 0.4, 1,
         12, 192, 541, 246, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 224) ** 2, 0.4, 1,
         12, 224, 589, 200, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 32) ** 2, 0.4, 1,
         12, 64, 590, 434, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 32) ** 2, 0.4, 1,
         12, 64, 542, 434, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 32) ** 2, 0.4, 1,
         12, 64, 494, 434, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 32) ** 2, 0.4, 1,
         12, 64, 446, 434, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 32) ** 2, 0.4, 1,
         12, 64, 398, 434, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 32) ** 2, 0.4, 1,
         12, 64, 350, 434, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 32) ** 2, 0.4, 1,
         12, 64, 302, 434, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 32) ** 2, 0.4, 1,
         12, 64, 254, 434, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 32) ** 2, 0.4, 1,
         12, 64, 206, 434, pymunk.Body.DYNAMIC)
    rect(BLUE, math.pi * (12 * 32) ** 2, 0.4, 1,
         12, 64, 158, 434, pymunk.Body.DYNAMIC)

    pivot(10000, 0.8, 5, (-194, 0), (194, 0), (977, 290))
    pivot(1000, 0.8, 5, (-62, 0), (125, 0), (140, 600))
    pivot(1000, 0.8, 5, (-100, 0), (100, 0), (340, 586))

    for i in range(25):
        circle((random.randint(0, 255), random.randint(0, 255), random.randint(
            0, 255), 255), 10, 0.8, 0.4, 8, WIN_WIDTH - 48, 48, pymunk.Body.DYNAMIC)

    for i in range(25):
        circle((random.randint(0, 255), random.randint(0, 255), random.randint(
            0, 255), 255), 10, 0.8, 0.4, 8, 244, 500, pymunk.Body.DYNAMIC)

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
