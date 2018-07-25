# Insertion Sort

def InsertionSort(lista):

	for i in range(1, len(lista)):
		atual = lista[i]

		for j in range(i - 1, -1, -1): #For que decresce partindo última posição ordenada até o início da lista
			if lista[j] > atual:
				lista[j], lista[j + 1] = lista[j + 1], lista[j]
			else:
				break
	return lista

def SelectionSort(lista):
	for i in range(0, len(lista)):
		min = lista[i]

		for j in range(i + 1, len(lista)):
			if lista[j] < min: 
				min = lista[j]
	lista[i], lista[j] = lista[j], lista[i]
	return lista



def main():
	
	teste = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
	teste2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]


	print('Lista original: %s' % str(teste))

	print('Lista ordenada pelo Insertion Sort: %s '% str(InsertionSort(teste)))

	print('Lista ordenada pelo Selection Sort: %s '% str(SelectionSort(teste)))

if __name__ == '__main__':
	main()

