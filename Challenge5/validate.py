#Validate Pin

def valid(pin):
    """ 
    Function to test if a string is a valid pin or not. 
    A valid pin has: 1. Exactly 4 or 6 characters. 2. Only numerical characters (0-9). 3. No whitespace.
    Args:
        input ([int]): the pin that needs to be tested.
    """
    pin = str(pin)
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit() == True:
            return True
        else:
            return False
    else:
        return False
      
print(valid(1234))

# Shorter Version
def valid1(pin):
    pin = str(pin)
    return len(pin) in (4, 6) and pin.isdigit()

print(valid1("h23479"))