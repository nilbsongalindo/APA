def partition(arr, low, high):
	pivot = arr[high]

	i = (low - 1)

	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = arr[high], arr[i + 1]

	return i + 1

def quickSort(arr, low, high):
	if(low < high):
		index = partition(arr, low, high)

		quickSort(arr, low, index - 1)
		quickSort(arr, index + 1, high)


def main():
	arr = [10, 7, 8, 9, 1, 5]
	n = len(arr)
	quickSort(arr,0,n-1)
	print ("Lista Ordenada: ")
	for i in range(n):
	    print ("%d" %arr[i])


if __name__ == '__main__':
	main()