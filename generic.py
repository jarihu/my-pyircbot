import json

class Generic:

    def getBots(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
        return config['config']['bots']

    def getCommands(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
        return config['config']['commands']

    def getCommandServer(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
        return config['config']['commandServer']


