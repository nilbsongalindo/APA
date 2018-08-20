def countSort(arr, k): #Where k is the range of values
	counting = [0 for i in range(k)]

	for i in arr: counting[i] += 1 #Increasing the element correspondent in the counter array by 1

	for i in range(1, len(counting)): #Sum of the element and his predecessor
		counting[i] += counting[i - 1]
	
	final_array = [0 for i in range(len(arr))] #Ordered array

	for i in range(len(arr)):   #
		final_array[counting[arr[i]] - 1] = arr[i]
		counting[arr[i]] = counting[arr[i]] - 1

	

	return final_array


def main():
	import numpy as np 
	arr = [1, 4, 1, 2,7, 5, 2]

	print('Lista: %s\n' % str(arr))

	print('Lista Ordenada: %s' % str(countSort(arr, 10)))






if __name__ == '__main__':
	main()
