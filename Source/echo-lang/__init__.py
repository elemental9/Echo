#paragraph space
def Echospace(paragraphspaces=1):
	for i in range(paragraphspaces):
		print("", end="/n")

#print letters/numbers
def Echoprint(message):
	print(str(message))

#execute
def Echocute(command):
	exec(command)
 
#evaluate
def Echovaluate(operation):
	return eval(operation)

#absolute
def Echolute(operation):
	return abs(operation)

#setup debugenabled variable
def Echodebug_statesetup():
	global debugenabled
	debugenabled = False
	
#execute shinydebug_statesetup()
Echodebug_statesetup()

#change debug state
def Debugstate(state):
	if state == 'enable':
		debugenabled = True
		print('debug mode has been enabled')
	elif state =='disable':
		debugenabled = False
		print('debug mode has been disabled')
	else:
		raise RuntimeError('An Error Has Occured: Invalid Debug State Entered (0005)')statesetup()

#supresswarnings
def Echodebug_supresswarning():
	if debugenabled is True:
		import warnings
		warnings.filterwarnings("ignore")
	else:
		raise RuntimeError('An Errror Has Occured:Debug mode Not Enabled(0006)')#supresswarnings

#exit execution
def Echocution(exitcode=0):
	import sys
	sys.exit(exitcode)
	
#store a value
def Echostore(value):
	Echo_stored = value
	
#get the stored value
def Echoget(value):
	return Echo_stored
