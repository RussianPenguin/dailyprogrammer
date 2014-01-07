import random

def combine_equation(nums, actions):
	return " ".join(\
		map(lambda i: \
			"%d %s" % (nums[i], actions[i]) \
				if i < 3 \
				else "%d" % nums[i], \
		range(4)))

def calc_equation(nums, actions):
	return eval(combine_equation(nums, actions))

def gen_action(a, b):
	actions = '+-/*'
	while True:
		action_idx = random.randint(0, 3)
		if actions[action_idx] == '/':
			if b == 0 or a % b != 0:
				continue
		return actions[action_idx]

def gen_equation(num_from, num_to):
	nums = [random.randint(num_from, num_to+1) for _ in range(4)]
	actions = [gen_action(nums[i], nums[i+1]) for i in range(3)]
	return combine_equation(nums, actions), calc_equation(nums, actions)

if __name__ == '__main__':
	random.seed()

	num_from, num_to = map(int, raw_input().split())
	equation, answer = gen_equation(num_from, num_to)
	while True:
		print "> %s" % equation
		user_answer = raw_input('> ')
		try:
			if int(user_answer) == answer:
				print "> Correct!"
				equation, answer = gen_equation(num_from, num_to)
			else:
				print "> Incorrect..."
		except ValueError:
			if user_answer.lower() == 'q':
				break

