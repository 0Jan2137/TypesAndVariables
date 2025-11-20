# Distance to the horizon from height h (meters), result in km
import math

h = float(input("Enter height in meters: "))
d = 3.57 * math.sqrt(h)
print(f"Distance to horizon: {d:.2f} km")
