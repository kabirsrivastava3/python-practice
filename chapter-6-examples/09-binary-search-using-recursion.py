#binary search using recursion

def binarySearch (arr, start, end, element):

	# Check base case
	if end >= start:

		mid = start + (end - start) // 2

		# If element is present at the middle itself
		if arr[mid] == element:
			return mid
		
		# If element is smaller than mid, then it
		# can only be present in left subarray
		elif arr[mid] > element:
			return binarySearch(arr, start, mid-1, element)

		# Else the element can only be present
		# in right subarray
		else:
			return binarySearch(arr, mid + 1, end, element)

	else:
		# Element is not present in the array
		return -1

# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
element = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, element)

if result != -1:
	print ("Element is present at index % d" % result)
else:
	print ("Element is not present in array")