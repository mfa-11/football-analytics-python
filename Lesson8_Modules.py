import math
print(math.pi)

import random
print(random.randint(1, 10))

import numpy as np
print(np.arange(0, 10, 2))

directions = ['Left', 'Middle', 'Right']
keeper = random.choice(directions)
print('The keeper dived: ' + keeper)

goals = np.array([2, 1, 0, 3, 1])
print(goals * 2)