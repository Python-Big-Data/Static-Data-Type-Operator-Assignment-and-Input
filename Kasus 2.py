# Pak Amir memiliki rumah dengan 4 buah kamar tidur masing-masing berukuran 4 x 4 meter. Apabila pak Amir ingin
# mengubin semua lantai kamar tidurnya dengan keramik berbentuk persegi panjang dengan ukuran 30 x 40 cm, berapa
# buah keramik yang diperlukan untuk pengubinan tersebut? Bantulah pak Amir untuk menghitungnya menggunakan program
# Python! Input program adalah jumlah kamar tidur, ukuran panjang dan lebar kamar tidur, serta panjang dan lebar ukuran
# keramik.

# Pertama hitung luas dari satu buah ubin
panjangUbin = 30
lebarUbin = 40
luasUbin = panjangUbin * lebarUbin
print(luasUbin)

# Kedua cari luas kamar keseluruhan
panjangKamar = 4*100
lebarKamar = 4*100
luasKamar = panjangKamar *lebarKamar
print(luasKamar*4)

# Luas kamar keseluruhan dibagi dengan luas ubin satuan untuk mencari banyak ubin yang diperlukan
banyakUbin = int((luasKamar*4)/luasUbin)
print('maka banyak ubin yang diperlukan ', banyakUbin , 'ubin')
