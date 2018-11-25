"""
The main code file.
"""

"""
Uncatagorised
"""
#paragraph space
def Echospace(paragraphspaces=1):
	for i in range(paragraphspaces):
		print("", end="/n")
		
def Echo(text, amount=1):
	for i in range(amount):
		print(text)

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
		raise RuntimeError('An Error Has Occured: Invalid Debug State Entered (0005)')

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

"""
Maths
"""

#sin of a number
def Echosin(number):
	import math
	return math.sin(number)
  
  #tan of a number
def Echotan(number):
	import math
	return math.tan(number)
  
#hypot of a number
def Echohypot(number):
	import math
	return math.hypot(number)
  
#atan of a number
def Echoatan(number):
	import math
	return math.atan(number)

#asin of a number
def Echoasin(number):
	import math
	return math.asin(number)

#get value of pi
def Echopi():
	import math
	return math.pi

#get value of e
def Echoe():
	import math
	return math.e
  
#divide 2 numbers
def Echodivide(firstnumber, secondnumber):
	return firstnumber / secondnumber

#multiply 2 numbers
def Echotimes(firstnumber, secondnumber):
	return firstnumber * secondnumber

#add 2 numbers
def Echoadd(firstnumber, secondnumber):
	return firstnumber + secondnumber

#minus 2 numbers
def Echominus(firstnumber, secondnumber):
	return firstnumber - secondnumber
