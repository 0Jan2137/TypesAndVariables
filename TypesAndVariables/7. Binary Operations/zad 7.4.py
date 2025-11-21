# A tree may be cut down if its diameter is at least 50 cm.
# Diameter = circumference / π

import math

circ = float(input('Enter tree circumference in cm: '))
diameter = circ / math.pi
can_cut = diameter >= 50

print(f'Tree can be cut down: {can_cut}')



#pobranie obwodu
#średnica = obwód / π
#sprawdzenie czy średnica ≥ 50
#wypisanie True/False