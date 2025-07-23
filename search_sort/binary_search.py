arr = [-1, 0, 3, 5, 9, 12]
target = 9

left = 0
right = len(arr) - 1

while left <= right:
    middle = (left + right) // 2
    if arr[middle] == target:
        print(target)
       # break
    elif arr[middle] < target:
    	left = middle + 1
    elif arr[middle] > target:
    	right = middle - 1
    	
