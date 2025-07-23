def printno(n):
  if n >= 1:
    print(n)
    n = n-1
    printno(n)
    
#printno(5)


def printfor(x, val = 1):
  if val > x:
    return
  print(val)
  val = val +1
  printfor(x, val)
printfor(4)
