import sys

base7 	= [[1,2,3]]
base13 	= [[1,3,4], [2,5,6]]
base15	= [[1,3,4], [2,6,7]]
base19	= [[1,5,6], [2,8,9], [3,4,7]]
base27	= [[1,12,13], [2,5,7], [3,8,11], [4,6,10]]
base45 	= [[1,11,12], [2,17,19], [3,20,22],[4,10,14],[5,8,13],[6,18,21], [7,9,16]]
base63 	= [[1,15,16], [2,27,29], [3,25,28],[4,14,18],[5,26,32],[6,17,23],[7,13,20],[8,11,19],[9,24,30],[10,12,22]]

bases = [[7,base7],[13,base13],[15,base15],[19,base19],[27,base27],[45,base45],[63,base63]]


#Function to check if a container contains something 
def contains(small, big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False

# Rotate a base about a graph
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
		if contains(next,rotations) == False:
			rotations.append(next)
	return rotations

# Function to print triples for a base
def print_triples(lst):
	for x in lst:
		for y in lst[x]:
			if y < len(lst[x]) -1:
				print(str(lst[x][y]) + ",", end =' ')
			else:
				print(str(lst[x][y]), end =' ')
		print('')


# Print all of the defined bases and all of their triples
# Warning: This prints a lot of stuff 
def print_all():
	results = []
	for i in range(0,len(bases)):
	#for i in range(0,len(bases)%2):
		print("Order: " + str(bases[i][0]))
		print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
		for j in range(0,len(bases[i][1])):
			result = []
			result.append(rotate_base_triple(bases[i][1][j],int(bases[i][0])))
			for x in range(0,len(result)):
				for y in range(0,len(result[x])):
					print(str(result[x][y]))
		print()
