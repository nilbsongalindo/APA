from itens import Itens
import numpy as np

def knapsack(W, itens, n):
	memo = np.zeros((W+1, n+1))

	for w in range(0, W+1):
		for i in range(0, len(itens)+1):
			if w == 0 or i == 0:
				memo[w][i] = 0
			elif w < itens[i-1].peso:
				memo[w][i] = memo[w][i-1]
			else:
				memo[w][i] = max(memo[w - itens[i-1].peso][i-1] + itens[i-1].valor, memo[w][i-1])

	return memo[w][i]


def main():
	itens = []
	n = 0
	W = 0
	count = 0

	for line in open('mochila01.txt'):
		line = line.rstrip('\n')
		if count == 0:
			x = (line.split(' '))
			n = int(x[0])
			W = int(x[1])

			count = 1
			continue

		aux = (line.split(' '))

		itens.append(Itens(int(aux[0]), int(aux[1])))

	print('Lista de itens (peso/valor):')

	for i in range(0, len(itens)):
		print(itens[i].peso, itens[i].valor)

	print("\nSolucao: ")
	print(knapsack(W, itens, n))


if __name__ == '__main__':
	main()