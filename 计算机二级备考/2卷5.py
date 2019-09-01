def getInput():
	try:
	    x=input()
	    while eval(x)!=int(x):
		    x=input()
	except:
		return getInput()

	return eval(x)

print(getInput())
