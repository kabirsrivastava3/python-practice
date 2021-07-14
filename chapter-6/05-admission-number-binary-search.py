# A list namely Adm stores admission numbers of 100 students in it, sorted in ascending order of admission numbers. 
# Write a program that takes an admission number and looks for it in list Adm using binary search technique. 
# The binary search function should use recursion in it.


def admissionNumbers(adm, element, start=0, end=99):

	if end >= start:

		mid = start + (end - start) // 2

		if adm[mid] == element:
			return mid
		
		elif adm[mid] > element:
			return admissionNumbers(adm, element, start, mid-1,)

		else:
			return admissionNumbers(adm, element, mid + 1, end)

	else:
		return -1


adm = []
size = 99
for index in range(size):
    valueAdm = int(input("Enter a list of 99 students : "))
    adm.append(valueAdm)

element = int(input("Enter an admission-number to be found : "))

result = admissionNumbers(adm, element, 0, size)

if result != -1:
	print ("Element is present at index % d" % result)
else:
	print ("Element is not present in array")

