def create_heap(arr, n, i):
	biggest = i #root
	left = 2 * i + 1
	right = 2 * i + 2

	#Checking if right node is greater than root
	if right < n and arr[biggest] < arr[right]:
		biggest = right

	#Checking if left node is greater than root
	if left < n and arr[biggest] < arr[left]:
		biggest = left


	if biggest != i:
		arr[i], arr[biggest] = arr[biggest], arr[i]

		create_heap(arr, n, biggest)

def heap_Sort(arr):
	n = len(arr)

	for i in range(n, -1, -1):
		create_heap(arr, n, i)

	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] #swap the first and the last node, then remove the last

		create_heap(arr, i, 0)


def main():
	arr = [2, 10, 8, 0, 4]

	heap_Sort(arr)

	print(arr)



if __name__ == '__main__':
	main()

