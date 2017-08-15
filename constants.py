import pygame
import settings_loader

settings_loader.load() # naloži settings.json

if not pygame.font.get_init():
    pygame.font.init()

window_width = settings_loader.settings["window_width"]  # širina okna
window_height = settings_loader.settings["window_height"]  # višina okna
#spreminjanje teh števil bo vplivalo na izgled grafa in okna

# graf je le del okna, zato potrebuje svojo širino in višino
graph_height = window_height*0.95
graph_width = window_width*0.95
# spreminjanje teh števil bo vplivalo na grafu dostopno polje


font = pygame.font.SysFont(settings_loader.settings["font_name"], settings_loader.settings["font_size"],
                           settings_loader.settings["font_bold"], settings_loader.settings["font_italic"])
# font s katerim bo izpisano besedilo in števila

# števila, ki vplivajo na izačune točk
start_graph_number = settings_loader.settings["start_graph_number"]  # število v sredini grafa
max_graph_number_x = settings_loader.settings["max_graph_number_x"]  # največje prikazano število v osi x
max_graph_number_y = settings_loader.settings["max_graph_number_y"]  # največje prikazano število v osi y
graph_calculation_interval = settings_loader.settings["interval"]  # interval med točkami. Računalnik bo točko izračunal vsakih graph_calculation_interval števil
                                   # manjše število pomeni lepši graf



graph_unit_size_y = graph_height / ((max_graph_number_y - start_graph_number)*2+1)  # velikost ene enote v pikslih
graph_unit_size_x = graph_width / ((max_graph_number_x - start_graph_number)*2+1)  # velikost ene enote v pikslih
# NE SPREMINJAJTE, RAZEN ČE VESTE KAJ DELATE


line_y_start = (window_width*0.5, window_height*0.02)  # začetna pozicija osi y
line_x_start = (window_width*0.02, line_y_start[1]+graph_height/2)  # začetna pozicija osi x
line_width = settings_loader.settings["line_width"] # debelina osi v pikslih
# števila bodo spremenila pozicije osi x in y


show_numbers = settings_loader.settings["show_numbers"]  # ali naj računalnik pokaže pomožna števila
show_multples_of = settings_loader.settings["show_multiples_of"]  # računalnik bo pomožno število prikazal le, če je deljivo z show_multiples_of

show_help_lines = settings_loader.settings["show_help_lines"]  # ali naj računalnik pokaže pomožne črte
help_line_width = settings_loader.settings["help_line_width"]  # debelina pomožnih črt v pikslih
