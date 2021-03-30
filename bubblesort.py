# worst case O(n^2)

def bubble(list):
	length = len(list) -1
	sorted = False

	while not sorted:
		sorted = True
		for i in range(0, length):
			if list[i] > list[i+1]:
				sorted = False
				list[i], list[i+1] = list[i+1], list[i]
	return list

print(bubble([4,6,8,3,4,5,8,9]))
