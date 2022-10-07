# Tinjau kembali soal nomor 7 di atas. Modifikasi program yang telah dibuat, sehingga bisa menghitung total profit
# dari hasil penjualan buahnya, apabila diketahui harga beli tiap jenis buah adalah sebagai berikut: Stawberry :
# Rp 25.000/Kg, Jeruk : Rp 12.500/Kg, Anggur : Rp 39.000/Kg, Apel : Rp 35.500/Kg, Semangka : Rp 19.200/Kg

# Membuat daftar harga buah per Kg
print('|--------Daftar Harga Buah saat dibeli-------|')
print('|1. Stawberry : Rp 25.000/Kg                 |')
print('|2. Jeruk     : Rp 12.500/Kg                 |')
print('|3. Anggur    : Rp 39.000/Kg                 |')
print('|4. Apel      : Rp 35.500/Kg                 |')
print('|5. Semangka  : Rp 19.200/Kg                 |')

hargaTotalStawberry2 = buahStrawberry * 25000
formatHarga7 = format(hargaTotalStawberry2, ",.2f")
print("Harga total pembelian strawberry: Rp" , formatHarga7)

hargaTotalJeruk2 = buahJeruk * 12500
formatHarga8 = format(hargaTotalJeruk2, ",.2f")
print("Harga total pembelian jeruk: Rp" , formatHarga8)

hargaTotalAnggur2 = buahAnggur * 39000
formatHarga9 = format(hargaTotalAnggur2, ",.2f")
print("Harga total pembelian anggur: Rp" , formatHarga9)

hargaTotalApel2 = buahApel * 35500
formatHarga10 = format(hargaTotalApel2, ",.2f")
print("Harga total pembelian apel: Rp" , formatHarga10)

hargaTotalSemangka2 = buahSemangka * 19200
formatHarga11 = format(hargaTotalSemangka2, ",.2f")
print("Harga total pembelian semangka: Rp" , formatHarga11)

hargaModal = hargaTotalStawberry2 + hargaTotalJeruk2 + hargaTotalAnggur2 + hargaTotalApel2 + hargaTotalSemangka2
formatharga12 = format(hargaModal, ',.2f')
print("Maka total semua harga pembelian adalah Rp ", formatharga12)

profit = hargaTotalSemuaBuah - hargaModal
formatharga14 = format(profit, ',.2f')
print("Maka total profitnya adalah Rp ", formatharga14)