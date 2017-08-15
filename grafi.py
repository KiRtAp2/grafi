import math

import func
import constants
import pygame
from sys import exit as quit
import colors

#ustvari okno
window = pygame.display.set_mode((constants.window_width, constants.window_height))

def draw_lines():
    """Funkcija izriše osi x in y"""

    pygame.draw.rect( # os y
        window, # kje
        colors.gray, # barva v rgb formatu

        # tuple z informacijami: (zacetni_x, zacetni_y, velikost_x, velikost_y)
        (constants.line_y_start[0], constants.line_y_start[1], constants.line_width, constants.graph_height)
    )

    pygame.draw.rect( # os x
        window,
        colors.gray,
        (constants.line_x_start[0], constants.line_x_start[1], constants.graph_width, constants.line_width)
    )


def draw_points(f=func.f, color=colors.black):
    """Funkcija izriše točke v grafu, vzame en argument - funkcijo f"""

    x = constants.start_graph_number # nastavi začetko vrednost na constants.start_graph_number
    while x < constants.max_graph_number_x:
        y = f(x) # izračuna y

        if abs(y) <= constants.max_graph_number_y: # če y ni prevelik, ga izriše
            pygame.draw.rect(
                window,
                color,
                (x*constants.graph_unit_size_x+constants.line_y_start[0]+constants.line_width, constants.line_x_start[1]-(y*constants.graph_unit_size_y), 2, 2)
            )
        else: # če y je prevelik, preneha šteti
            break
        x += constants.graph_calculation_interval # poveča x

    x = constants.start_graph_number # ponovi za negativne vrednosti x
    while x > -(constants.max_graph_number_x):
        y = f(x)

        if abs(y) <= constants.max_graph_number_y:
            pygame.draw.rect(
                window,
                color,
                (x * constants.graph_unit_size_x + constants.line_y_start[0] + constants.line_width, constants.line_x_start[1] - (y * constants.graph_unit_size_y), 2, 2)
            )
        else:
            break
        x -= constants.graph_calculation_interval


def show_numbers(font):
    """Funkcija pokaže številke ob grafu in pomožne črte"""

    start_number = font.render(str(constants.start_graph_number), True, colors.black) # prvo število je posebno
    window.blit(start_number, (constants.line_y_start[0]-20, constants.line_x_start[1]+5+constants.line_width))

    for i in range(constants.start_graph_number+1, constants.max_graph_number_y+1):
        if i%constants.show_multples_of==0:
            surf = font.render(str(i), True, colors.black)
            pos = (
                constants.line_y_start[0] - 45,
                constants.line_x_start[1]-i*constants.graph_unit_size_y,
            )
            window.blit(surf, pos)
            if constants.show_help_lines:
                pygame.draw.rect(
                    window,
                    colors.light_gray,
                    (0, constants.line_x_start[1]-i*constants.graph_unit_size_y, constants.window_width, constants.help_line_width)
                )

    for i in range(-constants.max_graph_number_y, constants.start_graph_number):
        if abs(i)%constants.show_multples_of==0:
            surf = font.render(str(i), True, colors.black)
            pos = (
                constants.line_y_start[0] - 60,
                constants.line_x_start[1] - i * constants.graph_unit_size_y,
            )
            window.blit(surf, pos)
            if constants.show_help_lines:
                pygame.draw.rect(
                    window,
                    (200, 200, 200),
                    (0, constants.line_x_start[1]-i*constants.graph_unit_size_y, constants.window_width, constants.help_line_width)
                )

    for i in range(constants.start_graph_number+1, constants.max_graph_number_x+1):
        if i%constants.show_multples_of==0:
            surf = font.render(str(i), True, (0, 0, 0))
            pos = (
                constants.line_y_start[0]+i*constants.graph_unit_size_x,
                constants.line_x_start[1]+10
            )
            window.blit(surf, pos)
            if constants.show_help_lines:
                pygame.draw.rect(
                    window,
                    (200, 200, 200),
                    (
                        constants.line_y_start[0]+i*constants.graph_unit_size_x,
                        0,
                        constants.help_line_width,
                        constants.window_height
                    )
                )

    for i in range(-constants.max_graph_number_x, constants.start_graph_number):
        if i%constants.show_multples_of==0:
            surf = font.render(str(i), True, (0, 0, 0))
            pos = (
                constants.line_y_start[0]+i*constants.graph_unit_size_x,
                constants.line_x_start[1]+10
            )
            window.blit(surf, pos)
            if constants.show_help_lines:
                pygame.draw.rect(
                    window,
                    (200, 200, 200),
                    (
                        constants.line_y_start[0]+i*constants.graph_unit_size_x,
                        0,
                        constants.help_line_width,
                        constants.window_height
                    )
                )


def main():

    window.fill(colors.white)
    draw_lines()
    if constants.show_numbers:
        show_numbers(constants.font)

    # add more draw_points commands to see more graphs
    draw_points(f=func.f, color=colors.black)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


if __name__ == '__main__':
    pygame.init()
    main()