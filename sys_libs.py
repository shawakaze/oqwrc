"""
    The main library to be used is qutip
"""
from qutip import *

"""
    The scipy and matplotlib modules with latex support
"""
from scipy import *
from scipy.linalg import *

import pylab as pl
import numpy as np

from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif')

import sympy
###################################################
import sys
import gtk 
import pygtk
