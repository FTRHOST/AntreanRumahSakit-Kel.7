import time

class SistemAntreanRS:
    def __init__(self):
        # 1. Konsep QUEUE (FIFO)
        self.queue_urgent = []
        self.queue_prioritas = []
        self.queue_reguler = []
        
        # 2. Konsep HASH TABLE (Dictionary)
        self.database_pasien = {}
        
        # 3. Konsep STACK (LIFO)
        self.riwayat_panggilan = []
        
        self.counter = 1 
        
    def tambah_antrean(self, nama, umur, kategori):
        id_antrean = f"{kategori[0].upper()}-{self.counter:03d}"
        self.counter += 1
        
        pasien_baru = {
            'id': id_antrean,
            'nama': nama,
            'umur': umur,
            'kategori': kategori,
            'waktu_daftar': time.strftime("%H:%M:%S")
        }
        self.database_pasien[id_antrean] = pasien_baru
        
        kategori_lower = kategori.lower()
        if kategori_lower == 'urgent':
            self.queue_urgent.append(id_antrean)
        elif kategori_lower == 'prioritas':
            self.queue_prioritas.append(id_antrean)
        else:
            self.queue_reguler.append(id_antrean)
            
        print(f"\n✅ Berhasil! Pasien '{nama}' mendapat ID Antrean: {id_antrean}")

    def panggil_pasien(self):
        id_panggilan = None
        
        if len(self.queue_urgent) > 0:
            id_panggilan = self.queue_urgent.pop(0)
        elif len(self.queue_prioritas) > 0:
            id_panggilan = self.queue_prioritas.pop(0)
        elif len(self.queue_reguler) > 0:
            id_panggilan = self.queue_reguler.pop(0)
        else:
            print("\n📭 Tidak ada antrean saat ini.")
            return
            
        pasien = self.database_pasien[id_panggilan]
        print(f"\n📢 PANGGILAN PASIEN:")
        print(f"   Mohon perhatian, pasien dengan ID {pasien['id']} atas nama {pasien['nama']}")
        print(f"   Silakan menuju ke ruang pemeriksaan.")
        
        self.riwayat_panggilan.append(id_panggilan)

    def tampilkan_antrean(self):
        print("\n=== DAFTAR ANTREAN SAAT INI ===")
        print(f"🔴 URGENT    ({len(self.queue_urgent)} orang) : {', '.join(self.queue_urgent)}")
        print(f"🟡 PRIORITAS ({len(self.queue_prioritas)} orang) : {', '.join(self.queue_prioritas)}")
        print(f"🟢 REGULER   ({len(self.queue_reguler)} orang) : {', '.join(self.queue_reguler)}")
        print("===============================")
        
    def cari_pasien(self, id_antrean):
        if id_antrean in self.database_pasien:
            pasien = self.database_pasien[id_antrean]
            print("\n🔍 DATA PASIEN DITEMUKAN:")
            print(f"   ID Antrean   : {pasien['id']}")
            print(f"   Nama Lengkap : {pasien['nama']}")
            print(f"   Umur         : {pasien['umur']} tahun")
            print(f"   Kategori     : {pasien['kategori']}")
            print(f"   Waktu Daftar : {pasien['waktu_daftar']}")
        else:
            print(f"\n❌ Data dengan ID {id_antrean} tidak ditemukan.")

    def edit_pasien(self, id_antrean):
        """Fitur Update Data & Pindah Queue dengan Generate ID Baru"""
        if id_antrean in self.database_pasien:
            pasien = self.database_pasien[id_antrean]
            print(f"\n✏️ MENGEDIT DATA PASIEN: {pasien['nama']} ({id_antrean})")
            print("   (Tekan Enter jika tidak ingin mengubah data tersebut)")
            
            nama_baru = input("Masukkan Nama Baru     : ")
            umur_baru = input("Masukkan Umur Baru     : ")
            
            # --- 1. Update Nama & Umur ---
            if nama_baru.strip() != "":
                pasien['nama'] = nama_baru
                
            if umur_baru.strip() != "":
                try:
                    pasien['umur'] = int(umur_baru)
                except ValueError:
                    print("⚠️ Umur harus angka! Umur lama tetap dipertahankan.")
            
            # --- 2. Update Kategori, Generate ID Baru, dan Pindah Queue ---
            print(f"\nKategori saat ini: {pasien['kategori']}")
            print("Pilih Kategori Baru:")
            print("1. Urgent\n2. Prioritas\n3. Reguler\n0. Jangan ubah kategori")
            
            pilihan_kat = input("Pilih (0-3): ")
            
            if pilihan_kat in ['1', '2', '3']:
                kategori_lama = pasien['kategori'].lower()
                
                # Tentukan nama kategori baru
                if pilihan_kat == '1': kategori_baru = "Urgent"
                elif pilihan_kat == '2': kategori_baru = "Prioritas"
                else: kategori_baru = "Reguler"
                
                # Jika kategori benar-benar berubah, jalankan algoritma perpindahan
                if kategori_lama != kategori_baru.lower():
                    # a. Hapus ID lama dari Queue yang lama
                    if kategori_lama == 'urgent' and id_antrean in self.queue_urgent:
                        self.queue_urgent.remove(id_antrean)
                    elif kategori_lama == 'prioritas' and id_antrean in self.queue_prioritas:
                        self.queue_prioritas.remove(id_antrean)
                    elif kategori_lama == 'reguler' and id_antrean in self.queue_reguler:
                        self.queue_reguler.remove(id_antrean)
                    
                    # b. Generate ID Baru
                    id_baru = f"{kategori_baru[0].upper()}-{self.counter:03d}"
                    self.counter += 1
                    
                    # c. Pindahkan data di Hash Table ke Key / ID yang baru
                    pasien['id'] = id_baru
                    pasien['kategori'] = kategori_baru
                    self.database_pasien[id_baru] = pasien # Buat key baru dengan data pasien
                    del self.database_pasien[id_antrean]   # Hapus key lama dari Hash Table
                    
                    # d. Masukkan ID Baru ke Queue yang baru
                    kategori_baru_lower = kategori_baru.lower()
                    if kategori_baru_lower == 'urgent':
                        self.queue_urgent.append(id_baru)
                    elif kategori_baru_lower == 'prioritas':
                        self.queue_prioritas.append(id_baru)
                    else:
                        self.queue_reguler.append(id_baru)
                        
                    print(f"🔄 Kategori berhasil diubah dari {kategori_lama.capitalize()} menjadi {kategori_baru}!")
                    print(f"   Nomor Antrean berubah dari {id_antrean} menjadi {id_baru}")
                    
                    # Update variabel id_antrean untuk pesan sukses di bawah
                    id_antrean = id_baru 
                    
            print(f"\n✅ Selesai! Data pasien dengan ID {id_antrean} telah diperbarui!")
        else:
            print(f"\n❌ Data dengan ID {id_antrean} tidak ditemukan di sistem.")

    def batalkan_antrean(self, id_antrean):
        """Fitur Hapus Data (Menghapus pasien dari Queue dan Hash Table)"""
        if id_antrean in self.database_pasien:
            pasien = self.database_pasien[id_antrean]
            kategori_lama = pasien['kategori'].lower()
            nama_pasien = pasien['nama']
            
            # 1. Hapus ID dari Queue yang sesuai
            if kategori_lama == 'urgent' and id_antrean in self.queue_urgent:
                self.queue_urgent.remove(id_antrean)
            elif kategori_lama == 'prioritas' and id_antrean in self.queue_prioritas:
                self.queue_prioritas.remove(id_antrean)
            elif kategori_lama == 'reguler' and id_antrean in self.queue_reguler:
                self.queue_reguler.remove(id_antrean)
                
            # 2. Hapus data lengkap dari Hash Table
            del self.database_pasien[id_antrean]
            
            print(f"\n✅ Berhasil! Antrean atas nama {nama_pasien} ({id_antrean}) telah dibatalkan dan dihapus dari sistem.")
        else:
            print(f"\n❌ Gagal! Data dengan ID {id_antrean} tidak ditemukan di sistem atau sudah dipanggil.")

    def lihat_riwayat(self):
        print("\n=== RIWAYAT PANGGILAN TERBARU ===")
        if not self.riwayat_panggilan:
            print("   Belum ada pasien yang dipanggil.")
            print("=================================")
            return
            
        for i in range(len(self.riwayat_panggilan)-1, -1, -1):
            id_pasien = self.riwayat_panggilan[i]
            nama = self.database_pasien[id_pasien]['nama']
            print(f"   - {id_pasien} ({nama})")
        print("=================================")


