"""
SISTEM PENCARIAN DATA MAHASISWA
Topik 0 - Implementasi Algoritma dan Struktur Data

2 Algoritma: Linear Search, Binary Search
2 Struktur Data: Array/List, Hash Map (Dictionary)
"""

import csv
import time

def load_data_from_csv(filename="database_1000.csv"):
    """Membaca data mahasiswa dari file CSV"""
    data = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    "id": int(row['no']),
                    "nim": row['nim'].strip(),
                    "nama": row['nama'].strip(),
                    "semester": int(row['semester']),
                    "ipk": float(row['ipk']),
                    "program_kelas": row['program_kelas'].strip()
                })
        print(f"\n[✓] Berhasil memuat {len(data)} data dari {filename}")
    except FileNotFoundError:
        print(f"\n[!] File {filename} tidak ditemukan! Pastikan file berada di folder yang sama.")
    except Exception as e:
        print(f"\n[!] Error membaca file: {e}")
    return data

# Inisialisasi data utama dari CSV
data_mahasiswa = load_data_from_csv()
hash_map = {mhs["nim"]: mhs for mhs in data_mahasiswa}  # Hash Map (Dictionary)

# 1. MENU / FUNGSI DATASET
def menu_dataset():
    """Menampilkan menu pilihan dataset"""
    print("\n" + "="*50)
    print("            MENU DATASET MAHASISWA")
    print("="*50)
    print("1. Tampilkan semua data mahasiswa")
    print("2. Tampilkan jumlah data")
    print("3. Muat Ulang / Refresh Data dari CSV")
    print("4. Kembali ke menu utama")
    print("="*50)
    return input("Pilih menu (1-4): ")

def tampilkan_semua_data(data):
    """Menampilkan semua data mahasiswa"""
    if not data:
        print("\n[!] Belum ada data mahasiswa!")
        return
    
    print("\n" + "-"*85)
    print(f"{'No':<5} {'NIM':<15} {'Nama':<20} {'Sem':<6} {'IPK':<6} {'Program Kelas':<25}")
    print("-"*85)
    for mhs in data:
        print(f"{mhs['id']:<5} {mhs['nim']:<15} {mhs['nama']:<20} {mhs['semester']:<6} {mhs['ipk']:<6} {mhs['program_kelas']:<25}")
    print("-"*85)
    print(f"Total: {len(data)} data")

def refresh_data():
    """Memuat ulang data langsung dari file CSV"""
    global data_mahasiswa, hash_map
    data_mahasiswa = load_data_from_csv()
    hash_map = {mhs["nim"]: mhs for mhs in data_mahasiswa}

# 2. TAMBAH DATA (MANUAL)
def tambah_data():
    """Menambah data mahasiswa secara manual"""
    global data_mahasiswa, hash_map
    
    print("\n--- TAMBAH DATA MAHASISWA ---")
    try:
        nim = input("Masukkan NIM: ").strip()
        if not nim:
            print("[!] NIM tidak boleh kosong!")
            return
        
        # Cek duplikat
        if nim in hash_map:
            print(f"[!] NIM {nim} sudah terdaftar!")
            return
        
        nama = input("Masukkan Nama: ").strip()
        semester = int(input("Masukkan Semester: "))
        ipk = float(input("Masukkan IPK: "))
        program_kelas = input("Masukkan Program Kelas: ").strip()
        
        new_id = len(data_mahasiswa) + 1
        mhs_baru = {
            "id": new_id,
            "nim": nim,
            "nama": nama,
            "semester": semester,
            "ipk": ipk,
            "program_kelas": program_kelas
        }
        
        data_mahasiswa.append(mhs_baru)
        hash_map[nim] = mhs_baru
        
        print(f"\n[✓] Data mahasiswa berhasil ditambahkan ke memori!")
        print(f"NIM: {nim} | Nama: {nama}")
        
    except ValueError:
        print("[!] Masukkan data angka dengan benar pada kolom Semester/IPK!")

# 3. UBAH / HAPUS DATA
def ubah_data():
    """Mengubah data mahasiswa berdasarkan NIM"""
    global data_mahasiswa, hash_map
    
    print("\n--- UBAH DATA MAHASISWA ---")
    nim = input("Masukkan NIM yang akan diubah: ").strip()
    
    if nim not in hash_map:
        print(f"[!] NIM {nim} tidak ditemukan!")
        return
    
    print("\nData ditemukan:")
    mhs = hash_map[nim]
    print(f"Nama         : {mhs['nama']}")
    print(f"Semester     : {mhs['semester']}")
    print(f"IPK          : {mhs['ipk']}")
    print(f"Program Kelas: {mhs['program_kelas']}")
    
    print("\nMasukkan data baru (kosongkan jika tidak diubah):")
    
    nama_baru = input("Nama baru: ").strip()
    semester_baru = input("Semester baru: ").strip()
    ipk_baru = input("IPK baru: ").strip()
    program_kelas_baru = input("Program Kelas baru: ").strip()
    
    # Update data
    if nama_baru:
        mhs["nama"] = nama_baru
    if semester_baru:
        try:
            mhs["semester"] = int(semester_baru)
        except ValueError:
            print("[!] Semester harus berupa angka, tidak diubah!")
    if ipk_baru:
        try:
            mhs["ipk"] = float(ipk_baru)
        except ValueError:
            print("[!] IPK harus berupa angka/desimal, tidak diubah!")
    if program_kelas_baru:
        mhs["program_kelas"] = program_kelas_baru
    
    # Update di list juga
    for idx, item in enumerate(data_mahasiswa):
        if item["nim"] == nim:
            data_mahasiswa[idx] = mhs
            break
    
    print(f"\n[✓] Data NIM {nim} berhasil diubah di memori!")

