def doubleMe(number):
    return number * 2
print(doubleMe(5))

def points(wins):
    return wins * 3
print(points(25))

def conversion(goals, shots):
    return goals / shots
print(conversion(15, 45))

def keeperrating(numofsaves):
    if numofsaves > 5:
        return 'Excellent'
    else:
        return 'Average'  
print(keeperrating(7))  
print(keeperrating(2))  

def result(our_goals, their_goals):
    if our_goals > their_goals:
        return 'win'
    elif our_goals < their_goals:
        return 'loss'
    else:
        return 'draw'
print(result(2, 1))    
print(result(2, 4))
print(result(2, 2))



