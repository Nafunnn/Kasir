# Inisialisasi Variabel

total_harga = 0
selesai = False
daftar_barang = {}

# Looping input barang dan harga

while not selesai :
    print("\n1. Tambahkan Barang")
    print("2. Hapus Barang")
    print("3. Selesai\n")
    pilihan = input("Pilih aksi : ")
    
    if pilihan == "1":
        barang = input("\nNama Barang : ")
        harga = int(input("Harga Barang : "))
        
        # Memeriksa keadaan barang di dalam list
        
        if barang in daftar_barang :
            print("\nBarang ", barang, " sudah ada di dalam daftar\n")
        
        else :
            # Menambahkan barang kedalam daftar_barang
            daftar_barang[barang] = harga
            
            # Menambahkan harga kedalam total_harga
            total_harga += harga
            
            # Konfirmasi jika barang sudah masuk kedalam barang
            print("\nBarang ", barang, " sudah masuk kedalam daftar\n")
            
    elif pilihan == "2":
        barang = input("\nNama barang yang akan di hapus : ")
        
        if barang in daftar_barang:
            harga = daftar_barang[barang]
            del daftar_barang[barang]
            total_harga -= harga
            print("\nBarang ", barang, " telah dihapus dari daftar\n")
            
        else:
            print("\nBarang tersebut tidak ada di dalam daftar\n")
    
    elif pilihan == "3":
        selesai = True
        
    else:
        print("\nPilihan tidak valid, silahkan pilih aksi yang tersedia di dalam daftar\n")
        
# Menghitung total harga dengan pajak 10%
total_harga_pajak = total_harga * 1.1

# Menampilkan barang dan harga yang terdapat di dalam daftar_barang
print("\nDaftar Barang")
print("-------------------------")
for barang, harga in daftar_barang.items():
    print(barang, ",", harga)
print("-------------------------\n")

# Menampilkan total_harga_pajak
print("Total harga sebesar : Rp. ", total_harga_pajak,"\n")