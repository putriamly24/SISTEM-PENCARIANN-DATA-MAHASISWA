import numpy as np
import matplotlib.pyplot as plt

def generate_grafik_big_o():
    # 1. Menentukan rentang data n dari 1 sampai 100
    n = np.arange(1, 101)

    # 2. Menghitung nilai matematika untuk masing-masing kompleksitas
    y_linear = n                     # O(n)
    y_binary = np.log2(n)            # O(log n) - menggunakan basis 2 sesuai cara kerja binary search
    y_hash = np.ones_like(n)         # O(1) - nilainya selalu konstan 1

    # 3. Pengaturan ukuran kanvas grafik
    plt.figure(figsize=(9, 6))

    # 4. Plot kurva dengan warna dan label yang sesuai dengan gambar
    plt.plot(n, y_linear, color='red', label='Linear Search - O(n)', linewidth=1.8)
    plt.plot(n, y_binary, color='orange', label='Binary Search - O(log n)', linewidth=1.8)
    plt.plot(n, y_hash, color='green', label='Hash Map - O(1)', linewidth=1.8)

    # 5. Konfigurasi Judul dan Label Sumbu (Axis)
    plt.title('Grafik Perbandingan Kompleksitas Waktu (Big O Notation)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Jumlah Elemen Data (n)', fontsize=11, labelpad=8)
    plt.ylabel('Langkah Operasi / Waktu Komputasi', fontsize=11, labelpad=8)

    # 6. Menampilkan garis kotak-kotak (grid) samar seperti di gambar
    plt.grid(True, linestyle='--', alpha=0.6)

    # 7. Menampilkan legenda di sudut kiri atas
    plt.legend(loc='upper left', fontsize=10)

    # 8. Mengatur batas minimal dan maksimal sumbu Y agar rapi
    plt.ylim(-5, 105)

    # Menampilkan grafik ke layar
    plt.tight_layout()
    print("[✓] Menampilkan grafik Big O... Tutup jendela grafik untuk selesai.")
    plt.show()

if __name__ == "__main__":
    generate_grafik_big_o()