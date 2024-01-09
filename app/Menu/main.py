import yaml

class Menu():
    config = yaml.safe_load(open("config.yaml"))

    print(config['menu']['header'])

    if len(difficultyHex) < 64:
        while len(difficultyHex) < 64:
            difficultyHex = difficultyHex + "0"
    elif len(difficultyHex) > 64:
        awaitingMatch == False
        print("Error: Difficulty too high")