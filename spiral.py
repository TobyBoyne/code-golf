r,m=range(10),min
for y in r:
 for x in r:
  X,Y=m(x,9-x),m(y,9-y)
  s=m(X,Y)
  d,j=abs(s-x)+abs(s-y),s-y<s-x
  print(f'{[0,36,64,84,96,100][s+j]+d-2*d*j:2}',end='\n '[x<9])