tarif_tol = {
    "motor": 500,
    "mobil": 1000,
    "bus": 1500,
    "truk": 2000
}

# Minta input jenis kendaraan, ulangi jika tidak valid
while True:
    jenis = input("Masukkan jenis kendaraan (motor/mobil/bus/truk): ").lower()
    if jenis in tarif_tol:
        break
    else:
        print("❌ Jenis kendaraan tidak dikenali. Silakan masukkan motor, mobil, bus, atau truk.\n")

# Input jarak
while True:
    try:
        jarak = float(input("Masukkan jarak tempuh di jalan tol (dalam km): "))
        if jarak < 0:
            print("❌ Jarak tidak boleh negatif.")
            continue
        break
    except ValueError:
        print("❌ Input jarak harus berupa angka.\n")

# Hitung tarif
tarif = tarif_tol[jenis] * jarak
print(f"\n✅ Tarif tol untuk {jenis} yang menempuh jarak {jarak} km adalah: Rp {int(tarif):,}")
