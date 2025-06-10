arr = [3,2,2,3]
val = 3

def removeElements(arr, val):
  x = 0
  for i in range(len(arr)):
    if arr[i] != val:
      arr[x] = arr[i]
      x = x+1
  return x, arr
   
print(removeElements(arr, val))
