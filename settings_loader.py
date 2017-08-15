import json

# prepares dictionary before starting
settings = {}


def read_file(file):
    global settings
    settings = json.load(file)

# Must be called first! Ensures settings will be loaded correctly
def load():
    try:
        settings_file = open("settings.json", "r")
        read_file(settings_file)
    except FileNotFoundError:
        print("File \"settings.json\" not found!\n")
        return False
