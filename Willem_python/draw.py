import numpy as np
import matplotlib.pyplot as plt
from poly_fit import poly_fit

def draw():
	xdata = np.array([0.0, 1.0, 2.0, 2.5, 3.0])
	ydata = np.array([2.9, 3.7, 4.1, 4.4, 5.0])
	
	a = poly_fit(xdata, ydata, 1)
	xapprox = np.array([0.0, 3.0])
	yapprox = np.zeros(2)

	for i in range(len(xapprox)):
		yapprox[i] += a[0] + a[1] * xapprox[i]

	fig, ax = plt.subplots()
	ax.plot(xdata, ydata, 'ro', xapprox, yapprox, 'b-')
	ax.set_aspect('equal')
	ax.grid(True, which = 'both')
	ax.axhline(y=0, color = 'k')
	ax.axvline(x=0, color = 'k')
	ax.set_xlim((-1,6))
	ax.set_ylim((-1,6))

	plt.show()

if __name__ == '__main__':
	draw()
