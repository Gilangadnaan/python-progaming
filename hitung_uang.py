jumlah_set = int(input("masukan jumlah set transaksi"))

for i in range(jumlah_set) :
    print(f"\n set transaksi ke(1+1)")

    target_uang = int(input("masukan target uang"))

    jumlah_100 = int(input("masukan jumlah lembar/koin uang RP.100:"))
    jumlah_500 = int(input("masukan jumlah lembar/koin uang RP.500:"))
    jumlah_1000 = int(input("masukan jumlah lembar/koin uang RP.1000:"))
    jumlah_5000 = int(input("masukan jumlah lembar/koin uang RP.5000:"))
    jumlah_10000 = int(input("masukan jumlah lembar/koin uang RP.10000:"))
    jumlah_20000 = int(input("masukan jumlah lembar/koin uang RP.20000:"))
    jumlah_50000 = int(input("masukan jumlah lembar/koin uang RP.50000:"))
    jumlah_100000 = int(input("masukan jumlah lembar/koin uang RP.100000:"))

total_uang = (jumlah_100*100)+(jumlah_500*500)+(jumlah_1000*1000)+(jumlah_5000*5000)+(jumlah_10000*10000)+(jumlah_20000*20000)+(jumlah_50000*50000)+(jumlah_100000*100000)

if total_uang > target_uang:
    print ("lebih dari target")

elif total_uang < target_uang:
    print ("kurang dari target")
    
else :
    print ("sama dengan target")