anggota = [
    "brucewyne",
    "victorstone",
    "ciscoramon"
]

print("=" * 36)
print("*" * 10, "Justice League", "*" * 10)
print("=" * 36)

username = str(input("Masukan username anda: "))

if username not in anggota:
    print("Access Denied")
    raise SystemExit

print(f"{'=' * 5} WELCOME {username} {'=' * 5}")
stop = False
while not stop:
    print("\n1. Tambah Anggota Justice League")
    print("2. Hapus Anggota Justice League")
    print("3. Tampilkan Anggota Justice League")
    print("4. Exit")

    pilihan = int(input("Masukan pilihan anda : "))

    if pilihan == 1:
        a = str(input("Masukan Anggota baru : "))
        anggota.append(a)
        print(f"data '{a}' berhasil ditambahkan")
    elif pilihan == 2:
        a = str(input("Anggota yang akan dihapus : "))

        if a not in anggota:
            print(f"data '{a}' tidak ditemukan")
            raise SystemExit

        anggota.remove(a)
        print(f"data '{a}' berhasil dihapus")
    elif pilihan == 3:
        print("Daftar Anggota Justice League :")

        for x in anggota:
            print(f"| {x} |", end="")
    elif pilihan == 4:
        print(f"see u next time MR.{username} ,GLHF")
        raise SystemExit