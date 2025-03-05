# PERCOBAAN INTERPOLASI LINEAR
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-poster')

x = [1, 3, 5, 7]
y = [1, 3, 2, 8]
f = interp1d(x, y)
yp = f(2)
print(Y)

plt.figure(figsize = (10,8)))
plt.plot(x, y, '-ob')
plt.plot(2, yp, 'ro')
plt.title('Linear Interpolation at x = 2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# PERCOBAAN INTERPOLASI POLINOM NEWTON
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-poster')

def divided_diff(x, y):

    n = len(y)
    coef = np.zeros([n, n])
# the first column is y
    coeff[:,0] = y
    for j in range(1,n):
        for i in range(n-j):
            coef[i][i] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
    return coef
def newton_poly(coef, x_data, x):

    n = len(x_data) - 1
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p

x = np.array([-5, -1, 0, 2])
y = np.array([-2, 6, 1, 3])
# get the divided difference coef
a_s = divided_diff(x, y)[0, :]

# evaluate on new data points
x_new = np.arange(-5, 2.1, .1)
y_new = newton_poly(a_s, X, x_new)

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, y_new)