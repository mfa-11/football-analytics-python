PlayerOne = {'Name': 'Haaland','Number': 9, 'Long Sleeves': True}
print(PlayerOne)
print(PlayerOne['Number'])
PlayerOne['Goals'] = 20
print(PlayerOne)
PlayerOne['Goals'] += 1
print(PlayerOne['Goals'])
PlayerOne['Long Sleeves'] = False
print(PlayerOne)
del PlayerOne['Long Sleeves']
print(PlayerOne)
PlayerOne.clear()
print(PlayerOne)