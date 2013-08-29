
"""
    Developer modules
"""
from HilbertSpace import *
from Operators import *

from solver import *
from constants import *

class main_app:
    
    P9 = Projection(9,8)
    
    def __init__(self,A,b,omega):
        self.A = A
        self.b = b
        self.omega = omega
        
    def test_solvable(self):
        try: 
            solve(self.A,self.b)
        except ValueError:
            print "Your system has no solution"
            sys.exit(1)
            
    
