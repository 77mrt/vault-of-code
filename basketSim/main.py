# import numpy as np
# from numpy import random
import random
import datagatherer
from time import sleep


class Person:

    def __init__(self, name, team, hasBall, throwStat, defenseStat):
        self.name = name
        self.team = team
        self.hasBall = hasBall
        self.throwStat = throwStat
        self.defenseStat = defenseStat

    def __str__(self):
        return 'Player: {} \nThrowing: {} \nDefense: {}'.format(self.name, self.throwStat, self.defenseStat)

    def savePlayer(self):
        return '{} {} {} {} {}'.format(self.name, self.team, self.hasBall, self.throwStat, self.defenseStat)

    def throwBall(self):
        success = random.randint(0, 100)
        throwChance = 45 + (self.throwStat * 5)

        if self.hasBall == True:
            if success < throwChance:
                print(str(success) + " < " + str(throwChance))
                print(self.name + ' takes the shot!')
                self.hasBall = False
                return True

            else:
                print(str(success) + " > " + str(throwChance))
                print(self.name + ' fumbles!')
                self.hasBall = False
                return False
        else:
            print(self.name + ' does not have a ball!')

    def blockThrow(self):
        success = random.randint(0, 100)
        blockChance = 45 + (self.defenseStat * 5)
        #Block needs tuning. Either needs to be lower so that defense doesn't entire hold the game hostage (even when defend is bad)
        #Or offense needs another option to temporarily circumvent defence
        if success < blockChance:
            print(str(success) + " < " + str(blockChance))
            print(self.name + ' blocks the shot!')
            return True
        elif success > blockChance:
            print(str(success) + " > " + str(blockChance))
            print(self.name + ' whiffs!')
            return False

#generates name and stats for a new player
def genPlayer(team):
    randThrow = random.randint(1, 5)
    randDefense = random.randint(1, 5)
    f = open(r'C:\Users\liter\Documents\GitHub\vault-of-code\basketSim\playernames.txt')
    name = f.readlines()
    randpick = random.randint(0, len(name) - 1)
    print(randpick)  # delete later
    myPerson = Person(name[randpick].rstrip(), team, False, randThrow, randDefense)
    f.close()
    return myPerson

#generates new list of players for a selected team
def genTeam():
    f = open(r"C:\Users\liter\Documents\GitHub\vault-of-code\basketSim\teamnames.txt")
    team = f.readlines()
    # randpick = random.randint(len(team))
    tName = ""
    r = 1
    for i in team:
        print(str(r) + ". " + i)
        r += 1

    errorCheck = False
    while not errorCheck:
        pick = int(input("Select a team: "))
        if len(team) < pick <= 0:
            print("Not a team. Select again.")
        else:
            #needs an error catcher here in case that file selected is empty
            print(team[pick - 1])
            tName = team[pick - 1].rstrip()
            errorCheck = True

    newFile = "C:/Users/liter/Documents/GitHub/vault-of-code/basketSim/teamslog/" + tName + ".txt"
    i = 0
    t = open(newFile, 'w')
    while i < 3:
        addPlayer = genPlayer(tName)
        t.write(addPlayer.savePlayer() + "\n")
        i += 1
    t.close()
    t2 = open(newFile, 'r')
    roster = t2.readlines()
    f.close()
    print(roster)

#returns list of players on an existing team txt file
def readTeamFromFile(teamName):
    newFile = "C:/Users/liter/Documents/GitHub/vault-of-code/basketSim/teamslog/" + teamName + ".txt"
    f = open(newFile, 'r')
    list = f.readlines()
    i = 0
    teamlist = []
    while i < 3:
        parse = list[i].split()
        currPlayer = Person(parse[0], parse[1], bool(parse[2]), int(parse[3]), int(parse[4]))
        teamlist.append(currPlayer)
        i += 1
    return teamlist

#save stat changes to players
def saveTeamToFile(teamList):
    teamFile = "C:/Users/liter/Documents/GitHub/vault-of-code/basketSim/teamslog/" + teamList[0].team + ".txt"
    f = open(teamFile, 'w')
    for player in teamList:
        f.write(player.savePlayer() + "\n")
    f.close()

