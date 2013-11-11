
from constants import *
from sys_libs import *

"""
    K-space or Hilbert space of graph
"""
pi = np.pi
def Kspace(N):
    L = []
    for i in range(N):
        L.append(basis(N,i))
    return L
"""
    K-space transition operators
"""
def D(K,j,i): 
    d = K[i]*K[j].dag()
    return d


def Hgate():
    return (1/sqrt(2))*Qobj(matrix([[1,1],[1,-1]]))
"""
    The next gate is not unitary
"""
def R(G,t):
    return cos(t/2.)*I - i*sin(t/2.)*G

def Ugate(A,N):
    return Qobj(expm(2*pi*i*N*A))

def I():
    return qeye(2)

def Z(n):
    a = np.zeros(n*n)
    a.shape = (n,n)
    a = np.matrix(a)
    return Qobj(a)

def CPTPmap(A,B,p):
    a = A*p*A.dag() + B*p*B.dag()
    return a

def NormalizationCondition(A,B):
    return A.dag()*A + B.dag()*B

def AntiCommutator(A,B):
    return A*B+B*A

def Probabilityfn(A):
    a = ptrace(A,[0,1,2])
    return a.tr()

def TraceDistance(A,B):
    a = A - B
    b = a.dag()*a
    b = b.sqrtm()
    return 0.5*b.tr()

def Expectation(M,p):
    c = (M*p).tr()
    return c

def Projection(N,i):
    a = tensor(I,I,I,Kspace(N)[i]*Kspace(N)[i].dag())
    return a
          
