"""
The main code file.
"""
import math
import sys
import warnings
from quilt_lang import isnum
"""
Setup
"""


def _Echovar_setup():
    """
    Initialise value
    """
    global Echo_stored
    Echo_stored = None


# Execute _Echovar_setup()
_Echovar_setup()


def _Echodebug_statesetup():
    """
    Setup debugenabled variable
    """
    global debugenabled
    debugenabled = False


# Execute _Echodebug_statesetup()
_Echodebug_statesetup()
"""
Uncatagorised
"""


def space(paragraphspaces=1):
    """
    Paragraph space
    """
    for _ in range(paragraphspaces):
        print("", end="/n")


def Echo(text, amount=1):
    """
    Print text with amount option
    
    >>> Echo("Hello World!")
    Hello World!
    """
    for _ in range(amount):
        print(str(text))


def Echocute(command):
    """
    Execute a command
    """
    exec(command)


def Echovaluate(operation):
    """
    Evaluate an expression
    """
    return eval(operation)


def Echolute(operation):
    """
    Find the absolute value of a number
    """
    return abs(operation)


def Debugstate(state):
    """
    Change debug state
    """
    if state == 'enable':
        debugenabled = True
        print('Debug mode has been enabled')
    elif state == 'disable':
        debugenabled = False
        print('Debug mode has been disabled')
    else:
        raise RuntimeWarning('Invalid debug state specified.')


def compare(value1, value2, comparison):
    """
    Compare 2 values
    """
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


def debug_supresswarning():
    """
    Supress warnings
    """
    if debugenabled is True:
        warnings.filterwarnings("ignore")
    else:
        raise RuntimeWarning('Debug mode is not enabled.')


def Echocution(exitcode=0):
    """
    Exit execution
    """
    sys.exit(exitcode)


def Echostore(value):
    """
    Store a value
    """
    Echo_stored = value


def Echoget(value):
    """
    Get the stored value
    """
    return Echo_stored


"""
Maths
"""


def Echosin(number):
    """
    Sin of a number
    """
    return math.sin(number)


def Echotan(number):
    """
    Tan of a number
    """
    return math.tan(number)


def Echohypot(number):
    """
    Hypot of a number
    """
    return math.hypot(number)


# Atan of a number
def Echoatan(number):
    return math.atan(number)


def Echoasin(number):
    """
    Asin of a number
    """
    return math.asin(number)


def Echopi():
    """
    Get value of pi
    
    >>> import math
    >>> math.pi == Echopi()
    """
    return math.pi


def Echoe():
    """
    Get value of e
    """
    return math.e


def Echodivide(firstnumber, secondnumber):
    """
    Divide 2 numbers
    """
    return firstnumber / secondnumber


def Echotimes(firstnumber, secondnumber):
    """
    Multiply 2 numbers
    """
    return firstnumber * secondnumber


def Echoadd(firstnumber, secondnumber):
    """
    Add 2 numbers
    """
    return firstnumber + secondnumber


def Echominus(firstnumber, secondnumber):
    """
    Minus 2 numbers
    """
    return firstnumber - secondnumber


# Unit testing
if __name__ == "__main__":
    import doctest
    doctest.testmod()
