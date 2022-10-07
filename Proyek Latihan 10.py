# Suatu warung internet (warnet) memberikan taruf akses internet ke pelanggannya Rp 2.250 per 30 menit. Selama
# perhitungan total tarif akses pelanggan dihitung secara manual oleh si pemiilik warnet. Bantulah si pemilik
# warnet untuk mempercepat proses perhitungan tarif akses internet pelanggannya dengan membuat sebuah program.
# Program ini menerima input berupa waktu mulainya seorang pelanggan mengakses internet dan waktu selsesainya.
# Adapun outputnya adalah lamanya akses (dalam jam, menit, dan detik) serta besar tarifnya. Berikut ini tampilan
# interface program yang diharapkan.



nomorKomputer = int(input('Masukkan No Komputer : '))
print('-------------------------------------------------------------------------------------------------------------------------------')
print('Waktu Mulai Akses')
jam1 = int(input('Jam            : '))
menit1 = int(input('Menit          : '))
detik1 = int(input('Detik          : '))
print('-------------------------------------------------------------------------------------------------------------------------------')
print('Waktu Selesai Akses')
jam2 = int(input('Jam            : '))
menit2 = int(input('Menit          : '))
detik2 = int(input('Detik          : '))
print('-------------------------------------------------------------------------------------------------------------------------------')
totalJam = (jam2-jam1)*3600
totalMenit = (menit2-menit1)*60
totalDetik = (detik2-detik1) + totalJam + totalMenit

hh = totalDetik //3600
sisadetik = totalDetik % 3600
mm = sisadetik // 60
ss = sisadetik % 60

print('Total waktu akses:',hh, "jam", mm, 'menit', ss, 'detik' )


totalDetik2 = (((detik2-detik1) + totalJam + totalMenit) / 60)/30

hargaBilling = 2250 * totalDetik2
formatHarga = format(hargaBilling, ',.2f')
print('Total biaya akses No Komputer', nomorKomputer, ': Rp', formatHarga)