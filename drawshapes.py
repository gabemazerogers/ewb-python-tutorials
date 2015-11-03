def drawSquare(width, outer, inner):
	for x in range(0,width):
		temp = ""
		for y in range(0,width):
			if (y == 0) or (y == width-1) or (x == 0) or (x == width-1):
				temp += outer
			else:
				temp += inner
		print temp

def drawX(width, outer, inner):
	for x in range(0,width):
		temp = ""
		for y in range(0, width):
			if(x == y) or (x == width-y-1) or (y == width-x-1):
				temp += inner
			else:
				temp +=	outer
		print temp
