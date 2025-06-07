def getReverse(num):
  num_copy = num
  num = abs(num)
  rev = 0
  while num > 0:
    rem = num % 10
    rev = (10*rev) + rem
    num = num // 10
  
  limit = 2**31
  if rev < -limit or rev > limit-1: return 0
  if num_copy < 0:
    return -rev
  return rev
  
print(getReverse(-1534236469))