def hapus_data():
    """Menghapus data mahasiswa berdasarkan NIM"""
    global data_mahasiswa, hash_map
    
    print("\n--- HAPUS DATA MAHASISWA ---")
    nim = input("Masukkan NIM yang akan dihapus: ").strip()
    
    if nim not in hash_map:
        print(f"[!] NIM {nim} tidak ditemukan!")
        return
    
    mhs = hash_map[nim]
    print(f"\nData akan dihapus:")
    print(f"Nama: {mhs['nama']} | Sem: {mhs['semester']} | Kelas: {mhs['program_kelas']}")
    
    konfirmasi = input("\nYakin ingin menghapus? (y/n): ").strip().lower()
    if konfirmasi == 'y':
        # Hapus dari list
        data_mahasiswa = [m for m in data_mahasiswa if m["nim"] != nim]
        # Hapus dari hash map
        del hash_map[nim]
        print(f"\n[✓] Data NIM {nim} berhasil dihapus dari memori!")
    else:
        print("[!] Penghapusan dibatalkan.")

# 4. ALGORITMA LINEAR SEARCH
def linear_search(data, target_nim):
    """
    Pencarian Linear - memeriksa satu per satu
    Kompleksitas: O(n)
    """
    langkah = 0
    for mhs in data:
        langkah += 1
        if mhs["nim"] == target_nim:
            return mhs, langkah
    return None, langkah

# 5. ALGORITMA BINARY SEARCH
def binary_search(data, target_nim):
    """
    Pencarian Binary - membagi data menjadi dua
    Syarat: data harus terurut berdasarkan NIM
    Kompleksitas: O(log n)
    """
    sorted_data = sorted(data, key=lambda x: x["nim"])
    low = 0
    high = len(sorted_data) - 1
    langkah = 0
    
    while low <= high:
        langkah += 1
        mid = (low + high) // 2
        if sorted_data[mid]["nim"] == target_nim:
            return sorted_data[mid], langkah
        elif sorted_data[mid]["nim"] < target_nim:
            low = mid + 1
        else:
            high = mid - 1
    
    return None, langkah

# 6. PENCARIAN DENGAN HASH MAP
def hash_search(target_nim):
    """
    Pencarian menggunakan Hash Map (Dictionary)
    Kompleksitas: O(1) rata-rata
    """
    return hash_map.get(target_nim)

# 7. PENGUKURAN WAKTU EKSEKUSI
def ukur_waktu(func, *args):
    """Mengukur waktu eksekusi suatu fungsi"""
    start = time.perf_counter()
    hasil = func(*args)
    end = time.perf_counter()
    waktu = (end - start) * 1000  # dalam milidetik
    return hasil, waktu

# 8. MENU PENCARIAN
def menu_pencarian():
    """Menu utama untuk pencarian data"""
    print("\n" + "="*50)
    print("            MENU PENCARIAN DATA")
    print("="*50)
    print("1. Linear Search (data tidak perlu diurutkan)")
    print("2. Binary Search (data harus diurutkan)")
    print("3. Hash Map Search (pencarian cepat via NIM)")
    print("4. Bandingkan semua metode")
    print("5. Kembali ke menu utama")
    print("="*50)
    return input("Pilih menu (1-5): ")

def tampilkan_hasil_pencarian(mhs, langkah, waktu, metode):
    """Menampilkan hasil pencarian"""
    if mhs:
        print(f"\n[✓] Data ditemukan!")
        print(f"Metode: {metode}")
        print(f"Langkah: {langkah}")
        print(f"Waktu: {waktu:.6f} ms")
        print("-"*45)
        print(f"No           : {mhs['id']}")
        print(f"NIM          : {mhs['nim']}")
        print(f"Nama         : {mhs['nama']}")
        print(f"Semester     : {mhs['semester']}")
        print(f"IPK          : {mhs['ipk']}")
        print(f"Program Kelas: {mhs['program_kelas']}")
        print("-"*45)
    else:
        print(f"\n[✗] Data tidak ditemukan!")
        print(f"Langkah: {langkah}")
        print(f"Waktu: {waktu:.6f} ms")

