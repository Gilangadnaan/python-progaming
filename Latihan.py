jumlah_karyawan = int(input("masukan jumlah karyawan"))
for i in range (jumlah_karyawan):

    jumlah_jam_kerja = float(input("masukan jumlah jam kerja :"))
    gaji_normal = (50000)
    gaji_lembur = (75000)

    if jumlah_jam_kerja > 40 :
        print ("gaji_lembur")
    elif jumlah_jam_kerja < 40 :
        print ("gaji_normal")