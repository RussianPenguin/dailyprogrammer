# -*- encoding: utf8 -*-

def get_winner(votes, loosers):
	order = {}
	for vote in votes:
		for pos in vote:
			if not pos in loosers:
				if pos in order:
					order[pos] += 1.0
				else:
					order[pos] = 1.0
				break
	#print order
	for pos in order:
		order[pos] /= len(votes)
	return order

def print_order(candidates, order):
	out_buffer = []
	for pos in sorted(order, key=order.get, reverse=True):
		out_buffer.append(str(str(order[pos] * 100) + "% " + candidates[pos]))
	return out_buffer

def has_winner(order):
	for pos in order:
		if order[pos] > 0.5:
			return pos
	else:
		return None

def get_looser(order):
	return sorted(order, key=order.get)[0]

if __name__ == '__main__':
	settings = map(int, raw_input().split())

	candidates = raw_input().split()

	votes = [map(int, raw_input().split()) for _ in range(settings[0])]
	loosers = set()

	while len(candidates) != len(loosers):
		order = get_winner(votes, loosers)
		#print order
		print 'Round ' + str(len(loosers) + 1) + ': ' + ', '.join(print_order(candidates, order))

		winner = has_winner(order)

		if winner != None:
			print candidates[winner] + " is the winner"
			break
		loosers.add(get_looser(order))
		#print loosers
	else:
		print "Bad choice"

	#print settings, candidates, votes

	
