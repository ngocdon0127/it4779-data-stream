from math import *

no_of_hash_funcs = 5
epsilon = exp(1) * (10 ** -4)
range_hash = int(ceil(exp(1) / epsilon))
# print (range_hash)
max_word = -1

teta = exp(-no_of_hash_funcs)

dic = {}
params_a = []
params_b = []

# Read hash functions' parameters
f = open('HW4-q4/hash_params.txt')
stt = 0
for line in f:
	if (no_of_hash_funcs <= stt):
		break
	line = line.strip()
	params_a.append(int(line.split('\t')[0]))
	params_b.append(int(line.split('\t')[1]))
	stt += 1

f.close()

# print params_a
# print params_b

def hf(i, x):
	return hash_fun(params_a[i], params_b[i], 123457, range_hash, x)

def hash_fun(a, b, p, n_buckets, x):
	y = x % p
	hash_val = (a * y + b) % p
	return hash_val % n_buckets


for i in range(no_of_hash_funcs):
	dic[i] = {}
	for j in range(range_hash):
		dic[i][j] = 0

f = open('HW4-q4/words_stream.txt')

for line in f:
	word = int(line.strip())
	max_word = word if (max_word < word) else max_word
	for j in range(no_of_hash_funcs):
		# h = hash_fun(params_a[j], params_b[j], 123457, range_hash, word)
		h = hf(j, word)
		# print 'increasing %d %d' % (j, h)
		dic[j][h] = dic[j][h] + 1



f.close()

# print dic[1]
# print dic[2]

def frequent(word):
	fre = dic[0][hf(0, word)]
	for i in range(1, no_of_hash_funcs):
		# print 'hf %d' % hf(i, word)
		fre_ = dic[i][hf(i, word)]
		# print "%d %d" % (fre, fre_)
		fre = fre_ if (fre_ < fre) else fre
	return fre

# print frequent(1)
# print frequent(2)

for i in range(1, max_word + 1):
	print "%d\t%d" % (i, frequent(i))
