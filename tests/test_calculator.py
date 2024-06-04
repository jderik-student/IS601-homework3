'''My Calculator Test'''
import pytest
from calculator import add, subtract, multiply, divide

# pylint: disable=unnecessary-dunder-call, invalid-name

def test_add():
    '''Test that addition function works '''    
    assert add(6,2) == 8

def test_subtract():
    '''Test that subtraction function works '''    
    assert subtract(6,2) == 4

def test_multiply():
    '''Test that multiplication function works '''    
    assert multiply(6,2) == 12

def test_division_nonZero_Divisor():
    '''Test that division function works with a non-zero Divisor'''    
    assert divide(6,2) == 3

def test_division_Zero_Divisor():
    '''Test that division function works '''    
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(6,0)
