s = ["A","B","C","D","E"]

def reverseString(arr):
  n = len(s)

  for i in range(n//2):
    s[i],s[n-1-i]=s[n-1-i],s[i]
  return s

print(reverseString(s))
