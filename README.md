# 🏥 Sistem Antrean Rumah Sakit (Queue System)

Sistem ini adalah aplikasi manajemen antrean rumah sakit berbasis Python yang mengimplementasikan berbagai struktur data fundamental dan algoritma penjadwalan. Aplikasi ini dirancang untuk mengelola pasien berdasarkan tingkat urgensi menggunakan metode **Weighted Round Robin**.

## 🚀 Fitur Utama

1.  **Multi-Queue Management**: Memisahkan antrean menjadi tiga kategori: Urgent, Prioritas, dan Reguler.
2.  **Weighted Round Robin (3:2:1)**: Algoritma pemanggilan otomatis yang memberikan prioritas lebih tinggi kepada pasien Urgent dan Prioritas.
3.  **CRUD Operasi**:
    *   **Create**: Menambah pasien baru dengan ID otomatis.
    *   **Read**: Mencari data pasien dan melihat daftar antrean.
    *   **Update**: Mengubah data pasien termasuk perpindahan kategori antrean.
    *   **Delete**: Membatalkan antrean pasien.
4.  **Riwayat Panggilan**: Mencatat pasien yang telah dipanggil menggunakan konsep LIFO (Stack).

## 🛠️ Struktur Data yang Digunakan

*   **Queue (FIFO)**: Digunakan untuk mengelola barisan antrean pasien di setiap kategori (`queue_urgent`, `queue_prioritas`, `queue_reguler`).
*   **Hash Table (Dictionary)**: Digunakan untuk `database_pasien`, memungkinkan pencarian data pasien secara instan (O(1)) berdasarkan ID.
*   **Stack (LIFO)**: Digunakan untuk `riwayat_panggilan`, menampilkan pasien yang terakhir dipanggil di posisi paling atas.

## ⚙️ Algoritma Pemanggilan (Weighted Round Robin)

Sistem menggunakan rasio **3:2:1** untuk memastikan keadilan bagi semua kategori namun tetap memprioritaskan yang kritis:
*   **Urgent**: 3 Pasien
*   **Prioritas**: 2 Pasien
*   **Reguler**: 1 Pasien

Siklus akan berulang setelah kuota terpenuhi atau jika antrean tertentu kosong.

### Detail Flowchart Algoritma Panggilan

```mermaid
graph TD
    A[Mulai panggil_pasien] --> B{Apakah SEMUA Queue Kosong?}
    B -- Ya --> C[Reset Kuota ke 3:2:1 & Tampilkan 'Tidak ada antrean']
    C --> Z([Selesai])
    
    B -- Tidak --> D{Kuota Urgent > 0 DAN<br>Queue Urgent ada isi?}
    
    D -- Ya --> D1[Ambil pasien Urgent terdepan]
    D1 --> D2[Kurangi Kuota Urgent -1]
    D2 --> Y[Tampilkan Panggilan & Masukkan ke Riwayat]
    
    D -- Tidak --> E{Kuota Prioritas > 0 DAN<br>Queue Prioritas ada isi?}
    
    E -- Ya --> E1[Ambil pasien Prioritas terdepan]
    E1 --> E2[Kurangi Kuota Prioritas -1]
    E2 --> Y
    
    E -- Tidak --> F{Kuota Reguler > 0 DAN<br>Queue Reguler ada isi?}
    
    F -- Ya --> F1[Ambil pasien Reguler terdepan]
    F1 --> F2[Kurangi Kuota Reguler -1]
    F2 --> Y
    
    F -- Tidak --> G[Reset Siklus!<br>Kuota di-reset kembali 3:2:1]
    G --> H[Panggil Ulang Fungsi secara Rekursif]
    H --> B
    
    Y --> Z([Selesai])
```

## 📊 Flowchart Sistem Secara Umum

```mermaid
graph TD
    A([Mulai]) --> B{Menu Utama}
    
    B -->|1| C[Tambah Pasien]
    C --> C1[Input Nama & Umur]
    C1 --> C2[Pilih Kategori: Urgent/Prioritas/Reguler]
    C2 --> C3[Generate ID & Simpan ke Hash Table]
    C3 --> C4[Masukkan ID ke Queue Terkait]
    C4 --> B

    B -->|2| D{Panggil Pasien}
    D --> D1{Cek Antrean & Kuota}
    D1 -->|Ada| D2[Ambil Pasien sesuai Rasio WRR 3:2:1]
    D2 --> D3[Pindahkan ke Riwayat Stack]
    D3 --> D4[Tampilkan Panggilan]
    D1 -->|Kosong| D5[Tampilkan Pesan Kosong]
    D4 --> B
    D5 --> B

    B -->|3| E[Tampilkan Daftar Antrean]
    E --> B

    B -->|4| F[Cari Pasien via ID]
    F --> F1{Cek di Hash Table}
    F1 -->|Ditemukan| F2[Tampilkan Detail Pasien]
    F1 -->|Tidak Ada| F3[Pesan Error]
    F2 --> B
    F3 --> B

    B -->|5| G[Lihat Riwayat Panggilan]
    G --> B

    B -->|6| H[Edit Data Pasien]
    H --> H1[Input ID Antrean]
    H1 --> H2{Ganti Kategori?}
    H2 -->|Ya| H3[Hapus ID Lama dari Queue & Hash Table]
    H3 --> H4[Generate ID Baru & Masukkan ke Queue Baru]
    H2 -->|Tidak| H5[Update Nama/Umur Saja]
    H4 --> B
    H5 --> B

    B -->|7| I[Batalkan Antrean]
    I --> I1[Hapus dari Queue & Hash Table]
    I1 --> B

    B -->|0| J([Keluar])
```

## 💻 Cara Menjalankan

1.  Pastikan Anda memiliki Python 3.x terinstal.
2.  Jalankan file `main.py` melalui terminal:
    ```bash
    python main.py
    ```

## 📝 Contoh ID Antrean
*   **U-001**: Kategori Urgent
*   **P-002**: Kategori Prioritas
*   **R-003**: Kategori Reguler
