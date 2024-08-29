jumlah_siswa = int(input("masukan jumlah siswa"))

for i in range (jumlah_siswa + 1):
    nama=input ("masukan nama siswa")

    a = int(input("masukan nilai tugas1"))
    b = int(input("masukan nilai tugas2"))
    c = int(input("masukan nilai tugas3"))


    jumlah = a+b+c 

    rata_rata = jumlah / 3

    if rata_rata >=70:
        print("kamu lulus")
    elif rata_rata >=50 and rata_rata <=69:
        print("kamu perlu prebaikan")
    else:
        print("kamu tidak lulus")
    