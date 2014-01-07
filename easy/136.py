if __name__ == '__main__':
	students, grades = map(int, raw_input().split())
	output = ""
	class_average = 0
	for idx in range(students):
		raw = raw_input().split()
		student_average = sum(map(int, raw[1:grades+1]), 0.0)/grades
		output += "%s %.2f\n" % (raw[0], student_average) 
		class_average += student_average
	print "%.2f" % (class_average/float(students))
	print output
