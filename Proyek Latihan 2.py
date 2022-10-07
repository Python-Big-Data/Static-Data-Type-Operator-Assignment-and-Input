# Tinjau kembali soal nomor 1 di atas . Terkadang untuk pengubinan diperlukan tambahan beberapa keramik sebagai
# cadangan jika ada yang rusak selama proses pengubinan. Apabila keramik cadangan disiapkan sekitar 10% dari total
# keramik yang diperlukan, maka hitunglah total box keramik yang diperlukan untuk pengubinan!

# Kita cari dulu banyak ubin 10% itu
sepuluhPersen = (banyakUbin * 10)/100
print(sepuluhPersen)

totalUbin = banyakUbin + sepuluhPersen
jumlahBoxTambahan = int(totalUbin/5)
print('Banyak box ubin setelah ditambahkan 10 % ubin menjadi',jumlahBoxTambahan, 'box')

