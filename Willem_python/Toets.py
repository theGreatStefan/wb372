import scipy as sc
import numpy as np
from scipy.integrate import quad

def Question_a():
	a = 0
	b = 1
	f = lambda x: x**(-1/4) * np.sin(x)
	answer = quad(f, a, b)

	print answer

def Question_b():
	a = 1
	b = np.inf
	f = lambda x: 1/(1+x**4)
	answer = quad(f, a, b)

	print answer

def Question_c():
	a = 0
	b = np.inf
	f = lambda x: 1/(1+x**4)
	answer = quad(f, a, b)

	print answer
