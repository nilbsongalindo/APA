def root(i):
	return int (i - 1) / 2

def left_child(i):
	return 2 * i + 1

def right_child(i):
	return 2 * i + 2

def max_heapfy(arr, n, i): #heapfy
	biggest = i
	left = left_child(i) #left_node
	right = right_child(i) #right_node

	#Checking if right node is greater than root
	if right < n and arr[biggest] < arr[right]:
		biggest = right

	#Checking if left node is greater than root
	if left < n and arr[biggest] < arr[left]:
		biggest = left

	#Checking if 'i' is the largest. T
	if biggest != i:
		arr[i], arr[biggest] = arr[biggest], arr[i]

		max_heapfy(arr, n, biggest)


def build_max_heap(arr):
	n = len(arr)
	for i in range(n, -1, -1):
		max_heapfy(arr, n, i)



def heap_Sort(arr):
	n = len(arr)

	build_max_heap(arr)
	#swap the first and the last node, then remove the last one
	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] 
		max_heapfy(arr, i, 0)


def main():
	arr = [2, 10, 8, 0, 4]

	heap_Sort(arr)

	print(arr)



if __name__ == '__main__':
	main()











