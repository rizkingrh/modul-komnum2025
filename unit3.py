#METODE NEWTON RAPHSON
def f(x):
  return x**3 - 2*x**2 + x - 3
def df(x):
  return 3*x**2 - 4*x + 1

def NewtonRaphson(x0, e, N):
  print('\n\n** PENERAPAN METODE NEWTON RAPHSON **')
  step = 1
  flag = 1
  condition = True
  while condition:
    if df(x0) == 0.0:
      print('Turunan fungsi menjadi nol. Pembagian nol terjadi.')
      break
    x1 = x0 - f(x0) / df(x0)
    print('Iterasi ke-%d, x%d = %0.6f dan f(x%d) = %0.6f' % (step, step, x1, step, f(x1)))

    x0 = x2
    step = step + 1
    if step > N:
      flag = 0
      break

    condition = ab(f(x1)) > e
    if flag == 1:
      print('\nHasil: %0.8f' % x1)
    else:
      print('\nTidak Konvergen.')


x0 = float(input('x0: '))
e = float(input('Toleransi error: '))
N = int(input('Maksimum iterasi: '))
NewtonRaphson(x0, e)


#Metode Iterasi Titik Tetap
def g(x):
 return 3 / (x - 2)

def IterasiTitikTetap(x0, e, N):
  print('\n\n** PENERAPAN ITERASI TITIK TETAP **')
  x_previous = x0
  step = 1
  while True:
    x_current = g(x_previous)
    error = abs(x_current - x_previous)
    print('Iterasi ke-%d, x%d = %0.6f, error = %0.6f' % (step, step, x_current, error))

    if error < e or step >= N:
      break
    x_previous = x_current
    step += 1

  if step <= N:
    print('\nHasil: %0.8f' % x_current)
  else:
    print('\nIterasi tidak konvergen dalam %d iterasi.' % N)


x0 = float(input('Masukkan tebakan awal (x0): '))
e = float(input('Masukkan toleransi error (e): '))
N = int(input('Masukkan maksimum iterasi (N): '))
IterasiTitikTetap(x0, e, N)