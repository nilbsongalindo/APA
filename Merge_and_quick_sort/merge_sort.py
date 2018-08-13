def merge(arr):
	if len(arr) > 1:
		m = len(arr) // 2 #Calcula o meio

		L = arr[:m]
		R = arr[m:]

		merge(L)
		merge(R)
		
		i = 0
		j = 0
		k = 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			k += 1
			i += 1

		while j < len(R):
			arr[k] = R[j]
			k += 1
			j += 1

def main():
	arr = [54,26,93,17,77,31,44,55,20]
	print('Lista: %s\n' % str(arr))
	merge(arr)
	print('Lista Ordenada: %s' % str(arr))

if __name__ == '__main__':
	main()