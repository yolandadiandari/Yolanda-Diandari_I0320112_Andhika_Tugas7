# masukkan jumlah siswa
x = input("Masukkan data nilai:").split(',')

jumlah = len(x)

for i in range(0,len(x)):
    x[i] = int(x[i])

import math
# fungsi 1 : menentukan nilai terendah
print("Nilai paling rendah adalah:", min(x))

#fungsi 2 : menentukan nilai tertinggi
print("Nilai tertinggi adalah", max(x))

#fungsi 3 : menentukan rata-rata nilai mahasiswa
rata_rata = sum(x)/jumlah

#fungsi 4 : pembulatan ke bawah nilai rata-rata
print("Nilai rata-rata : ", math.floor(rata_rata))

#mengurutkan nilai
print("Nilai terendah ke tertinggi adalah", sorted(x))


