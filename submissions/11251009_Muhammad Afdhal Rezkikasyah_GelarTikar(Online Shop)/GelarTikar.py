DB_FILENAME = "DB.txt"
def load_db():
    data_list = []
    try:
        file = open(DB_FILENAME, 'r')
        for line in file:
            line = line.strip()
            if not line: continue
            # Ubah string dengan pemisah ; menjadi Array/List
            parts = line.split(';')
            if len(parts) == 4:
                data_list.append([int(parts[0]), parts[1], int(parts[2]), int(parts[3])])
        file.close()
    except (FileNotFoundError, ValueError):
        return [] 
    return data_list
def save_db(data):
    try:
        file = open(DB_FILENAME, 'w')
        for item in data:
            file.write(f"{item[0]};{item[1]};{item[2]};{item[3]}\n")
        file.close()
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")
def tampilkan_tabel(data):
    if not data:
        print("Data kosong.")
    else:
        print("-" * 65)
        print(f"{'ID':<5} | {'Nama Barang':<25} | {'Harga (Rp)':<15} | {'Stok':<5}")
        print("-" * 65)
        for item in data:
            print(f"{item[0]:<5} | {item[1]:<25} | {item[2]:<15} | {item[3]:<5}")
        print("-" * 65)
def bubble_sort_manual(data, index_kolom):
    n = len(data)
    # Loop setiap pass (putaran)
    for i in range(n - 1):
        # Loop membandingkan elemen
        for j in range(n - 1 - i):
            # Bandingkan nilai pada kolom yang diminta
            # Jika elemen sekarang lebih besar dari elemen berikutnya, tukar
            if data[j][index_kolom] > data[j+1][index_kolom]:
                # Proses Swapping (Tukar Posisi)
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
    return data
def sequential_search(data, id_dicari):
    for i in range(len(data)):
        if data[i][0] == id_dicari:
            return i
    return -1
def create(data):
    print("\n[ TAMBAH DATA ]")
    try:
        max_id = 0
        for item in data:
            if item[0] > max_id: max_id = item[0]
        id_barang = max_id + 1
        nama = input("Nama Barang (atau 'q' batal): ")
        if nama.lower() == 'q': return data
        if not nama.strip(): 
            print("x Nama tidak boleh kosong."); return data
        harga_in = input("Harga (Angka): ")
        if harga_in.lower() == 'q': return data
        harga = int(harga_in)
        stok_in = input("Stok (Angka): ")
        if stok_in.lower() == 'q': return data
        stok = int(stok_in)
        data.append([id_barang, nama, harga, stok])
        save_db(data)
        print(">> Data berhasil disimpan!")
    except ValueError:
        print("x Input Harga/Stok harus berupa angka!")
    return data
def read(data):
    while True:
        print("\n[ LIHAT DATA ]")
        tampilkan_tabel(data)
        print("\n1. Urutkan ID (Ascending)")
        print("2. Urutkan Harga Termurah (Bubble Sort)")
        print("3. Cari Barang")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Pilihan: ")
        if pilihan == '1':
            # Menggunakan Bubble Sort Manual pada Index 0 (ID)
            bubble_sort_manual(data, 0)
            print(">> Data diurutkan berdasarkan ID.")
        elif pilihan == '2':
            # Menggunakan Bubble Sort Manual pada Index 2 (Harga)
            bubble_sort_manual(data, 2)
            print(">> Data diurutkan berdasarkan Harga Termurah.")
            save_db(data)
        elif pilihan == '3':
            search_menu(data)
        elif pilihan == '4':
            break
        else:
            print("x Pilihan tidak valid.")
def update(data):
    print("\n[ EDIT DATA ]")
    tampilkan_tabel(data)
    id_in = input("Masukkan ID yang akan diedit (atau 'q' batal): ")
    if id_in.lower() == 'q': return data
    try:
        idx = sequential_search(data, int(id_in))
        if idx != -1:
            print(f"Mengedit: {data[idx][1]}")
            nama = input("Nama baru (Enter jika tetap): ")
            harga = input("Harga baru (Enter jika tetap): ")
            stok = input("Stok baru (Enter jika tetap): ")
            if nama.strip(): data[idx][1] = nama
            if harga.strip(): data[idx][2] = int(harga)
            if stok.strip(): data[idx][3] = int(stok)
            save_db(data)
            print(">> Data berhasil diupdate!")
        else:
            print("ID tidak ditemukan.")
    except ValueError:
        print("Input ID/Harga/Stok harus angka.")
    return data
def delete(data):
    print("\n[ HAPUS DATA ]")
    tampilkan_tabel(data)
    id_in = input("Masukkan ID yang akan dihapus (atau 'q' batal): ")
    if id_in.lower() == 'q': return data
    try:
        idx = sequential_search(data, int(id_in))
        if idx != -1:
            item = data[idx]
            yakin = input(f"Hapus '{item[1]}'? (y/n): ")
            if yakin.lower() == 'y':
                data.pop(idx)
                save_db(data)
                print(">> Data berhasil dihapus.")
        else:
            print("x ID tidak ditemukan.")
    except ValueError:
        print("x Input ID harus angka.")
    return data
def search_menu(data):
    keyword = input("\nMasukkan Nama atau ID yang dicari: ")
    hasil = []
    for item in data:
        # Cek jika keyword ada di Nama (Case Insensitive)
        # ATAU keyword sama dengan ID
        nama_barang = item[1].lower()
        kata_kunci = keyword.lower()
        id_barang_str = str(item[0])
        if kata_kunci in nama_barang or kata_kunci == id_barang_str:
            hasil.append(item)
    print(f"\nHasil Pencarian '{keyword}':")
    tampilkan_tabel(hasil)
    input("Tekan Enter untuk kembali...")
def menu_utama():
    print("\n" + "="*30)
    print(" GELAR TIKAR (Online Shop)\n BY MUHAMMAD AFDHAL REZKIKASYAH")
    print("="*30)
    print("1. Tambah Barang")
    print("2. Lihat & Cari Barang")
    print("3. Edit Barang")
    print("4. Hapus Barang")
    print("5. Keluar")
    return input("Pilih menu [1-5]: ")
# --- PROGRAM UTAMA ---
data_barang = load_db()
while True:
    pilihan = menu_utama()
    if pilihan == '1':
        data_barang = create(data_barang)
    elif pilihan == '2':
        read(data_barang)
    elif pilihan == '3':
        data_barang = update(data_barang)
    elif pilihan == '4':
        data_barang = delete(data_barang)
    elif pilihan == '5':
        print("Terima kasih!")
        break
    else:
        print("x Pilihan tidak valid.")