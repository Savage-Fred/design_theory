w,h = 8,8
addition = [[0 for x in range(w)] for y in range(h)]
multiplication = [[0 for x in range(w)] for y in range(h)]

addition[0][0] = 0
addition[0][1] = 1
addition[0][2] = 2
addition[0][3] = 3
addition[0][4] = 4
addition[0][5] = 5
addition[0][6] = 6
addition[0][7] = 7

addition[1][0] = 1
addition[1][1] = 0
addition[1][2] = 6
addition[1][3] = 4
addition[1][4] = 3
addition[1][5] = 7
addition[1][6] = 2
addition[1][7] = 5

addition[2][0] = 2
addition[2][1] = 6
addition[2][2] = 0
addition[2][3] = 7
addition[2][4] = 5
addition[2][5] = 4
addition[2][6] = 1
addition[2][7] = 3

addition[3][0] = 3
addition[3][1] = 4
addition[3][2] = 7
addition[3][3] = 0
addition[3][4] = 1
addition[3][5] = 6
addition[3][6] = 5
addition[3][7] = 2

addition[4][0] = 4
addition[4][1] = 3
addition[4][2] = 5
addition[4][3] = 1
addition[4][4] = 0
addition[4][5] = 2
addition[4][6] = 7
addition[4][7] = 6

addition[5][0] = 5
addition[5][1] = 7
addition[5][2] = 4
addition[5][3] = 6
addition[5][4] = 2
addition[5][5] = 0
addition[5][6] = 3
addition[5][7] = 1

addition[6][0] = 6
addition[6][1] = 2
addition[6][2] = 1
addition[6][3] = 5
addition[6][4] = 7
addition[6][5] = 3
addition[6][6] = 0
addition[6][7] = 4

addition[7][0] = 7
addition[7][1] = 5
addition[7][2] = 3
addition[7][3] = 2
addition[7][4] = 6
addition[7][5] = 1
addition[7][6] = 4
addition[7][7] = 0


multiplication[0][0] = 0
multiplication[0][1] = 0
multiplication[0][2] = 0
multiplication[0][3] = 0
multiplication[0][4] = 0
multiplication[0][5] = 0
multiplication[0][6] = 0
multiplication[0][7] = 0

multiplication[1][0] = 0
multiplication[1][1] = 1
multiplication[1][2] = 2
multiplication[1][3] = 3
multiplication[1][4] = 4
multiplication[1][5] = 5
multiplication[1][6] = 6
multiplication[1][7] = 7

multiplication[2][0] = 0
multiplication[2][1] = 2
multiplication[2][2] = 3
multiplication[2][3] = 4
multiplication[2][4] = 5
multiplication[2][5] = 6
multiplication[2][6] = 7
multiplication[2][7] = 1

multiplication[3][0] = 0
multiplication[3][1] = 3
multiplication[3][2] = 4
multiplication[3][3] = 5
multiplication[3][4] = 6
multiplication[3][5] = 7
multiplication[3][6] = 1
multiplication[3][7] = 2

multiplication[4][0] = 0
multiplication[4][1] = 4
multiplication[4][2] = 5
multiplication[4][3] = 6
multiplication[4][4] = 7
multiplication[4][5] = 1
multiplication[4][6] = 2
multiplication[4][7] = 3

multiplication[5][0] = 0
multiplication[5][1] = 5
multiplication[5][2] = 6
multiplication[5][3] = 7
multiplication[5][4] = 1
multiplication[5][5] = 2
multiplication[5][6] = 3
multiplication[5][7] = 4

multiplication[6][0] = 0
multiplication[6][1] = 6
multiplication[6][2] = 7
multiplication[6][3] = 1
multiplication[6][4] = 2
multiplication[6][5] = 3
multiplication[6][6] = 4
multiplication[6][7] = 5

multiplication[7][0] = 0
multiplication[7][1] = 7
multiplication[7][2] = 1
multiplication[7][3] = 2
multiplication[7][4] = 3
multiplication[7][5] = 4
multiplication[7][6] = 5
multiplication[7][7] = 6



numMols = 7
order = 8
result = 0
xterm = 0
for x in range(1,8):
	print("\nMOLS(" + str(x)+")")
	print("\t", end="")
	for i in range(order):
		print(str(i), end=" ")
	print("")
	for i in range(order*3):
		print("-", end="")
	print("\n0|\t", end="")
	for i in range(order):
		for j in range(order):
			xterm = multiplication[i][x]
			result = addition[xterm][j]
			print (result, end = " ")
		if i < (order -1):
			print ("\n"+str(i+1)+"|\t", end="")
	print("\n\ni*" + str(x) + "+j -> " + str(xterm))
	print("")













