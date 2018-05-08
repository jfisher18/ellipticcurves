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

def pollard(n,b):
  a=2
  for j in range(2,b+1):
    a=(pow(a,j))%n
    d=gcd(a-1,n)
    if (1<d) and (d<n):
      return d
  return 0