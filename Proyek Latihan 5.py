# Buatlah program python yang berguna untuk menghitung luas sebuah lingkaran. Input dari script ini adlah berupa
# jari-jari lingkaran, dan output luasnya adalah luasnya. Gunakan Pi=3.14. Gunakan pula operator ** untuk menghitung
# pangkat dalam perhitungan luasnya.

# Mengambil data dari pengguna
pi = 3.14
panjangJariJari = float(input("Masukkan panjang jari-jari lingkaran yang Anda mau: "))

luasLingkaran = pi * (panjangJariJari**2)
print(int(luasLingkaran))

