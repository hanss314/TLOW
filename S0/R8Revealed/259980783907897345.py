# Uses a quartic function to join the points smoothly and (somewhat) elegantly
def polynomial(x):
  return round(2.591917115010642e-05 * (x**4)
  + 0.012593676996136708 * (x**3)
  - 0.1793381011762537 * (x**2)
  + 0.8080941409987598 * x)
