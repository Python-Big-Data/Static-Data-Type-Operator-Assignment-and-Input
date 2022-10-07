# Jarak dua buah kota A dan B adalah 128.783.082 cm. Dengan menggunakan perintah Python, tuliskan rangkaian ekspresi
# dalam Jupyter Notebook sehingga dihasilkan output sebagai berikut: 128.783.082 cm = ... km + ... m + ... cm

# Mengkonversi ke dalam km dengan menggunakan operator pembagian ke bawah
jarak = 128783082
km = 128783082 // 100000
print(km)

# Menghitung sisa dari jarak
sisa = jarak % 100000
print(sisa)

# Menghitung meter dari sisa
m = sisa // 100
print(m)

# Menghitung cm dari sisa
cm = sisa % 100
print(cm)

# Print secara keseluruhan
print(' 128.783.082 cm = ',km, 'km + ',m, ' m + ', cm,'cm')