"""
The main code file.
"""
import math
import sys
import warnings
from quilt_lang import isnum
"""
Uncatagorised
"""


# Paragraph space
def space(paragraphspaces=1):
    for _ in range(paragraphspaces):
        print("", end="/n")


# Print text with amount option
def Echo(text, amount=1):
    for _ in range(amount):
        print(str(text))


# Execute a command
def Echocute(command):
    exec(command)


# Evaluate an expression
def Echovaluate(operation):
    return eval(operation)


# Find the absolute value of a number
def Echolute(operation):
    return abs(operation)


# Setup debugenabled variable
def _Echodebug_statesetup():
    global debugenabled
    debugenabled = False


# Execute Echodebug_statesetup()
_Echodebug_statesetup()


# Change debug state
def Debugstate(state):
    if state == 'enable':
        debugenabled = True
        print('Debug mode has been enabled')
    elif state == 'disable':
        debugenabled = False
        print('Debug mode has been disabled')
    else:
        raise RuntimeWarning('Invalid debug state specified.')


def compare(value1, value2, comparison):
    if isnum(value1) and isnum(value2):
        comparison = comparison.lower()
        if comparison == 'equals':
            return value1 == value2
        elif comparison == 'not equal':
            return value1 != value2
        elif comparison == 'less than':
            return value1 < value2
        elif comparison == 'greater than':
            return value1 > value2
        elif comparison == 'more than':
            return value1 > value2
        elif comparison == 'less than or equal to':
            return value1 <= value2
        elif comparison == 'greater than or equal to':
            return value1 >= value2
        elif comparison == 'more than or equal to':
            return value1 >= value2


# Supresswarnings
def debug_supresswarning():
    if debugenabled is True:
        warnings.filterwarnings("ignore")
    else:
        raise RuntimeWarning('Debug mode is not enabled.')


# Exit execution
def Echocution(exitcode=0):
    sys.exit(exitcode)


# Initialise value
def _Echovar_setup():
    Echo_stored = None
    global Echo_stored


# Execute Echovar_setup()
_Echovar_setup()


# Store a value
def Echostore(value):
    Echo_stored = value


# Get the stored value
def Echoget(value):
    return Echo_stored


"""
Maths
"""


# Sin of a number
def Echosin(number):
    return math.sin(number)


# Tan of a number
def Echotan(number):
    return math.tan(number)


# Hypot of a number
def Echohypot(number):
    return math.hypot(number)


# Atan of a number
def Echoatan(number):
    return math.atan(number)


# Asin of a number
def Echoasin(number):
    return math.asin(number)


# Get value of pi
def Echopi():
    return math.pi


# Get value of e
def Echoe():
    return math.e


# Divide 2 numbers
def Echodivide(firstnumber, secondnumber):
    return firstnumber / secondnumber


# Multiply 2 numbers
def Echotimes(firstnumber, secondnumber):
    return firstnumber * secondnumber


# Add 2 numbers
def Echoadd(firstnumber, secondnumber):
    return firstnumber + secondnumber


# Minus 2 numbers
def Echominus(firstnumber, secondnumber):
    return firstnumber - secondnumber
