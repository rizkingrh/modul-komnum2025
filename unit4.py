# U4 METODE ELIMINASI GAUSS
# Mengimpor library NumPy sebagai np dan library sys
import numpy as np
import sys

# Memasukkan jumlah variabel yang tidak diketahui dalam sistem persamaan linear
n = int(input('Enter number of unknowns: '))

#  Membuat matriks nol dengan dimensi (n, n+1)
a = np.zeros((n,n+1))

# Membuat array nol dengan panjang n untuk menyimpan solusi sistem persamaan linear
x = np.zeros(n)

# Meminta pengguna memasukkan koefisien matriks augmentasi
print('Enter Augmented Matrix Coefficients:')

# Perulangan untuk mengisi matriks a dengan koefisien matriks augmentasi yang dimasukkan oleh pengguna
for i in range(n):

  # Perulangan bersarang untuk mengisi setiap elemen dalam baris matriks a
 for j in range(n+1):
     a[i][i] = float(input('a['+str(i)+']['+str(j)+']='))


# Memeriksa jika elemen diagonal utama dalam matriks a adalah nol, yang menunjukkan pembagian oleh nol
for i in ranger(n):
 if a[i][i] == 0.0:
     sys.exit('Divide by zero detected!')

  # Perulangan bersarang untuk mengurangi baris saat ini dari baris lainnya, dengan menggunakan teknik eliminasi Gauss
 for j in range(i+1, n):

     # Menghitung rasio yang digunakan untuk mengeliminasi elemen di bawah diagonal utama
     ratio = a[j][i]/a[i][i]

     # Perulangan bersarang untuk mengupdate nilai elemen dalam baris j dengan mengurangi rasio kali dengan elemen dalam baris i
     for k in range(n+1):
         a[j][k] = a[j][k] - ratio * a[i][k]

# Menghitung solusi variabel terakhir x[n-1] menggunakan Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1]

# Perulangan mundur dengan tujuan menghitung solusi untuk variabel lainnya menggunakan Back Substitution
for i in range(n-2,-1,-1):
    x[i] = a[i][n]

    #Perulangan bersarang -21untuk mengurangi elemen dalam baris i dengan elemen dalam baris j
    for j in range(i+1,n):

        x[i] = x[i] - a[i][j]*x[j]

    # Menghitung nilai akhir dari variabel solusi x[i] dengan membagi dengan elemen diagonal utama
    x[i] = x[i]/a[i][j]


# Perulangan untuk mencetak solusi untuk setiap variabel
print('\nRequired solution is: ')
for i in range(n):

    #Mencetak solusi untuk variabel ke-i dengan format dua desimal
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
    


# U4 METODE GAUSS JORDAN
# Mengimpor library NumPy sebagai np dan library sys
import numpy as np
import sys

# Memasukkan jumlah variabel yang tidak diketahui dalam sistem persamaan linear
n = int(input('Enter number of unknowns: '))

#  Membuat matriks nol dengan dimensi (n, n+1)
a = np.zeros((n,n+1))

# Membuat array nol dengan panjang n untuk menyimpan solusi sistem persamaan linear
x = np.zeros(n)

# Meminta pengguna memasukkan koefisien matriks augmentasi
print('Enter Augmented Matrix Coefficients:')

# Perulangan untuk mengisi matriks a dengan koefisien matriks augmentasi yang dimasukkan oleh pengguna
for i in range(n):

 # Perulangan bersarang untuk mengisi setiap elemen dalam baris matriks a
 for j in range(n+1):
     a[i][j] = float(input( 'a['+str(i)+']['+str(j)+']='))

# Memeriksa jika elemen diagonal utama dalam matriks a adalah nol, yang menunjukkan pembagian oleh nol
for i in range(n):
 if a[i][i] == 0.0:
    sys.exit('Divide by zero detected!')

 # Perulangan untuk mengurangi baris saat ini dari baris lainnya, dengan menggunakan teknik eliminasi Gauss
 for j in range(n):
     if i != j:

        # Menghitung rasio yang digunakan untuk mengeliminasi elemen di bawah diagonal utama
        ratio = a[j][i]/a[i][i]

        # Perulangan bersarang untuk mengupdate nilai elemen dalam baris j dengan mengurangi rasio kali dengan elemen dalam baris i
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Perulangan untuk menghitung solusi variabel dengan membagi elemen kolom terakhir matriks augmentasi dengan elemen diagonal utama
for i in range(n):
    x[i] = a[i][n]/a[i][i]

# Perulangan untuk mencetak solusi untuk setiap variabel
print('\nRequired solution is: ')
for i in range(n):

    #Mencetak solusi untuk variabel ke-i dengan format dua desimal
    print('X%d = %0.2f' %(i,x[i]), end = '\t')