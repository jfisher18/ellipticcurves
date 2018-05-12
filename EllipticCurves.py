import math

def gcd(a,b):
  a1=max(a,b)
  b1=min(a,b)
  a=a1
  b=b1
  r=a%b
  if(r==0):
    return b
  else:
    return gcd(a,r)

def sieve(n):
  multiples = []
  primes = []
  for i in range(2, n + 1):
    if i not in multiples:
      primes.append(i)
      for j in range(i * i, n + 1, i):
        multiples.append(j)
  return primes

def lcm_list(b):
  primes = sieve(b)
  lcm = 1
  for p in primes:
    lcm *= pow(p, math.floor(math.log(b,p)))
  return lcm

def pollard(n,b,attempts):
  m=lcm_list(b)
  a=2
  for j in range(2,2+attempts):
    x=(pow(a,m)-1)%n
    d=gcd(x,n)
    if (1<d) and (d<n):
      return d
  return 0

def elliptic_curve_addition_R(x1, y1, x2, y2, a, b):
  slope = 0
  if math.isnan(y1):
    return y2
  elif math.isnan(y2):
    return y1
  elif x1 == x2 and y1 == -y2:
    return math.nan
  elif x1 == x2 and y1 == y2:
    slope = (3 * pow(x1,2) + a) / (2 * y1)
  else:
    slope = (y1 - y2) / (x1 - x2)
  x3 = pow(slope,2) - x1 - x2
  y3 = -slope * x3 - y1 + slope * x1
  return x3, y3

def elliptic_curve_addition_finite(x1, y1, x2, y2, a, b, n):
  slope = 0
  if math.isnan(y1):
    return y2
  elif math.isnan(y2):
    return y1
  elif x1 == x2 and y1 == -y2:
    return math.nan
  elif x1 == x2 and y1 == y2:
    slope = (3 * pow(x1, 2) + a) / (2 * y1) % n
  else:
    slope = (y1 - y2) / (x1 - x2) % n
  x3 = pow(slope, 2) - x1 - x2 % n
  y3 = -slope * x3 - y1 + slope * x1 % n
  return x3, y3

