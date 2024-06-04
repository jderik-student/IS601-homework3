'''
    This code defines the basic operations of a calculator that can only add, subtract, multiply, and divide 
'''
def add(a,b):
    """Performs addition"""
    return a + b

def subtract(a,b):
    """Performs subtraction"""
    return a - b

def multiply(a,b):
    """Performs multiplication"""
    return a * b

def divide(a,b):
    """Performs division, raises a ValueError if given a 0 as the Divisor"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
