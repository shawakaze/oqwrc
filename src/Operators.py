
from HilbertSpace import *
from constants import *

H = Hgate()
I = I()
K=Kspace(9)

def R(t):
    return cos(t/2.)*I - i*sin(t/2)*sigmay()

def Bounds(A,t):
    U = Ugate(A)
    U = Qobj(U)
    B11 = tensor(I,I,I)
    B12 = tensor(I,H,I)
    B23 = tensor(I,v0*v0.dag(),I)+ tensor(I,v1*v1.dag(),U)
    B34 = B12
    B45 = tensor(I,v0*v0.dag(),I)+tensor(R(t),v1*v1.dag(),I)
    B56 = B12
    B67 = B23.dag()
    B78 = B12
    B89 = tensor(v1*v1.dag(),I,I)
    B99 = B11
    return [B11,B12,B23,B34,B45,B56,B67,B78,B89,B99]

def ForwardPropagation(A,t):
    L = []
    for i in range(1,10):
        L.append(Bounds(A,t)[i])
    return L

def ReversePropagation(A,t):   
    L = []
    for i in range(0,9):
        L.append(Bounds(A,t)[i])
    return L

def SupForward(w,A,t):
    L = []
    w = sqrt(w)
    fp = ForwardPropagation(A,t)
    for i in range(8):
        L.append(tensor(w*fp[i],K[i+1]*K[i].dag()))
    L.append(tensor(w*fp[8],K[8]*K[8].dag()))
    return L

def SupReverse(l,A,t):
    L = []
    l = sqrt(l)
    rp = ReversePropagation(A,t)
    L.append(tensor(l*rp[0],K[0]*K[0].dag()))
    for i in range(1,9):
        L.append(tensor(l*rp[i],K[i-1]*K[i].dag()))
    return L 

def PureForward(A,t):
    L = []
    fp = ForwardPropagation(A,t)
    for i in range(8):
        L.append(tensor(fp[i],K[i+1]*K[i].dag()))
    L.append(tensor(fp[len(fp)-1],K[8]*K[8].dag()))
    return L

def PureReverse(A,t):
    L = []
    rp = ReversePropagation(A,t)
    L.append(tensor(rp[0],K[0]*K[0].dag()))
    for i in range(1,9):
        L.append(tensor(rp[i],K[i-1]*K[i].dag()))
    return L 

 
