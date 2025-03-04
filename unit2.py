#METODE SETENGAH INTERVAL
import numpy as np

def fungsi(x):
    return x ** 2 + 3 * x - 6

xi =  float(input('Masukan Nilai xi:'))
xu = float(input('Masukan Nilai Xu:'))
t = float(input('Masukan Nilai t:'))

def biseksi(xi, xu, t):
    if fungsi(xi) * fungsi(xu) >= 0:
        print("Nilai yang diperkirakan untuk xi dan xu tidak tepat\n")
        return

    iterasi = 0
    err = t + 1
    xr_lama = 0
    while err > t:
        iterasi += 1
        xr = (xi + xu) / 2
        if fungsi(xr) == 0.0:
            break
        if fungsi(xi) * fungsi(xr) < 0:
            xu = xr
        else:
            xi = xr
        if xr_lama != 0:
            err = abs((xr - xr_lama)/xr) * (100/100)
        xr_lama = xr


    print("Nilai Akar persamaan : ", xr)
    print("Jumlah iterasi : ", iterasi)
    print("Nilai Error aproksimasi : ", err)

biseksi(xi, xu, t)


#REGULAFALSI

import numpy as np

def fungsi(x):
    return x ** 2 + 3 * x - 6

xi = float(input('Masukan Nilai Xi:'))
xu = float(input('Masukan Nilai Xu:'))
t = float(input('Masukan Nilai t:'))

def regula_falsi(xi, xu, t):
    if fungsi(xi) * fungsi(xu) >= 0:
        print("Nilai yang diperkirakan untuk xi dan xu tidak tepat\n")
        return

    iterasi = 0
    err = t + 1
    xr_lama = 0
    while err > t:
        iterasi += 1
        xr = xu - (fungsi(xu) * (xi - xu)) / (fungsi(xi) - fungsi(xu))
        if fungsi(xr) == 0.0:
            break
        if fungsi(xi) * fungsi(xr) < 0:
            xu = xr
        else:
            xi = xr
        if xr_lama != 0:
            err = abs((xr - xr_lama)/xr) * (100/100)
        xr_lama = xr

    print("Nilai Akar persamaan : ", xr)
    print("Jumlah iterasi : ", iterasi)
    print("Nilai Error aproksimasi : ", err)

regula_falsi(xi, xu, t)