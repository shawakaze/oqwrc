
"""
    Developer modules
"""
from HilbertSpace import *
from Operators import *

from solver import *
from constants import *

class main:
    
    P9 = Projection(9,8)
    
    def __init__(self,A,b):
        self.A = A
        self.b = b
        
    def test_solvable(self):
        try: 
            solve(self.A,self.b)
        except ValueError:
            print "Your system has no solution"
            sys.exit(1)
            
    
