base7 	= ([1,2,3])
base13 	= ([1,3,4], [2,5,6]) 
base15	= ([1,3,4], [2,6,7])
base19	= ([1,5,6], [2,8,9], [3,4,7])
base27	= ([1,12,13], [2,5,7], [3,8,11], [4,6,10])
base45 	= ([1,11,12], [2,17,19], [3,20,22],[4,10,14],[5,8,13],[6,18,21], [7,9,16])
base63 	= ([1,15,16], [2,27,29], [3,25,28],[4,14,18],[5,26,32],[6,17,23],[7,13,20],[8,11,19],[9,24,30],[10,12,22])

bases = [(7,base7),(13,base13),(15,base15),(19,base19),(27,base27),(45,base45),(63,base63)]

def rotate_base_triple(base, n):
	rotations = []
	for x in range (0,n):
		b1 = base[0] + x; 
		b2 = base[1] + x;
		next = [b1, b2]
		y = b1 + b2
		y = y%n
		if y > n//2:
			y = 0 - y 
			y %= n
		next.append(y)
		rotations.append(next)
	return rotations

def find_all_triples_for_base(base, n):
	results = []
	for x in range(0,len(base)):
		#print(base[x])
		result = rotate_base_triple(base, n)
		results.append(result)
	return results

def find_all(lst):
	results = []
	for x in range (0, len(lst)):
		result = find_all_triples_for_base(bases[x][1],bases[x][0]);
		print("Base: " + str(bases[x][0]))
		#for i in range (0, len(result)):
			#print_triples(result[i])
		results.append(result)
	return results;

def print_triples(lst):
	for x in range(0, len(lst)):
		for y in range(0, len(lst[x])):
			if y < len(lst[x]) -1:
				print(str(lst[x][y]) + ",", end =' ')
			else:
				print(str(lst[x][y]), end =' ')
		print('')



def main():
#	print(bases[0][1][0])
#	print(bases[0][1][1])
#	print(bases[0][1][2])
#	test1 = find_all_triples_for_base(base19,19)
#	for i in range (0, len(test1)):
#		print_triples(test1[i])
	find_all(bases)
	#test1 = rotate_base_triple(base13[1],13)
	#print_triples(test1)

main()