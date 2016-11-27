f = open('HW4-q4/counts.txt')
f_predict = open('result.txt')

for line in f:
	# print '==='
	# print line
	line = line.strip()
	line_predict = f_predict.readline().strip()
	word = int(line.split('\t')[0])
	frequent = int(line.split('\t')[1])
	frequent_predict = int(line_predict.split('\t')[1])
	err = (frequent_predict - frequent) / (float(frequent))
	# print "%d %f" % (word, err)
	if (err < 1):
		print word
	# print '==='

f.close()
f_predict.close()