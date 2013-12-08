# -*- encoding: utf8 -*-

import re

# translate food name to vertex number in vertex_map
def food_to_vertex(food, vertex_map):
	vertices = []
	pattern = '^' + food.replace('*', '.*') + '$'

	for vertex in vertex_map:
		if re.search(pattern, vertex):
			vertices.append(vertex_map[vertex])
	return vertices

# find vertex which have same output
def simular_vertex_by_out(graph):
	simular = {}
	simular_exclude = []
	for i in range(len(graph)):
		if i in simular_exclude:
			continue

		simular_for_i = []
		for j in range(len(graph)):
			if i == j and not j in simular_exclude:
				continue
			# sompare
			for idx in range(len(graph[i])):
				if graph[i][idx] != graph[j][idx]:
					break
			else:
				simular_for_i.append(j)

		if len(simular_for_i):
			for item in simular_for_i:
				simular_exclude.append(item)
			simular[i] = simular_for_i
	return simular

# swap edge direction
def inverse_graph(graph):
	return [[graph[j][i] for j in range(len(graph[i]))] for i in range(len(graph))]

# find simular vertex in a and b
def vertex_diff(a, b):
	diff = {}
	for base in list(set(a.keys()) & set(b.keys())):
		if len(set(a[base]) & set(b[base])) == len(a[base]) and len(a[base]) == len(b[base]):
			diff[base] = a[base]
	return diff

def dfs(start, graph, unused):
	used = []
	path = []
	def dfs_func(vertex):
		used.append(vertex)
		path.append(vertex)
		for idx in range(len(graph[vertex])):
			if not idx in unused and graph[vertex][idx] == 1 and not idx in used:
				dfs_func(idx)

	dfs_func(start)
	return path

def print_food_order(order, food, simular):
	i = 1
	used = []
	for food_idx in order:
		items = [food[food_idx]]
		used.append(food_idx)
		if food_idx in simular:
			for simular_idx in simular[food_idx]:
				items.append(food[simular_idx])
				used.append(simular_idx)
		print i, ', '.join(items)
		i += 1
	for idx in list(set(range(len(food))) - set(used)):
		print "Warning: " + food[idx] + " does not have any ordering"
			
def print_graph(graph):
	for idx in range(len(graph)):
		print ' '.join(map(str, graph[idx]))

if __name__ == '__main__':
	# get input
	defines = map(lambda x: int(x), raw_input().split())
	food = [raw_input() for _ in range(defines[0])]
	rules = [raw_input().split() for _ in range(defines[1])]

	# prepare food map for better using in code
	food_map = dict(zip(food, range(len(food))))

	# make food graph
	food_graph = [[0 for _ in range(defines[0])] for _ in range(defines[0])]

	# filling edges for rules
	for rule in rules:
		vertex = map(lambda x: food_to_vertex(x, food_map), rule)
		for source in vertex[0]:
			for drain in vertex[1]:
				food_graph[source][drain] = 1

	# find simular vertex (optimize graph)
	simular_by_out = simular_vertex_by_out(food_graph)
	# find sumular vertex by input with reverse graph 
	simular_by_inp = simular_vertex_by_out(inverse_graph(food_graph))
	# find simular vertex by output and input
	simular = vertex_diff(simular_by_inp, simular_by_out)
			
	# create list of unused vertex (based on simular list)
	unused = []
	for idx in simular:
		unused += simular[idx]
	#print unused

	# find vertex without input
	reversed_graph = inverse_graph(food_graph)
	vertex_without_input = []
	for i in range(len(reversed_graph)):
		if i in unused:
			continue
		if set(reversed_graph[i]) == set([0]):
			vertex_without_input.append(i)

	#print vertex_without_input

	# depth search in graph for all start vertex
	# calculate, which of founded trees are maximal tree
	food_order = []

	print "befor remove transitive edges"
	print_graph(food_graph)
	# remove transitive edges
	for j in range(len(food_graph)):
		if not j in unused:
			for i in range(len(food_graph)):
				if not i in unused:
					if food_graph[i][j] == 1:
						for k in range(len(food_graph)):
							if not k in unused and food_graph[j][k] == 1:
								food_graph[i][k] = 0;
	print "after remove transitive edges"
	print_graph(food_graph)
	for i in vertex_without_input:
		food_order.append(dfs(i,  food_graph, unused))
	food_order.sort(lambda x, y: cmp(len(x), len(y)))

	print_food_order(food_order[-1], food, simular)
	
	#print defines, "\n", food, "\n", rules, "\n", food_map, "\n", food_graph

