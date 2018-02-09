import func
import consts
import pygame
from sys import exit as quit
import colors


#ustvari okno
window = pygame.display.set_mode((consts.WWIDTH, consts.WHEIGHT))


def draw_lines():
    """Nariši osi x in y"""

    # os y
    pygame.draw.rect(
        window,  # kje
        colors.GRAY,  # barva v rgb formatu
        (consts.LINE_START_Y[0], consts.LINE_START_Y[1], consts.LINE_WIDTH, consts.GHEIGHT)
        # tuple z informacijami: (zacetni_x, zacetni_y, velikost_x, velikost_y)
    )

    # os x
    pygame.draw.rect(
        window,
        colors.GRAY,
        (consts.LINE_START_X[0], consts.LINE_START_X[1], consts.GWIDTH, consts.LINE_WIDTH)
    )


def draw_points(f=func.f, color=colors.BLACK):
    """Nariši točke grafa"""

    x = -consts.GRAPH_MAX_X
    while x <= consts.GRAPH_MAX_X:
        try:
            y = f(x)

        except ZeroDivisionError:
            pass  # ni potrebno risati točke, ker primanjklaj nebi smel biti opazen

        else:
            rect = (
                x*consts.GUNIT_SIZE_X+consts.LINE_START_Y[0]+consts.LINE_WIDTH,
                consts.LINE_START_X[1]-(y*consts.GUNIT_SIZE_Y),
                2,
                3
            )
            if abs(y) <= consts.GRAPH_MAX_Y:
                pygame.draw.rect(
                    window,
                    color,
                    rect
                )

        finally:
            x += consts.GRAPHINTERVAL


def show_utils(font):
    """Pokaži številke in črte ob grafu"""

    for i in range(-consts.GRAPH_MAX_Y+1, consts.GRAPH_MAX_Y):
        if not i % consts.SHOW_MULTIPLES_OF:

            surf = font.render(str(i), True, colors.BLACK)

            pos = (
                consts.LINE_START_Y[0]-45,
                consts.LINE_START_X[1] - i*consts.GUNIT_SIZE_Y
            )

            window.blit(surf, pos)

            if consts.DO_SHOW_HELP_LINES:
                pygame.draw.rect(
                    window,
                    colors.LIGHTGRAY,
                    (0, consts.LINE_START_X[1] - i * consts.GUNIT_SIZE_Y, consts.WWIDTH, consts.HELP_LINE_WIDTH)
                )

    for i in range(-consts.GRAPH_MAX_Y, consts.GRAPH_MAX_X+1):
        if not i % consts.SHOW_MULTIPLES_OF:

            surf = font.render(str(i), True, colors.BLACK)

            pos = (
                consts.LINE_START_Y[0] + i * consts.GUNIT_SIZE_X,
                consts.LINE_START_X[1]+10
            )

            window.blit(surf, pos)

            if consts.DO_SHOW_HELP_LINES:
                pygame.draw.rect(
                    window,
                    colors.LIGHTGRAY,
                    (
                        consts.LINE_START_Y[0] + i * consts.GUNIT_SIZE_X,
                        0,
                        consts.HELP_LINE_WIDTH,
                        consts.WHEIGHT
                    )
                )


def main():

    window.fill(colors.WHITE)
    draw_lines()
    print("Done drawing lines")
    if consts.DO_SHOW_NUMBERS:
        show_utils(consts.FONT)
        print("Done drawing numbers")

    # add more draw_points commands to see more graphs
    draw_points(f=func.f, color=colors.BLACK)
    print("Done drawing points")

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


if __name__ == '__main__':
    pygame.init()
    main()