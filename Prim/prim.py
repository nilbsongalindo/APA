import sys

class Graph():

	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = []

	def setVerticies(self, vertices):
		self.vertices = vertices

	def Key_minimo(self, key, conjunto):
		minimo = float("inf")

		for vertice in range(self.vertices):
			if key[vertice] < minimo and conjunto[vertice] == False:
				index_minimo = vertice
				minimo = key[vertice]
		return index_minimo

	def imprime(self, parent):
		x = 0
		for i in range(1, self.vertices):
			print(parent[i], '->', i, ' ', self.graph[i][parent[i]])
			x += self.graph[i][parent[i]]
		print('Custo total: %.2f' % x)

	def prim(self):
		key = [float("inf")] * self.vertices
		parent = [None] * self.vertices
		parent[0] = -1
		key[0] = 0
		conjunto = [False] * self.vertices

		for v in range(self.vertices):
			u = self.Key_minimo(key, conjunto)

			conjunto[u] = True

			for w in range(self.vertices):
				if self.graph[u][w] > 0 and conjunto[w] == False and key[w] > self.graph[u][w]:
					key[w] = self.graph[u][w]
					parent[w] = u

		self.imprime(parent)





