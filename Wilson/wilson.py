

def contains(small, big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False
results = []
def wilson(order):
	n = order - 2
	print ("n: " + str(n))
	for x in range (1,n):
		for y in range((x+1),n):
			for z in range ((y+1),n):
				if ((x+y+z)%n) == 0:
					result = [x,y,z]
					result.sort()
					if contains(result, results) == False:
						results.append(result)

def def_graph(order):
	n = order - 2
	list0 = []
	list_inf1 = []
	list_inf2 = []
	for x in range(1,n//2):
		list0.append([x,(-x)%n,0])
	print ("list zero: \n")
	for x in range(0,len(list0)):
		print(list0[x])

	for x in range(0,n):
	#list_inf1.append([x,(0-2*x)%n, "inf1"])
		y = (-2*x)%n
		result = [x,y]
		result.sort()
		if contains(result,list_inf1) == False:
			list_inf1.append(results.append("i1"))
		print(list_inf1[x])
	print ("list infinity1:\n")

#wilson(19)
#number_of_triples = 0;
#for x in range(0,len(results)):
#	for y in range(0,len(results[x])):
#		print (results[x][y], end=' ')
#	print ("")
#	number_of_triples += 1
#print ("number of triples: " + str(number_of_triples))

#def_graph(37)


for x in range(1, 35):
	print(str(x) + ", " + str((-x%35)))
	#print(str(x) + ", " + str(((-2*x)%36)))