def bandingkan_semua():
    """Membandingkan semua metode pencarian"""
    print("\n" + "="*50)
    print("         PERBANDINGAN METODE PENCARIAN")
    print("="*50)
    
    nim = input("Masukkan NIM yang dicari: ").strip()
    if not nim:
        print("[!] NIM tidak boleh kosong!")
        return
    
    print(f"\nMencari NIM: {nim}")
    print("-"*50)
    
    # 1. Linear Search
    (hasil_ls, langkah_ls), waktu_ls = ukur_waktu(linear_search, data_mahasiswa, nim)
    tampilkan_hasil_pencarian(hasil_ls, langkah_ls, waktu_ls, "Linear Search")
    
    print("-"*50)
    
    # 2. Binary Search
    (hasil_bs, langkah_bs), waktu_bs = ukur_waktu(binary_search, data_mahasiswa, nim)
    tampilkan_hasil_pencarian(hasil_bs, langkah_bs, waktu_bs, "Binary Search")
    
    print("-"*50)
    
    # 3. Hash Map Search
    start = time.perf_counter()
    hasil_hm = hash_search(nim)
    end = time.perf_counter()
    waktu_hm = (end - start) * 1000
    langkah_hm = 1
    
    tampilkan_hasil_pencarian(hasil_hm, langkah_hm, waktu_hm, "Hash Map Search")
    
    print("-"*50)
    
    # Rekomendasi berdasarkan hasil empiris waktu terkecil
    print("\n" + "="*50)
    print("              REKOMENDASI")
    print("="*50)
    print("Berdasarkan hasil pengujian di atas:")
    
    if waktu_ls < waktu_bs and waktu_ls < waktu_hm:
        print("✓ Linear Search adalah yang tercepat untuk kasus ini")
    elif waktu_bs < waktu_ls and waktu_bs < waktu_hm:
        print("✓ Binary Search adalah yang tercepat untuk kasus ini")
    else:
        print("✓ Hash Map Search adalah yang tercepat untuk kasus ini")
    
    print("\nRekomendasi umum:")
    print("- Untuk pencarian berdasarkan NIM, gunakan Hash Map (O(1))")
    print("- Untuk data yang sudah terurut, gunakan Binary Search (O(log n))")
    print("- Untuk data kecil atau tidak terurut, gunakan Linear Search (O(n))")
    print("="*50)

# 10. MENU UTAMA
def menu_utama():
    """Menu utama aplikasi"""
    while True:
        print("\n" + "="*50)
        print("   SISTEM PENCARIAN DATA MAHASISWA")
        print("="*50)
        print("1. Kelola Dataset")
        print("2. Tambah Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Pencarian Data")
        print("6. Tampilkan Semua Data")
        print("7. Keluar")
        print("="*50)
        print(f"Total Data: {len(data_mahasiswa)} mahasiswa")
        print("="*50)
        
        pilihan = input("Pilih menu (1-7): ")
        
        if pilihan == '1':
            while True:
                sub = menu_dataset()
                if sub == '1':
                    tampilkan_semua_data(data_mahasiswa)
                elif sub == '2':
                    print(f"\nTotal data mahasiswa: {len(data_mahasiswa)}")
                elif sub == '3':
                    refresh_data()
                elif sub == '4':
                    break
                else:
                    print("[!] Pilihan tidak valid!")
        elif pilihan == '2':
            tambah_data()
        elif pilihan == '3':
            ubah_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            while True:
                sub = menu_pencarian()
                if sub == '1':
                    nim = input("Masukkan NIM: ").strip()
                    if nim:
                        (hasil, langkah), waktu = ukur_waktu(linear_search, data_mahasiswa, nim)
                        tampilkan_hasil_pencarian(hasil, langkah, waktu, "Linear Search")
                elif sub == '2':
                    nim = input("Masukkan NIM: ").strip()
                    if nim:
                        (hasil, langkah), waktu = ukur_waktu(binary_search, data_mahasiswa, nim)
                        tampilkan_hasil_pencarian(hasil, langkah, waktu, "Binary Search")
                elif sub == '3':
                    nim = input("Masukkan NIM: ").strip()
                    if nim:
                        start = time.perf_counter()
                        hasil = hash_search(nim)
                        end = time.perf_counter()
                        waktu = (end - start) * 1000
                        tampilkan_hasil_pencarian(hasil, 1, waktu, "Hash Map Search")
                elif sub == '4':
                    bandingkan_semua()
                elif sub == '5':
                    break
                else:
                    print("[!] Pilihan tidak valid!")
        elif pilihan == '6':
            tampilkan_semua_data(data_mahasiswa)
        elif pilihan == '7':
            print("\nTerima kasih telah menggunakan sistem!")
            break
        else:
            print("[!] Pilihan tidak valid!")

if __name__ == "__main__":
    menu_utama()