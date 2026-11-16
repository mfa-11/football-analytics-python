City = ['Doku', 'Haaland', 'Anderson']
print(City [0 : 2])
print(City [0])
print(City[2])
City.append('Cherki')
print(City)

CityGoals = [2, 1, 0, 3, 1]
OppGoals = [0, 1, 2, 1, 1]
Points = 0
for i in range(5):
    if CityGoals[i] > OppGoals[i]:
        Points += 3
    elif CityGoals[i] == OppGoals[i]:
        Points += 1
print('City points: ' + str(Points))


CityGoals = [2, 1, 0, 3, 1]
OppGoals = [0, 1, 2, 1, 1]
GD = 0
for i in range(5):
    GD += (CityGoals[i] - OppGoals[i])
print('City Goal difference: ' + str(GD))    
CityGoals.append(4)
OppGoals.append(0)
CityGoals.reverse()
OppGoals.reverse()
print(CityGoals[0:3])
print(OppGoals[0:3])