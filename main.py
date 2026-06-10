import time

class SistemAntreanRS:
    def __init__(self):
        # 1. Konsep QUEUE (FIFO) menggunakan List 
        # Pengembangan ide: membagi queue menjadi 3 level prioritas
        self.queue_urgent = []
        self.queue_prioritas = []
        self.queue_reguler = []
        
        # 2. Konsep HASH TABLE (Dictionary)
        # Menyimpan detail pasien untuk pencarian cepat menggunakan ID Antrean
        self.database_pasien = {}
        
        # 3. Konsep STACK (LIFO) menggunakan List
        # Menyimpan riwayat panggilan agar bisa dilihat dari yang terbaru
        self.riwayat_panggilan = []
        
        self.counter = 1 # Untuk mengenerate nomor antrean
        
    def tambah_antrean(self, nama, umur, kategori):
        """Fitur Tambah Data"""
        # Generate ID unik berdasarkan kategori
        id_antrean = f"{kategori[0].upper()}-{self.counter:03d}"
        self.counter += 1
        
        # Data yang dimasukkan ke Hash Table
        pasien_baru = {
            'id': id_antrean,
            'nama': nama,
            'umur': umur,
            'kategori': kategori,
            'waktu_daftar': time.strftime("%H:%M:%S")
        }
        self.database_pasien[id_antrean] = pasien_baru
        
        # Memasukkan ID ke Queue sesuai kategori
        kategori_lower = kategori.lower()
        if kategori_lower == 'urgent': # Misalnya: Gawat Darurat
            self.queue_urgent.append(id_antrean)
        elif kategori_lower == 'prioritas': # Misalnya: Lansia, Ibu Hamil
            self.queue_prioritas.append(id_antrean)
        else: # Misalnya: Pasien Umum
            self.queue_reguler.append(id_antrean)
            
        print(f"✅ Berhasil! Pasien '{nama}' mendapat ID Antrean: {id_antrean}")

    def panggil_pasien(self):
        """Fitur Hapus Data dari Antrean (Dequeue) & Masuk ke Stack"""
        id_panggilan = None
        
        # Cek dari prioritas tertinggi terlebih dahulu
        if len(self.queue_urgent) > 0:
            id_panggilan = self.queue_urgent.pop(0)
        elif len(self.queue_prioritas) > 0:
            id_panggilan = self.queue_prioritas.pop(0)
        elif len(self.queue_reguler) > 0:
            id_panggilan = self.queue_reguler.pop(0)
        else:
            print("📭 Tidak ada antrean saat ini.")
            return
            
        # Mengambil data lengkap dari Hash Table
        pasien = self.database_pasien[id_panggilan]
        print(f"\n📢 PANGGILAN PASIEN:")
        print(f"   Mohon perhatian, pasien dengan ID {pasien['id']} atas nama {pasien['nama']}")
        print(f"   Silakan menuju ke ruang pemeriksaan.")
        
        # Push ke Stack untuk riwayat
        self.riwayat_panggilan.append(id_panggilan)

    def tampilkan_antrean(self):
        """Fitur Tampilkan Data (Traversal)"""
        print("\n=== DAFTAR ANTREAN SAAT INI ===")
        print(f"🔴 URGENT    ({len(self.queue_urgent)} orang) : {', '.join(self.queue_urgent)}")
        print(f"🟡 PRIORITAS ({len(self.queue_prioritas)} orang) : {', '.join(self.queue_prioritas)}")
        print(f"🟢 REGULER   ({len(self.queue_reguler)} orang) : {', '.join(self.queue_reguler)}")
        print("===============================")
        
    def cari_pasien(self, id_antrean):
        """Fitur Cari Data dengan efisiensi O(1) menggunakan Hash Table"""
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

    def lihat_riwayat(self):
        """Pengembangan Fitur: Menampilkan Stack dari atas (LIFO)"""
        print("\n=== RIWAYAT PANGGILAN TERBARU ===")
        if not self.riwayat_panggilan:
            print("   Belum ada pasien yang dipanggil.")
            return
            
        # Looping list secara mundur untuk mensimulasikan pembacaan Stack
        for i in range(len(self.riwayat_panggilan)-1, -1, -1):
            id_pasien = self.riwayat_panggilan[i]
            nama = self.database_pasien[id_pasien]['nama']
            print(f"   - {id_pasien} ({nama})")
        print("=================================")


# ========================================================
# BAGIAN DEMONSTRASI PROGRAM (Simulasi Sesuai Ketentuan UAS)
# ========================================================
if __name__ == "__main__":
    rs = SistemAntreanRS()
    
    print("\n--- 1. DEMO PENAMBAHAN DATA ---")
    rs.tambah_antrean("Bapak Andi", 35, "Reguler")
    rs.tambah_antrean("Kakek Budi", 70, "Prioritas")
    rs.tambah_antrean("Ibu Citra (Pendarahan)", 28, "Urgent")
    rs.tambah_antrean("Adik Dewi", 12, "Reguler")
    
    print("\n--- 2. DEMO TAMPILKAN ANTREAN ---")
    rs.tampilkan_antrean()
    
    print("\n--- 3. DEMO PANGGILAN (Mengutamakan prioritas tertinggi) ---")
    rs.panggil_pasien() # Akan memanggil Urgent (Citra) duluan
    rs.panggil_pasien() # Kemudian memanggil Prioritas (Budi)
    
    print("\n--- 4. DEMO ANTREAN SETELAH DIPANGGIL ---")
    rs.tampilkan_antrean()
    
    print("\n--- 5. DEMO PENCARIAN DATA (Hash Table) ---")
    rs.cari_pasien("R-001") # Mencari Bapak Andi
    
    print("\n--- 6. DEMO RIWAYAT PANGGILAN (Stack) ---")
    rs.lihat_riwayat()
