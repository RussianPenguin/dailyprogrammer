if __name__ == '__main__':
	data = [raw_input().lstrip("\n") for _ in range(input())]
	data = map(lambda s: list(s.ljust(max(map(len, data)), ' ')), data)
	print "\n".join(["".join(s) for s in zip(*data)])
