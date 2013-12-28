import collections

if __name__ == '__main__':
	linesCnt = int(input())
	# prepare raw matrix
	adjacencyMatrix = {}

	for _ in range(linesCnt):
		row = raw_input().split()
		adjacencyMatrix[row[0]] =  row[1:]

	#print adjacencyMatrix

	# bfs
	queue = collections.deque([])
	visited = []

	colors = {}

	# select initial vertex
	for vertex in adjacencyMatrix:
		queue.append(vertex)
		break

	while True:
		try:
			vertex = queue.popleft()

			if vertex in visited:
				continue		
	
			adjacencyColors = set()

			if vertex in adjacencyMatrix:
				# collect solors for all adjacency verterx
				for target in adjacencyMatrix[vertex]:
					if target in colors:
						adjacencyColors.add(colors[target])

				# and select unused color for current vertex
				# we can use "five colors theorem" (like xrange(5)). but overhead is need
				for colorIndex in xrange(0, 100):
					if not colorIndex in adjacencyColors:
						colors[vertex] = colorIndex
						break

				for target in adjacencyMatrix[vertex]:
					
					queue.append(target)

			visited.append(vertex)
		except IndexError:
			break

	#print visited
	#print colors
	for vertex in colors:
		print "%s: %d" % (vertex, colors[vertex])
		
