# PERCOBAAN PERTAMA
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Masukkan data
X = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
y = np.array([2, 3, 4, 5, 6])

# Membuat model regresi linier
model = LinearRegression().fit(X, Y)

# Memprediksi nilai
x_pred = np.array([10]).reshape((-1, 1))
y_pred = model.predict(x_prred)
a = model.intercept_
b = model.coef_

#Menghitung r-squared
r_sq = model.score(X, Y)

# Menampilkan hasil
print('Koefisien regresi: ', model.coef_) #m/b
print('Intercept: ', model.intercept_) #c/a
print('Persamaan Regresi : {} + {}x'.format(a,b))
print('Hasil prediksi: ', y_pred)
print('R-squared: ', r_sq)
plt.figure(figsize = (10,8))
plt.plot(X, y, 'b.')
plt.plot(X,model.intercept_ + model.coef_*X, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# PERCOBAAN KEDUA
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-poster')

# generate x and y
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))

# assemble matrix A
A = np.vstack([Y, np.ones(len(x))]).T

# turn y into a column vector
y = y[:, np.newaxis]

# Direct least square regression
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y)
print(alpha)

# plot the results
plt.figure(figsize = (10,8))
plt.plot(x, Y, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()