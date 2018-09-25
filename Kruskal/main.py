from graph import Graph
import numpy as np

def main():
	g = Graph()
	count = 0
	input = open('dij10.txt', 'r')
	x = input.read()
	tamanhoMatriz = 0

 #leitura do arquivo da matriz de adjacencia
	for row,line in enumerate(x.split('\n')):
		for col,val in enumerate(line.split(' ')):
			if(count == 0):
				tamanhoMatriz = int(val)
				count += 1
				break
			break

	count = 0
	matriz = np.zeros((tamanhoMatriz, tamanhoMatriz))
	matrizFinal = np.zeros((tamanhoMatriz, tamanhoMatriz))

	for row,line in enumerate(x.split('\n')):
		for col,val in enumerate(line.split(' ')):
			if(count == 0):
				tamanhoMatriz = int(val)
				count += 1
				break
			else:
				count+=2
				matriz[int(row-1)][int(col)] = int(val)

	for i in range(0, tamanhoMatriz):
		for j in range(i, tamanhoMatriz):
			if i == j:
				continue
			else:
				g.edge(i, j, matriz[i][j-i-1])
				g.edge(j, i, matriz[i][j-i-1])
				matrizFinal[i][j] = matriz[i][j-i-1]
				matrizFinal[j][i] = matriz[i][j-i-1]

	print('Matriz de adjacencias: \n')
	print(matrizFinal)

	count -=1
	g.setVerticies(count)
	#método para calcular MST
	g.kruskal()

if __name__ == '__main__':
	main()
