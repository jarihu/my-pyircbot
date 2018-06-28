import sys
import server as IrcServer
import generic as Config
import bot as IrcBot

def main():
    configs = Config.Generic()
    botConfigs = configs.getBots()
    botCommands = configs.getCommands()
    botCommandServer = configs.getCommandServer()

    minions = []    
    for botConfig in botConfigs:
        ircServer = IrcServer.Server(botConfig['server']['name'], botConfig['server']['port'], botConfig['server']['network'])
        commandServer = IrcServer.Server(botCommandServer['name'], botCommandServer['port'], botCommandServer['network'])
        minion = IrcBot.Bot(botConfig['name'], ircServer, commandServer)
        minion.connect()
        minion.joinIrcChannels(botConfig['server']['channels'])
        minion.joinCommandChannel(botCommandServer['channel'])
        minions.append(minion)

    while True:
        for minion in minions:
            #print(minion.name + " reading...")
            minion.read()

if __name__== "__main__":
  main()