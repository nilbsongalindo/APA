class Graph():

	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = [[0 for columns in range(vertices)]for rows in range(vertices)]

	def setVerticies(self, vertices):
		self.vertices = vertices

	def distancia_minima(self, distancia, conjunto):
		minimo = float("inf")
		index_minimo = 0

		for vertice in range(self.vertices):
			if distancia[vertice] < minimo and conjunto[vertice] == False:
				minimo = distancia[vertice]
				index_minimo = vertice	
		
		return index_minimo

	def imprime(self, distancia):
		for no in range(self.vertices):
			print(no, '--',distancia[no])

	def dijkstra(self, origem):
		distancia = [float('inf')] * self.vertices
		distancia[origem] = 0
		conjunto = [False] * self.vertices

		for v in range(self.vertices):
			u = self.distancia_minima(distancia, conjunto)

			conjunto[u] = True

			for w in range(self.vertices):
				if self.graph[u][w] > 0 and conjunto[w] == False and distancia[w] > distancia[u] + self.graph[u][w]:
					distancia[w] = distancia[u] + self.graph[u][w] 

		self.imprime(distancia)





