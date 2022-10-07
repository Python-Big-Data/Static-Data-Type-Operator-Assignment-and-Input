# Suatu supermarket buah menjual beberapa jenis buah dengan harga masing-masing per Kg nya sebagai berikut:
# Stawberry : Rp 30.000/Kg, Jeruk : Rp 15.000/Kg, Anggur : Rp 42.000/Kg, Apel : Rp 38.000/Kg, Semangka : Rp 21.000/Kg
# Buatlah script Python untuk membantu pemilik supermarket dalam menghitung jumlah total hasil penjualannya. Input dari
# script ini adalah total berapa Kg penjualan masing-masing jenis buah.

# Membuat daftar harga buah per Kg
print('|----------Daftar Harga Buah per Kg----------|')
print('|1. Stawberry : Rp 30.000/Kg                 |')
print('|2. Jeruk     : Rp 15.000/Kg                 |')
print('|3. Anggur    : Rp 42.000/Kg                 |')
print('|4. Apel      : Rp 38.000/Kg                 |')
print('|5. Semangka  : Rp 21.000/Kg                 |')

buahStrawberry = float(input("Masukkan banyaknya berat buah total buah Strawberry : "))
buahJeruk = float(input("Masukkan banyaknya berat buah total buah Jeruk: "))
buahAnggur = float(input("Masukkan banyaknya berat buah total buah Anggur: "))
buahApel = float(input("Masukkan banyaknya berat buah total buah Apel: "))
buahSemangka = float(input("Masukkan banyaknya berat buah total buah Semangka: "))

hargaTotalStawberry = buahStrawberry * 30000
formatHarga1 = format(hargaTotalStawberry, ",.2f")
print("Harga total penjualan strawberry: Rp" , formatHarga1)

hargaTotalJeruk = buahJeruk * 15000
formatHarga2 = format(hargaTotalJeruk, ",.2f")
print("Harga total penjualan jeruk: Rp" , formatHarga2)

hargaTotalAnggur = buahAnggur * 42000
formatHarga3 = format(hargaTotalAnggur, ",.2f")
print("Harga total penjualan anggur: Rp" , formatHarga3)

hargaTotalApel = buahApel * 38000
formatHarga4 = format(hargaTotalApel, ",.2f")
print("Harga total penjualan apel: Rp" , formatHarga4)

hargaTotalSemangka = buahSemangka * 21000
formatHarga5 = format(hargaTotalSemangka, ",.2f")
print("Harga total penjualan semangka: Rp" , formatHarga5)

hargaTotalSemuaBuah = hargaTotalStawberry + hargaTotalJeruk + hargaTotalAnggur + hargaTotalApel + hargaTotalSemangka
formatharga6 = format(hargaTotalSemuaBuah, ',.2f')
print("Maka total semua harga penjualan adalah Rp ", formatharga6)