# ========================================================
# TAMPILAN MENU INTERAKTIF
# ========================================================
def main():
    rs = SistemAntreanRS()
    
    while True:
        print("\n" + "="*35)
        print("🏥 SISTEM ANTREAN RUMAH SAKIT 🏥")
        print("="*35)
        print("1. Tambah Pasien Baru")
        print("2. Panggil Pasien Selanjutnya")
        print("3. Lihat Daftar Antrean")
        print("4. Cari Data Pasien (Cek Detail)")
        print("5. Lihat Riwayat Panggilan")
        print("6. Edit Data Pasien")
        print("7. Batalkan (hapus) Antrean")
        print("0. Keluar Program")
        print("="*35)
        
        pilihan = input("Pilih menu (0-7): ")
        
        if pilihan == '1':
            print("\n--- Form Tambah Pasien ---")
            nama = input("Masukkan Nama Pasien: ")
            
            # Validasi input umur agar tidak error jika dimasukkan huruf
            while True:
                try:
                    umur = int(input("Masukkan Umur Pasien: "))
                    break
                except ValueError:
                    print("⚠️ Umur harus berupa angka! Silakan coba lagi.")
            
            print("\nPilih Kategori Pasien:")
            print("1. Urgent (Gawat Darurat/Kritis)")
            print("2. Prioritas (Lansia/Ibu Hamil/Disabilitas)")
            print("3. Reguler (Umum)")
            
            kat_pilihan = input("Pilih kategori (1/2/3): ")
            if kat_pilihan == '1':
                kategori = "Urgent"
            elif kat_pilihan == '2':
                kategori = "Prioritas"
            else:
                kategori = "Reguler" # Default jika input salah/3
                
            rs.tambah_antrean(nama, umur, kategori)
            
        elif pilihan == '2':
            rs.panggil_pasien()
            
        elif pilihan == '3':
            rs.tampilkan_antrean()
            
        elif pilihan == '4':
            id_cari = input("\nMasukkan ID Antrean (contoh: R-001, U-002): ")
            rs.cari_pasien(id_cari.upper()) # otomatis diubah ke huruf besar
            
        elif pilihan == '5':
            rs.lihat_riwayat()
            
        elif pilihan == '6':
            id_edit = input("\nMasukkan ID Antrean yang ingin diedit (contoh: R-001): ")
            rs.edit_pasien(id_edit.upper())

        elif pilihan == '7':
            id_batal = input("\nMasukkan ID Antrean yang ingin dibatalkan (contoh: R-001): ")
            rs.batalkan_antrean(id_batal.upper())

        elif pilihan == '0':
            print("\nTerima kasih telah menggunakan Sistem Antrean Rumah Sakit! 🙏")
            break
            
        else:
            print("\n⚠️ Pilihan tidak valid! Silakan pilih angka 0-5.")
            
        # Memberikan sedikit jeda sebelum menu muncul kembali
        time.sleep(1)

if __name__ == "__main__":
    main()
