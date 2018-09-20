import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy import stats

def drawGraph():
	xdata = np.array([0.50, 1.00, 1.50, 2.00, 2.50])
	ydata = np.array([0.49, 1.55, 3.26, 6.74, 10.16])
	func1 = interp1d(xdata, ydata)
	func2 = interp1d(xdata, ydata, kind='cubic')
	slope, intercept, rVal, pVal, stdErr = stats.linregress(xdata, ydata)

	xplot = np.linspace(0., 4., 50)

	fig, ax = plt.subplots()
	ax.plot(xdata, ydata, 'ro', xplot, func1(xplot), 'g-', xplot, func2(xplot), 'b-', xplot, slope * xplot + intercept, 'y-')
	ax.set_aspect('equal')
	ax.grid(True, which = 'both')
	ax.axhline(y=0, color = 'k')
	ax.axvline(x=0, color = 'k')

	plt.show()

if __name__ == '__main__':
	drawGraph()
