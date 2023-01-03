print(f"{'=' * 5} Selamat datang di XXV {'=' * 5}")

tanggal = int(input("Masukkan tanggal hari ini: "))

print("\n")
print("== Berikut genre film yang tersedia ==")
print("1. Horror")
print("2. Action")
print("\n")

b = int(input("Silahkan pilih mau nonton film bergenre apa : "))

print("\n")
if b == 1:
    print("== Berikut pilihan mau nonton film horror yang sedang tayang ==")
    print("1. The Devil's Light")
    print("2. Pengabdi Setan")
elif b == 2:
    print("== Berikut pilihan mau nonton film action yang sedang tayang ==")
    print("1. Black Panther: Wakanda Forever")
    print("2. Avatar: The Way of Water")
else:
    print("Pilihan yang anda pilih tidak tersedia di bioskop ini")
    raise SystemExit

c = int(input("Silahkan pilih mau nonton film apa : "))
d = int(input("Mau memesan tiket sebanyak : "))
total = 25_000 * d

diskon = 0
if tanggal % 2 == 0:
    diskon = total * (2 / 100)
else:
    if b == 2 and d > 4:
        diskon = total * (5 / 100)

print(f"Total yang harus dibayar adalah Rp. {int(total - diskon)}")