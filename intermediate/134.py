def solutions_count(value, coins):
	#print value, coins, range(0, value)
	result = [[0 for _ in range(len(coins))] for _ in range(0, value+1)]
	for idx in range(len(coins)):
		result[0][idx] = 1

	for idx in range(1, value+1):
		for coin_idx in range(len(coins)):
			x = 0
			if idx - coins[coin_idx] >= 0:
				x = result[idx - coins[coin_idx]][coin_idx]
			y = 0
			if coin_idx >= 1:
				y = result[idx][coin_idx-1]

			result[idx][coin_idx] = x+y
	print result
	return result[value][len(coins)-1]

def solutions(value, coins):
	all_solutions = []	

	def next_solution(cur, start_idx, remains):
		#print range(start_idx, len(coins))
		for idx in range(start_idx, len(coins)):
			rest = remains - coins[idx]
			inner_sln = dict(cur)

			if rest < 0:
				break

			if not coins[idx] in inner_sln:
				inner_sln[coins[idx]] = 0
			inner_sln[coins[idx]] += 1

			if rest == 0:
				all_solutions.append(dict(inner_sln))
				break
			else:
				next_solution(dict(inner_sln), int(idx), int(rest))
	
	next_solution(dict({}), 0, value)
	return all_solutions

if __name__ == '__main__':
	mutations, value = map(int, raw_input().split())
	for idx in range(mutations):
		print "Currency %d combinations" % (idx+1)
		for combination in solutions(value, map(int, raw_input().split())):
			print " ".join(map(lambda x: "%d:%d" % (x, combination[x]), combination))
