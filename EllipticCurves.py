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

print(pollard(5917,5,1))