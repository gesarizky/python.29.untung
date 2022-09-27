# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
beli = float(input("Tuliskan Harga Beli satuan: "))
jual = float(input("Tuliskan Harga Jual Satuan: "))
jumlah = float(input("Tuliskan Jumlah Barang: "))

# Mengkonversi
untung = jual - beli
total = untung * jumlah
persen = untung / beli * 100

# Menampilkan Hasil
print('=======================================')
print('Maka Keuntungan Perunit = Rp. %d' %(untung))
print('Maka Total Keuntungan  = Rp. %d' %(total))
print('Maka Persentase Untung/Rugi %d Persen' %(persen))
print('=======================================')
