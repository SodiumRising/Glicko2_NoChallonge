#Import something
from glicko2 import *

def main():

    playerList = createPlayers()
    tournamentData = getTournamentData()
    glicko2Data = prepareData(playerList, tournamentData)
    calculate(playerList, glicko2Data)


def createPlayers():

    #Variables
    playerList = []

    #Open player text file that contains name, rating, rd, vol
    ratingFile = open("players.txt", "r")

    #Read lines from file and store into a list
    lines = ratingFile.readlines()

    for line in lines:
        #Remove \n character
        line = line.strip()
        #Split based on semicolon
        strippedLine = line.split(';')
        #Create player object based on the split
        player = Player(strippedLine[0],float(strippedLine[1]),float(strippedLine[2]),float(strippedLine[3]))
        #Add new player to list 
        playerList.append(player)

    ratingFile.close()
    
    return playerList


def getTournamentData():

    #Variables
    dataList = []

    #Open player text file that contains name, rating, rd, vol
    dataFile = open("tournament.txt", "r")

    #Read lines from file and store into a list
    lines = dataFile.readlines()

    for line in lines:
        #Remove \n character
        line = line.strip()
        #Split based on semicolon
        strippedLine = line.split(';')
        #Create player object based on the split
        data = Data(strippedLine[0],strippedLine[1],strippedLine[2])
        #Add new player to list 
        dataList.append(data)

    dataFile.close()

    return dataList


def prepareData(playerList, tournamentData):

    cpOpponents = []
    cpRatings = []
    cpRDs = []
    cpOutcomes = []
    glicko2Data = []

    #Separate each entry to a variable/list
    for entry in tournamentData:

        splitOpponent = entry.opponents.split(',')
        splitOutcomes = entry.outcomes.split(',')
        cpOpponents.append(splitOpponent)

        #convert outcomes to ints
        for x in splitOutcomes:

            cpOutcomes.append(int(x))

        #Separate by each players matches
        for matches in cpOpponents:
            
            #Separate by each opponent per series of matches
            for opponent in matches:

                #Iterate through playerList to find current opponent
                for player in playerList:

                    if opponent == player.username:

                        cpRatings.append(float(player.rating))
                        cpRDs.append(float(player.rd))
                    

            g2d = Glicko2Data(entry.player, cpRatings, cpRDs, cpOutcomes)
            glicko2Data.append(g2d)
            cpRatings = []
            cpRDs = []
            cpOutcomes = []
    
        cpOpponents = []
    
    return glicko2Data


def calculate(playerList, glicko2Data):

    foundList = []

    #open('players.txt', 'w').close()
    ratingsFile = open('players.txt', 'w')

    #iterate by player through playerList
    for player in playerList:

        #Iterate through glicko2Data to line up key with current player
        for p in glicko2Data:

            if player.username == p.username:
                foundList.append(player.username)
                player.update_player(p.rating, p.rd, p.outcome)
                ratingsFile.write("{0};{1};{2};{3}\n".format(player.username,player.rating,player.rd,player.vol))
                print("{0}\nNew Rating: {1}, New RD: {2}, New Vol: {3}".format(player.username,player.rating,player.rd,player.vol))
        

    #Write remaining Players back into file
    for player in playerList:

        if (player.username not in foundList):

            ratingsFile.write("{0};{1};{2};{3}\n".format(player.username,player.rating,player.rd,player.vol))
            print("{0}\nRating: {1}, RD: {2}, Vol: {3}".format(player.username,player.rating,player.rd,player.vol))
    
    ratingsFile.close()


class Data:

    def __init__(self, player, opponents, outcomes):

        self.player = player
        self.opponents = opponents
        self.outcomes = outcomes

class Glicko2Data:

    def __init__(self, username, rating, rd, outcome):

        self.username = username
        self.rating = rating
        self.rd = rd
        self.outcome = outcome


if __name__ == "__main__":

    main()

"""
Notes on how to implement without Challonge or Smash.gg API

--How to save players' scores--
Store data in Notepad with semicolon separated values

--How to record tournament results--
Separate by something like username;opponent1,opponent2;result1,result2
Separate sections by semicolon, then each result in the section by commas

Should I have the code ask who played who and who won so it's more automated and less room for errors?
"""