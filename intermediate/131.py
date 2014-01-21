import math

def is_wall(game_map, x, y):
	if y < 0 or y >= len(game_map) or x < 0 or x >= len(game_map[y]):
		return False
	return game_map[y][x] == 'x'
	
# detect hit by direction
def hit(game_map, x, y, signX, signY):
	cell_x = int(x)
	cell_y = int(y)

	if is_wall(game_map, cell_x, cell_y):
		return True

	if x % cell_x == 0:
		if signX > 0:
			if is_wall(game_map, cell_x, cell_y):
				return True
		else:
			if is_wall(game_map, cell_x - 1, cell_y):
				return True

	if y % cell_y == 0:
		if signY > 0:
			if is_wall(game_map, cell_x, cell_y):
				return True
		else:
			if is_wall(game_map, cell_x, cell_y - 1):
				return True

	return False

if __name__ == '__main__':
	width, height = map(int, raw_input().split())
	game_map = [raw_input().rjust(width, ' ') for _ in range(height)]
	walk_map = [[game_map[_][__] for __ in range(width)] for _ in range(height)]

	x, y, fi = map(float, raw_input().split())

	deltaX = math.cos(fi)*0.0001
	deltaY = -math.sin(fi)*0.0001
	
	signX = math.copysign(1, deltaX)
	signY = math.copysign(1, deltaY)

	# calc initial ray len
	map_x = x
	map_y = y

	while not hit(game_map, map_x, map_y, signX, signY):
		walk_map[int(map_y)][int(map_x)] = 'Z'

		map_x += deltaX
		map_y += deltaY

		#print map_x, map_y, x, y
	
	print "\n".join(map(lambda _: "".join(_), walk_map))

	print "%.03f %.03f" % (map_x, map_y)
