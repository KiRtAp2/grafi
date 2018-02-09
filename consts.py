import pygame
import settings_loader

settings_loader.load()  # naloži settings.json

from settings_loader import settings

if not pygame.font.get_init():
    pygame.font.init()

WWIDTH = settings["window_width"]  # širina okna
WHEIGHT = settings["window_height"]  # višina okna
#spreminjanje teh števil bo vplivalo na izgled grafa in okna


# graf je le del okna, zato potrebuje svojo širino in višino
GWIDTH = WWIDTH * 0.95
GHEIGHT = WHEIGHT * 0.95
# spreminjanje teh števil bo vplivalo na velikost grafa v oknu


FONT = pygame.font.SysFont(settings["font_name"], settings["font_size"],
                           settings["font_bold"], settings["font_italic"])
# font, s katerim bo izpisano besedilo in števila

# števila, ki vplivajo na izačune točk
GRAPHSTART = settings["start_graph_number"]  # število v sredini grafa
GRAPH_MAX_X = settings["max_graph_number_x"]  # največje prikazano število v osi x
GRAPH_MAX_Y = settings["max_graph_number_y"]  # največje prikazano število v osi y
GRAPHINTERVAL = settings["interval"]  # interval med točkami. Računalnik bo točko izračunal vsakih GRAPHINTERVAL števil
# manjše število pomeni lepši graf


GUNIT_SIZE_Y = GHEIGHT / ((GRAPH_MAX_Y - GRAPHSTART) * 2 + 1)  # velikost ene enote v pikslih
GUNIT_SIZE_X = GWIDTH / ((GRAPH_MAX_X - GRAPHSTART) * 2 + 1)  # velikost ene enote v pikslih
# NE SPREMINJAJTE, RAZEN ČE VESTE KAJ DELATE


LINE_START_Y = (WWIDTH * 0.5, WHEIGHT * 0.02)  # začetna pozicija osi y
LINE_START_X = (WWIDTH * 0.02, LINE_START_Y[1] + GHEIGHT / 2)  # začetna pozicija osi x
LINE_WIDTH = settings_loader.settings["line_width"]  # debelina osi v pikslih
# števila bodo spremenila pozicije osi x in y


DO_SHOW_NUMBERS = settings["show_numbers"]  # ali naj računalnik pokaže pomožna števila
SHOW_MULTIPLES_OF = settings_loader.settings["show_multiples_of"]  # računalnik bo pomožno število prikazal le, če je deljivo z show_multiples_of

DO_SHOW_HELP_LINES = settings_loader.settings["show_help_lines"]  # ali naj računalnik pokaže pomožne črte
HELP_LINE_WIDTH = settings_loader.settings["help_line_width"]  # debelina pomožnih črt v pikslih
