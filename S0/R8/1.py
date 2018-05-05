def tlow8(x):
  #Simple Lagrange Interpolation
  y =  x    * 113560967/140529378
  y += x**2 * -840075727/4684312600
  y += x**3 * 353956319/28105875600
  y += x**4 * 242827/9368625200
  return round(y)
