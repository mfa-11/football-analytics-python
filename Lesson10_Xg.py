import random
if random.random() <= 0.21:
    print('GOOOAL')
else:
    print('Missed')    


Goals = 0 
for i in range (0, 10000):    
    if random.random() <= 0.21:
        Goals += 1
print(Goals)        


HomeXG = [0.21, 0.66, 0.1, 0.14, 0.01]
AwayXG = [0.04, 0.06, 0.01, 0.06, 0.12, 0.01, 0.06]
def testShots(shots):
    Goals = 0
    for shot in shots:
        if random.random() <= shot:
            Goals += 1
    return Goals
print(testShots(HomeXG))    
print(testShots(AwayXG))    


def calculateWinner(home, away):
    HomeGoals = testShots(home)
    AwayGoals = testShots(away)
    if HomeGoals > AwayGoals:
        return 'home'
    elif AwayGoals > HomeGoals:
        return 'away'
    else:
        return 'draw'
print(calculateWinner(HomeXG, AwayXG))

def calculateChance(team1, team2):
    home = 0
    away = 0
    draw = 0
    for i in range(0,10000):
        matchWinner = calculateWinner(team1, team2)
        if matchWinner == 'home':
            home += 1
        elif matchWinner == 'away':
            away += 1
        else:
            draw += 1
    print('Home wins ' + str(home/100) + '%, away wins ' + str(away/100) + '%, draw ' + str(draw/100) + '%')  
calculateChance(HomeXG, AwayXG)                

BigChance = [0.5]
SmallChance = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05,0.05, 0.05, 0.05, 0.05]
calculateChance(BigChance, SmallChance)