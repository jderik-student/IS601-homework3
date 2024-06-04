from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

'''
    This class defines a basic calculator that can only add, subtract, multiply, and divide 
'''

class Calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculation(a,b, add)
        return calculation.calculate()
    
    def subtract(a,b):
        calculation = Calculation(a,b, subtract)
        return calculation.calculate()
    
    def multiply(a,b):
        calculation = Calculation(a,b, multiply)
        return calculation.calculate()
    
    def divide(a,b):
        calculation = Calculation(a,b, divide)
        return calculation.calculate()
