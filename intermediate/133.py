from collections import deque
import itertools

def get_cells(lookahead, grid):
	cells = []
	for location in lookahead:
		val = grid[location[0]][location[1]]
		if val != 'X' and val != ' ':
			cells.append(val)
	return cells

def print_grid(grid, label = None):
	if label:
		print label
	print "\n".join("".join(row) for row in grid)

if __name__ == '__main__':
	elements, grid_size = map(int, raw_input().split())
	parts = [raw_input().split() for _ in range(elements)]

	exec_queue = deque([])
	
	grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
	grid_map = {}

	current_part_name = 'A'
	for item in parts:
		grid[int(item[1])][int(item[0])] = current_part_name
		grid_map[current_part_name] = item
		current_part_name = chr(ord(current_part_name)+1)

	#print_grid(grid)

	exec_queue.append('A')

	iteration = 0
	while len(exec_queue) > 0:
		print_grid(grid, "Step %d" % iteration)
		iteration += 1
		current_cell = exec_queue.popleft()
		#print current_cell
		if not current_cell in grid_map:
			continue
		activator = grid_map[current_cell]
		#print activator
		lookahead = []
		for direction in activator[3].lower():
			if direction == 'l':
				bound = int(activator[0]) - int(activator[2])

				if bound < 0:
					bound = 0

				x = [int(activator[1])]
				y = range(bound, int(activator[0]))
				coords = [(i, j) for i, j in itertools.izip(itertools.cycle(x), y)]
				#print x, y, coords
				lookahead += coords
			elif direction == 'r':
				bound = int(activator[0]) + int(activator[2])
				if bound > grid_size:
					bound = grid_size
				x = [int(activator[1])]
				y = range(int(activator[0]) + 1, bound)
				coords = [(i, j) for i, j in itertools.izip(itertools.cycle(x), y)]
				#print x, y, coords
				lookahead += coords
			elif direction == 'u':
				bound = int(activator[1]) - int(activator[2])
				if bound < 0:
					bound = 0
				x = range(bound, int(activator[1]))
				y = [int(activator[0])]
				coords = [(i, j) for i, j in itertools.izip(x, itertools.cycle(y))]
				#print coords
				lookahead += coords
			elif direction == 'd':
				bound = int(activator[1]) + int(activator[2])
				if bound > grid_size:
					bound = grid_size
				x = range(int(activator[1])+1, bound)
				y = [int(activator[0])]
				coords = [(i, j) for i, j in itertools.izip(x, itertools.cycle(y))]
				#print coords
				lookahead += coords
		grid[int(activator[1])][int(activator[0])] = 'X'
		exec_queue += get_cells(lookahead, grid)
		#print lookahead
		#print_grid(grid)
	else:
		print_grid(grid, "Step %d" % iteration)
		
	#print parts
