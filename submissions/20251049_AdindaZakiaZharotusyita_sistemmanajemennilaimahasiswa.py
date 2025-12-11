data_mahasiswa = []

def create_data():
    print("\n=== Tambah Data Mahasiswa ===")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    try:
        nilai = int(input("Masukkan Nilai: "))
    except ValueError:
        print("Nilai harus berupa angka!")
        return
    data_mahasiswa.append([nim, nama, nilai])
    print("Data berhasil ditambahkan!")

def read_data():
    print("\n=== Daftar Data Mahasiswa ===")
    if len(data_mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
    else:
        print(f"{'NIM':<10} {'Nama':<15} {'Nilai':<5}")
        print("-" * 32)
        for mhs in data_mahasiswa:
            print(f"{mhs[0]:<10} {mhs[1]:<15} {mhs[2]:<5}")

def update_data():
    print("\n=== Ubah Nilai Mahasiswa ===")
    nim = input("Masukkan NIM mahasiswa yang ingin diubah nilainya: ")

    for mhs in data_mahasiswa:
        if mhs[0] == nim:
            print(f"Data ditemukan: Nama: {mhs[1]}, Nilai lama: {mhs[2]}")

            nilai_baru = input("Masukkan Nilai baru: ")

            try:
                mhs[2] = int(nilai_baru)
            except ValueError:
                print("Nilai harus berupa angka!")
                return

            print("Nilai berhasil diperbarui!")
            return

    print("Data dengan NIM tersebut tidak ditemukan.")


def delete_data():
    print("\n=== Hapus Data Mahasiswa ===")
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    for mhs in data_mahasiswa:
        if mhs[0] == nim:
            data_mahasiswa.remove(mhs)
            print("Data berhasil dihapus!")
            return
    print("Data dengan NIM tersebut tidak ditemukan.")

def sort_data():
    print("\n=== Urutkan Data Mahasiswa (Nilai Besar ke Kecil) ===")

    if len(data_mahasiswa) == 0:
        print("Belum ada data!")
        return

    data_mahasiswa.sort(key=lambda x: x[2], reverse=True)

    print("Data berhasil diurutkan!")
    read_data()

def search_data():
    print("\n=== Cari Data Mahasiswa ===")
    keyword = input("Masukkan NIM atau Nama yang ingin dicari: ")

    print("\nHasil Pencarian:")
    print(f"{'NIM':<10} {'Nama':<15} {'Nilai':<5}")
    print("-" * 32)

    ditemukan = False
    for mhs in data_mahasiswa:
        if keyword.lower() in mhs[0].lower() or keyword.lower() in mhs[1].lower():
            print(f"{mhs[0]:<10} {mhs[1]:<15} {mhs[2]:<5}")
            ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan.")

def menu():
    while True:
        print("\n═══════════════════════════════════════")
        print("   SISTEM MANAJEMEN NILAI MAHASISWA")
        print("⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖")
        print("1. Tambah Data Mahasiswa")
        print("2. Lihat Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Urutkan Data Mahasiswa (Nilai)")
        print("6. Cari Mahasiswa")
        print("7. Keluar")
        print("─────────────  ⋆⋅☆⋅⋆ ───────────")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            create_data()
        elif pilihan == "2":
            read_data()
        elif pilihan == "3":
            update_data()
        elif pilihan == "4":
            delete_data()
        elif pilihan == "5":
            sort_data()
        elif pilihan == "6":
            search_data()
        elif pilihan == "7":
            print("Terima kasih! Program selesai. 👋")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
menu()