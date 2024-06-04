'''My Calculator Test'''
import pytest
from calculator import Calculator

# pylint: disable=unnecessary-dunder-call, invalid-name

def test_add():
    '''Test that addition function works '''    
    assert Calculator.add(6,2) == 8

def test_subtract():
    '''Test that subtraction function works '''    
    assert Calculator.subtract(6,2) == 4

def test_multiply():
    '''Test that multiplication function works '''    
    assert Calculator.multiply(6,2) == 12

def test_division_nonZero_Divisor():
    '''Test that division function works with a non-zero Divisor'''    
    assert Calculator.divide(6,2) == 3

def test_division_Zero_Divisor():
    '''Test that division function works '''    
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(6,0)
