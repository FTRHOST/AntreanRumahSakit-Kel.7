# 🏥 Sistem Antrean Rumah Sakit (Queue System)

Sistem ini adalah aplikasi manajemen antrean rumah sakit berbasis Python yang mengimplementasikan berbagai struktur data fundamental dan algoritma penjadwalan. Aplikasi ini dirancang untuk mengelola pasien berdasarkan tingkat urgensi menggunakan metode **Weighted Round Robin**.

oleh:
1. Azis Khoirul Setiawan (43050250004)
2. Miftakhul Anwar (43050250010)
3. Muhammad Fathir Al Faruq (43050250011)

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

## 📊 Flowchart Sistem

Untuk memudahkan pemahaman, flowchart sistem dibagi menjadi beberapa bagian utama:

### 1. Alur Menu Utama
Menunjukkan navigasi utama dalam aplikasi.

```mermaid
graph TD
    A([Mulai]) --> B{Menu Utama}
    
    B -->|1| C[[Registrasi Pasien]]
    B -->|2| D[[Proses Panggilan]]
    B -->|3| E[Tampilkan Antrean]
    B -->|4| F[[Pencarian Data]]
    B -->|5| G[Lihat Riwayat]
    B -->|6| H[[Edit Data Pasien]]
    B -->|7| I[[Batalkan Antrean]]
    B -->|0| J([Keluar])

    C --> B
    D --> B
    E --> B
    F --> B
    G --> B
    H --> B
    I --> B
```

### 2. Alur Manajemen Pasien (Tambah & Batalkan)
Detail proses pendaftaran pasien baru dan pembatalan antrean.

```mermaid
graph LR
    subgraph Tambah_Pasien
    C1[Input Nama & Umur] --> C2[Pilih Kategori]
    C2 --> C3[Generate ID & Simpan ke Hash Table]
    C3 --> C4[Masukkan ID ke Queue]
    end

    subgraph Batalkan_Antrean
    I1[Input ID Antrean] --> I2[Cek di Hash Table]
    I2 -->|Ada| I3[Hapus dari Queue & Hash Table]
    I2 -->|Tidak| I4[Pesan Error]
    end
```

### 3. Alur Operasi Data (Cari & Edit)
Detail proses pencarian dan pembaruan data pasien.

```mermaid
graph TD
    subgraph Cari_Pasien
    F1[Input ID] --> F2{Cek Hash Table}
    F2 -->|Ditemukan| F3[Tampilkan Detail]
    F2 -->|Tidak| F4[Pesan Error]
    end

    subgraph Edit_Pasien
    H1[Input ID] --> H2{Cek Data}
    H2 -->|Ada| H3{Ubah Kategori?}
    H3 -->|Ya| H4[Hapus ID Lama, Generate ID Baru]
    H3 -->|Tidak| H5[Update Nama/Umur Saja]
    H4 --> H6[Update Queue & Hash Table]
    H5 --> H6
    H2 -->|Tidak| H7[Pesan Error]
    end
```

### 4. Alur Panggilan (Weighted Round Robin)
Proses pemanggilan pasien berdasarkan prioritas rasio 3:2:1.

```mermaid
graph TD
    D_Start[Mulai Panggilan] --> D1{Cek Semua Queue}
    D1 -- Kosong --> D2[Tampilkan Pesan Kosong]
    D1 -- Ada Isi --> D3{Cek Kuota & Queue}
    
    D3 -- Sesuai Rasio --> D4[Ambil Pasien terdepan]
    D4 --> D5[Kurangi Kuota Kategori]
    D5 --> D6[Pindahkan ke Riwayat Stack]
    D6 --> D7[Tampilkan Panggilan]
    
    D3 -- Kuota Habis --> D8[Reset Kuota ke 3:2:1]
    D8 --> D_Start
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
