import yaml

class Menu():
    config = yaml.safe_load(open("config.yaml"))

    print("Baboucoin")