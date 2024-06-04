'''
    This class defines a calculation and stores its term and the operation to be calculated 
'''

class Calculation:
    def __init__(self, a, b, operation):
        # Stores the two terms of the operation and the operation function
        self.a = a
        self.b = b
        self.operation = operation
    
    def calculate(self):
        # Calls the stored operation on its two terms
        return self.operation(self.a, self.b)