#rewards for winning
def statIncrease(teamList):
    for player in teamList:
        blessing = random.random()
        print(blessing)  # delete later
        if blessing > 0.4:
            statSelect = random.randint(1,2)
            if statSelect == 1:
                throwBonus = round(random.uniform(0,0.25),4)
                print(player.name + " gains a boost to their throwing!")
                player.throwStat = throwBonus + player.throwStat
            elif statSelect == 2:
                defBonus = round(random.uniform(0, 0.25),4)
                print(player.name + " gains a boost to their defense!")
                player.defenseStat = defBonus + player.defenseStat
        else:
            print('Divinity Denied.')

def hoopsGame(Person, rounds):
    player = Person
    score = 0
    misses = 0
    cont = 0
    player.hasBall = True
    while cont < rounds:
        if player.hasBall == True:
            print(player.name + ' has the ball!')

        print(player.throwStat)

        result = player.throwBall()

        if result:
            score += 1
        elif not result:
            misses += 1

        print('Score: ' + str(score))
        print('Misses: ' + str(misses))
        player.hasBall = True
        cont += 1
        sleep(3)
        print('')

    if score < misses:
        print(player.name + ' loses!')
    elif score > misses:
        print(player.name + ' wins!')
    else:
        print('Disapointing')


def hoopsGame2(offPlayer, defPlayer):
    score = 0
    rounds = 0
    # time is in seconds
    time = 60
    offPlayer.hasBall = True
    while time > 0:
        if offPlayer.hasBall:
            print(offPlayer.name + ' has the ball!')
        else:
            print(offPlayer.name + ' does not have the ball!')
            break

        offense = offPlayer.throwBall()
        defense = defPlayer.blockThrow()

        if offense and defense:
            print(defPlayer.name + ' saves it! The game continues.')
            offPlayer.hasBall = True
            time -= 3
        elif offense and not defense:
            print(offPlayer.name + ' scores!')
            score += 1
            offPlayer.hasBall = True
            time -= 3
        elif not offense and defense:
            print(defPlayer.name + ' grabs the ball! ' + defPlayer.name + ' passes it back.')
            offPlayer.hasBall = True
            time -= 3
        elif not offense and not defense:
            print('The ball is wild!')
            randBasket = random.randint(0,100)
            if randBasket > 95:
                print('The ball falls in anyway. ' + offPlayer.team + ' scores!')
                score += 1
                time -= 3
            else:
                print('The ball falls out of bounds.')
                time -= 3
            offPlayer.hasBall = True

        if score == 3:
            print(offPlayer.team + ' wins!')
            off_team = [offPlayer]
            print(offPlayer.name + ' is granted an increase!')
            statIncrease(off_team)
            break

        rounds += 1
        #datagatherer.collectHoopsGame2(offense,defense,score,True)
        print('Round: ' + str(rounds))
        print('Score: ' + str(score))
        print('Time Remaining: 00:' + str(time) + ' seconds')
        sleep(3)
        print('')
    if score < 3 and time == 0:
        print(defPlayer.team + ' wins!')
        def_team = [defPlayer]
        print(defPlayer.name + ' is granted an increase!')
        statIncrease(def_team)
    #datagatherer.resultHoopsGame2()
    print('Game Over')

def main():
    player1 = Person('Cal', 'off_team', False, 1, 1)
    print(player1.name + ' enters the Court.')
    print(player1.__str__())

    player2 = Person('Ibis', 'def_team', False, 1, 1)
    print(player2.name + ' enters the Court.')
    print(player2.__str__())
    print('')

    hoopsGame2(player1, player2)
    # hoopsGame(player,10)

    # print(player.__str__())
    # genTeam()

    #team1 = readTeamFromFile('Rockets')
    #statIncrease(team1)
    #i = 0
    #while i < len(team1):
    #   print(team1[i].__str__())
    #   i += 1
    #saveTeamToFile(team1)

if __name__ == '__main__':
    main()
