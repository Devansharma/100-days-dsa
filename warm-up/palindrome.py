def getReverse(num):
  rev = 0
  while num > 0:
    rem = num % 10
    rev = (10*rev) + rem
    num = num // 10
  return rev

def checkPalindrome(num):
  if num < 0:
    return False
  elif num == getReverse(num):
    return True
  else:
    return False

print(checkPalindrome(-121))
