
from src import *

class main_app:
    
    P9 = Projection(9,8)
    
    def __init__(self,A,b,omega):
        self.A = A
        self.b = b
        self.omega = omega
        
    def test_solvable(self):
        try: 
            solve(self.A,self.b)
            print "Your system has a solution"
            return True
        except:
            print "Warning!!\tWarning!!\nYour system has no solution\nProgram exiting."
            