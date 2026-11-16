ManCity = ['Haaland', 'Cherki', 'Anderson','Bouaddi' ]
for player in ManCity:
    print('ManCity player: ' + player )

goals = [2, 0, 1, 3, 0]
for goal in goals:
    if goal > 0:
        print ('scored')
    else:
        print('No goal')    

players = ['Haaland', 'Cherki', 'Anderson', 'Bouaddi']
for player in players:
    if player == 'Haaland':
        print('Haaland is a striker')
    else:
        print(player + ' is a midf')


Haaland_goals = [2, 0, 1, 3, 0]      
total = 0
for goal in Haaland_goals:
    total = total + goal
print('Total goals: ' + str (total))


Haaland_goals = [2, 0, 1, 3, 0]
matches = 0
for goal in Haaland_goals:
    if goal > 0:
        matches = matches + 1
print( 'Matches scored in: ' + str (matches))        