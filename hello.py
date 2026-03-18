toko={

}
count=0
def jual_barang(toko,nama,jumlah):
    toko[nama]["terjual"]+=(jumlah*-1)
def tambah_barang(toko,nama,stok,harga):
    if nama not in toko:
        toko[nama]={
            "stok":stok,
            "harga":harga,
            "terjual":0
        }
    else:
        toko[nama]["stok"]+=stok
        toko[nama]["harga"]=harga
    if stok<0:
        jual_barang(toko,nama,stok)

def ringkasan_penjualan(toko,nama):
    if "terjual" in toko[nama]:
        toko[nama]["pendapatan"]=toko[nama]["terjual"]*toko[nama]["harga"]
    analisis_toko(toko,nama)
def analisis_toko(toko):
    barang_terlaris=None
    stok_tertipis=99999999999999
    total_pendapatan=0
    max_terjual=0
    stok_terendah=None
    for k,v in toko.items():
        
        if "terjual" in v:
            total_pendapatan+=v["terjual"]*v["harga"]
            if v["terjual"]>max_terjual:
                max_terjual=v["terjual"]
                barang_terlaris=k
        
        if v["stok"]<stok_tertipis:
            stok_tertipis=v["stok"]
            stok_terendah=k
    if barang_terlaris==None:
        barang_terlaris="Tidak Ada Penjualan..."
    analisa_penjualan={
        
        "Barang Terlaris:":barang_terlaris,
        "Stok Terendah:":stok_terendah,
        "Total Omset:":total_pendapatan
        
    }
    return analisa_penjualan


while True:
    name=input(f"Masukan Nama Produk (ketik (stop) untuk berhenti):").lower()
    if name=="stop":
        break
    stock=int(input("Masukan jumlah stok:"))
    
    if name not in toko:
        price=int(input(f"Masukan Harga {name}:"))
            
    else:
        validator=input(f"Apakah kamu ingin mengubah harga {name}? jika ingin mengubah harga ketik (iya)").lower()
        if validator=="iya":
            price=int(input(f"Masukan Harga {name}:"))
        else:
            price = toko[name]["harga"]
    tambah_barang(toko,name,stock,price)
print(toko)
pembukuan=analisis_toko(toko)
print(pembukuan)

    