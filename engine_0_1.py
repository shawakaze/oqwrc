
"""
    Developer modules
"""

from src import *
from doc import *

P9 = Projection(9,8)

"""
    Input matrix
"""

A = matrix([[1,0],[0,1]])

"""
    The b vector expressed in terms of the eigenvectors of A
"""
b = (1/csr(2))*array([[1],[1]])

"""
    Determination of rotation angle
"""
theta = thetafn(A)
"""
    Real solution from standard gaussian methods
"""
real_solution = DM(A,b)

"""
    Initial density matrix
"""
g = Qobj(b)
g = g.unit()

p0 = tensor(v1*v1.dag(),v0*v0.dag(),g*g.dag(),K[0]*K[0].dag())


def solution_generator(w):
    l = 1-w
    exit_status = False
    P = [p0]
    Kf = SupForward(w,A,theta)
    Kb = SupReverse(l,A,theta)
    n = 0
    while not exit_status:
        Zero_ = tensor(Z(2),Z(2),Z(2),Z(9))
        for j in range(9):
            Zero_ = Zero_ + CPTPmap(Kf[j],Kb[j],P[n])

        P.append(Zero_)
        n = n + 1
        if n>9 :
            exit_status = True
        else:
            exit_status = False
        
    solution = P[len(P)-1]*tensor(I,I,I,P9)
    return [ptrace(solution,2),solution]
    
##########################################################

def draw():
    x,y,z=[],[],[]
    delta = 0.1
    for w in arange(0.5,1,delta):
          p = solution_generator(w)
          solution = p[0]
          l = p[1]
          x.append(w)
          y.append(Probabilityfn(l))
          z.append(fidelity(solution,real_solution))

    figure(1)
    title(r"Probability of detection vs $\omega$")
    ylabel(r"Probability of detection at node 9, $p_9$")
    xlabel(r"$\omega$ - forward propagation amplitude")
    xlim(0.5,1)
    ylim(0,1.4)

    plot1, = plot(x,y,'r')
    legend([plot1],['Probability of detection at node 9'],'upper left')
    #pl.savefig("Probability_of_detection.png") give the file whatever name you want
#-------------------------------------------------------------------------------
    figure(2)
    title(r"Fidelity (actual,oqw) vs $\omega$")
    ylabel(r"Fidelity,$\mathcal{F}(actual-dm,oqw-dm)$")
    xlabel(r"$\omega$ - forward propagation amplitude")
    xlim(0.5,1)
    ylim(0,1.2)
    
    plot2, = plot(x,z,'b')
    legend([plot2],['fidelity between the two solns'],'upper left')
    #pl.savefig("fidelity_plot.png") give what ever name you want

    show()
#welcome()
#draw()
print solution_generator(0.8)
                  
