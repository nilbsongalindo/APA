class Graph():

	def __init__(self):
		self.verticies = 0
		self.graph = []

	def setVerticies(self, verticies):
		self.verticies = verticies

	def edge(self, x, y, w):
		self.graph.append([x, y, w])

	def findSet(self, parent, i):
		if parent[i] == i:
			return i
		else:
			return self.findSet(parent, parent[i])


	def make_set(self, vertice, parent):
		parent.append(vertice)

	def union(self, x, y, parent):
		root1 = self.findSet(parent, x)
		root2 = self.findSet(parent, y)

		parent[root2] = root1


	def kruskal(self):
		result = []
		parent = []
		i = 0
		aux = 0


		for node in range(self.verticies):
			self.make_set(node, parent)

		self.graph = sorted(self.graph, key= lambda element:element[2])

		while aux < self.verticies - 1:
			u, v, w = self.graph[i]
			i += 1

			if self.findSet(parent, u) != self.findSet(parent, v):
				result.append([u, v, w])
				self.union(u, v, parent)
				
			aux += 1

		print('Kruskal MST: ')
		for (u, v, w) in result:
			print('%d - %d -> %d'% (u, v, w))







