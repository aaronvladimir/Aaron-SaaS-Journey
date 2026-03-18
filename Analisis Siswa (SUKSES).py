data={

}
def data1(data,nama,nilai):
    if nama not in data:
        data[nama]=[nilai]
    else:
        data[nama].append(nilai)

def kalkulasi(data):
    hasil_kalkulasi={

    }
    for k,v in data.items():
        rata=sum(v)/len(v)
        maks=max(v)
        mins=min(v)

        hasil_kalkulasi[k]={
        "Nilai":v.copy(),
        "Rata-Rata":rata,
        "Nilai Maksimum":maks,
        "Nilai Minimum":mins
        }
        
    return hasil_kalkulasi



while True:
    nama=input("Masukan Nama Siswa, Ketik (stop) untuk mengakhiri:")
    if nama=="stop":
        break
    nilai=int(input(f"Masukan Nilai {nama}:"))
    data1(data,nama,nilai)

hasil=kalkulasi(data)
for k,v in hasil.items():
    print(
        k,
        "Nilai Total Ujian:",v["Nilai"],
        "Nilai Maksimal:",v["Nilai Maksimum"],
        "Nilai Minimal:",v["Nilai Minimum"],
        "Nilai Rata-Rata:,",v["Rata-Rata"]
    )


