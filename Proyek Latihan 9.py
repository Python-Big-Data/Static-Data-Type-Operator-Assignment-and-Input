# Supermarket X adalah satu-satunya supermarket di Kota Solo terkenal karena kejujurannya. Berapa pun total belanja
# pelanggan, selalu dibulatkan ke bawah ke kelipatan Rp 1.000 rupiah. Sebagai contoh misalkan total belanja pelanggan
# adalah Rp 120.580, maka akan dibulatkan ke Rp 120.000, atau misalkan totalnya Rp 99.999 maka akan dibulatkan ke bawah
# menjadi Rp 99.000 Karena kebaikan supermarket inilah, semakin lama semakin banyak pelanggannya. Namun, karena kasirnya
# masih menggunakan sistem manual (tanpa komputerisasi), maka semakin lama kasir mengalami kerepotan dalam menangani
# transaksi yang semakin banyak per harinya. Buatlah program Python untuk membantu kasir dalam menentukan total belanja
# sesuai ketentuan yang berlaku di supermarket tersebut. Input program adalah total belanja pelanggan, sedangkan
# outputnya
# adalah total belanja setelah pembualatan ke bawah ke kelipatan Rp 1.000

# Melakukan pembulatan ke bawah sebesar 1000
totalBelanja = float(input("Masukkan banyaknya harga total belanjaan: "))
formatBelanja = format(totalBelanja, ",.2f")
print("sebelum dibulatkan ke bawah Rp", formatBelanja)
# Setelah di bulatkan ke bawah sebanyak Rp 1000
totalBelanja2 = int(totalBelanja//1000)
formatBelanja2 = format(totalBelanja2, ",.2f")
print("Sesudah dibulatkan ke bawah Rp", str(totalBelanja2) + ",000,00" )

