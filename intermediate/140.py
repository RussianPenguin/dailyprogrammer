if __name__ == '__main__':
	description = map(int, raw_input().split())

	# fill 
	matrix = [[0 for _ in range(description[0])] for _ in range(description[0])]

	for _ in range(description[1]):
		nodes = [[int(node.strip()) for node in node_set.split()] for node_set  in raw_input().split('->')]
		print nodes
		for from_node in nodes[0]:
			for to_node in nodes[1]:
				matrix[from_node][to_node] = 1

	for line in matrix:
		print "".join(map(str, line))
	
