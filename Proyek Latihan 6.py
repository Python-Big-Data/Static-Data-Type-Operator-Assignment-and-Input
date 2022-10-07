# Buatlah program Python yang berguna untuk mengkonversi suhu dari sebuah celcius (input) ke satuan suhu lainnya,
# yaitu Reamur, Romer, Kelvin, Rankine, Newton, Fahrenheit, dan Delisle. Hasil konversi inilah yang menjadi outputnya.
# Gunakan tabel rumus konversi suhu di : wikipedia

celcius = float(input("Masukkan derajat celcius: "))

# Konversi suhu dari celcius ke Fahrenheit
konversiFahrenheit = ((celcius *  9)/5) + 32
print("Suhu Fahrenheitnya adalah ", konversiFahrenheit, "derajat Fahrenheit")

# Konversi suhu dari celcius ke Kelvin
konversiKelvin = celcius + 273.15
print("Suhu Kelvin adalah ", konversiKelvin, "kelvin")

# Konversi suhu dari celcius ke Rankine
konversiRankine = format((celcius + 273.15) * 9/5, ",.2f")
print("Suhu Rankine adalah ", konversiRankine, "derajat Rankine")

# Konversi suhu dari celcius ke Delisle
konversiDelisle = (100 - celcius) * 3/2
print("Suhu Delisle adalah ", konversiDelisle, "derajat Delisle")

# Konversi suhu dari celcius ke Newton
konversiNewton = celcius * 33/100
print("Suhu Newton adalah ", konversiNewton, "derajat Newton")

# Konversi suhu dari celcius ke Reamur
konversiReamur = celcius * 4/5
print("Suhu Reamur adalah ", konversiReamur, "derajat Reamur")

# Konversi suhu dari celcius ke Romer
konversiRomer = (celcius * 21/40) + 7.5
print("Suhu Romer adalah ", konversiRomer, "derajat Romer")