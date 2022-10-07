# Pak Maman ingin menukarkan uangnya sejumlah Rp. 32.892.700 ke dalam pecahan uang Rp 100.000, Rp 50.000, Rp 10.000,
# Rp 5.000, Rp 1.000, Rp 500, dan Rp 100 ke Pak Budi. bank. Buatlah program python yang bisa membantu mempercepat
# Pak Budi dalam menentukan berapa buah/lembar uang untuk masing-masing pecahan tersebut!

uang = 32892700
# Konversi ke dalam pecahan 100.000
seratusRibu = uang//100000
print(seratusRibu)

sisa = uang % 100000
print(sisa)

limapuluhRibuSisa = sisa % 50000
print(limapuluhRibuSisa)

limapuluhRibu = sisa // 50000
print(limapuluhRibu)

sepuluhRibu = limapuluhRibuSisa // 10000
print(sepuluhRibu)

sepuluhRibuSisa = limapuluhRibuSisa % 10000
print(sepuluhRibuSisa)

seribu = sepuluhRibuSisa // 1000
print(seribu)

seribuSisa = sepuluhRibuSisa % 1000
print(seribuSisa)

limaRatus = seribuSisa // 500
print(limaRatus)

limaRatusSisa = seribuSisa % 500
print(limaRatusSisa)

seratus = limaRatusSisa // 100
print(seratus)

seratusSisa = limaRatusSisa % 100
print(seratusSisa)

print("Jadi masing-masing uang ada ",seratusRibu, "lembar uang Rp 100.000,", limapuluhRibu, "lembar uang Rp 50.000,",
      sepuluhRibu,
    "lembar uang Rp 10.000,",seribu ,"lembar uang Rp 1000", limaRatus, "buah uang Rp 500", seratus, "buah uang Rp 100")