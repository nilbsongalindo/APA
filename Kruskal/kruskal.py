from graph import Graph
"""
OBS: O arquivo de teste 'dij10.txt' continha algum separador que não permitia que eu iterasse sobre ele.
Copiei tudo que havia no arquivo, colei e outro de mesmo nome e funcionou.
"""
def main():
	g = Graph()
	count = 0
	input = open('dij10.txt', 'r')
	x = input.read()

	for row,line in enumerate(x.split('\n')):
		for col,val in enumerate(line.split(' ')):
			print (row, col, val)
			count += 1
			g.edge(int(row), int(col), int(val))

	print(count)
	g.setVerticies(count)
	g.kruskal()

if __name__ == '__main__':
	main()
