# best O(n) worst O(n^2)
def insertion(list):
	indexing_length = range(1, len(list))

	for i in indexing_length:
		value_to_sort = list[i]

		# i>0 because python allows negative indexing
		while list[i-1] > value_to_sort and i>0:
			list[i], list[i-1] = list[i-1], list[i]

			i = i-1;

	return list

print(insertion([4,5,8,3,1,4,6,9]))