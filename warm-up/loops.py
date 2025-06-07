print("----------")

def findElement(arr, element):
  for i in range(len(arr)):
    if element == arr[i]:
      return i
  return -1
      
      
#print(findElement([1,2,3,4,5,6,11,3,5], 12))

def countNegative(arr):
  count = 0
  for i in range(len(arr)):
    if arr[i] < 0:
      count = count + 1
  return count
  
#print(countNegative([0, -1, -3, 6, 9, -5, 3, 9]))


def findLargest(arr):
  largest = arr[0]
  for i in range(len(arr)):
    if largest < arr[i]:
      largest = arr[i]
  return largest
  
#print(findLargest([0, -1, -3, 6, 9, 22, 3, 9]))

def findSmallest(arr):
  smallest = arr[0]
  for i in range(len(arr)):
    if smallest > arr[i]:
      smallest = arr[i]
  return smallest
  
#print(findSmallest([0, -1, -3, 6, 9, 22, 3, 9]))

def findSecondLargest(arr):

  if len(arr) < 2:
    return None
    
  firstLargest = float('-inf')
  secondLargest = float('-inf')
  
  for i in range(len(arr)):
    if arr[i] > firstLargest:
      secondLargest = firstLargest
      firstLargest = arr[i]
    elif arr[i] > secondLargest and arr[i] != firstLargest:
      secondLargest = arr[i]
  return secondLargest
  
##print(findSecondLargest([0, -1, -3, 6, 9, 22, 3, 9, 22]))

def getDigitCount(n):
  n = abs(n)
  if n == 0:
    return 1
  count = 0
  while n > 0:
    n = n//10
    #print(n)
    count = count + 1
  return count

print(getDigitCount(-11223456))
