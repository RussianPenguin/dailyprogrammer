def print_matrix(matrix, label = None):
	if label:
		print label
	print "\n".join(" ".join(map(str, x)) for x in matrix)

def start_edge(matrix):
	size = len(matrix)
	for line in range(size):
		for edge in range(size):
			if adj_matr[line][edge]:
				return line
	return -1

def run_wave(adj_matrix, visited, vertex_list):
	path_list = []
	for vertex in vertex_list:
		for idx in range(len(adj_matrix[vertex])):
			if adj_matrix[vertex][idx] and visited[idx] == -1:
				path_list.append((vertex, idx))
	return path_list

if __name__ == '__main__':
	vertex_cnt = int(input())
	adj_matr = [map(int, raw_input().split()) for _ in range(vertex_cnt)]
	print_matrix(adj_matr, 'Adjacency matrix')

	# select random vertex for start
	vertex = start_edge(adj_matr)
	if vertex == -1:
		exit(-1)

	# run wave algorithm
	visited = [-1 for _ in range(vertex_cnt)]

	# first step of wave algorithm we should do manually
	visited[vertex] = 0
	next_weight = 1
	vertex_list = [vertex]

	while True:
		path_list = run_wave(adj_matr, visited, vertex_list)
		if not len(path_list):
			break
		#print path_list, 'Wave'
		# fill add new path to weights matrix with next_weight
		for path in path_list:
			visited[path[1]] = next_weight

		# prepare new vertex_list for next wave

		vertex_list = [path[1] for path in path_list]
		next_weight += 1
		#print visited, 'Weights on step %d' % (next_weight - 2)

	print max(visited)
