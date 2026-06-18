# AKRAB

## 1. Deskripsi Aplikasi

### 1.1 Deskripsi dan Fungsi Aplikasi

**AKRAB (Aplikasi Karyawan Rekam Administrasi Berkelanjutan)** adalah sebuah sistem manajemen data karyawan yang dirancang untuk memfasilitasi operasi pengelolaan data karyawan secara efisien dan terintegrasi. AKRAB menyediakan fungsi lengkap untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada data karyawan perusahaan dengan antarmuka yang user-friendly dan data yang tersimpan secara persisten.

**Fungsi Utama AKRAB:**
- **Create (Buat)**: Menambahkan data karyawan baru ke dalam sistem
- **Read (Baca)**: Menampilkan dan melihat detail data karyawan dari database
- **Update (Ubah)**: Memperbarui informasi data karyawan yang sudah ada
- **Delete (Hapus)**: Menghapus data karyawan dari sistem
- **Search (Cari)**: Mencari karyawan berdasarkan nama, departemen, atau posisi
- **Manage (Kelola)**: Mengelola status karyawan (aktif/tidak aktif)

### 1.2 Alasan Pembuatan Aplikasi

AKRAB dibuat untuk memenuhi **Syarat Kelulusan Capstone Project Module 1 - Purwadhika Digital Technology School**. Tujuan dari pembuatan AKRAB adalah:

1. Mengaplikasikan konsep CRUD yang telah dipelajari dalam modul
2. Mendemonstrasikan kemampuan dalam mengimplementasikan logika program menggunakan Python
3. Menunjukkan penguasaan dalam pengelolaan data menggunakan struktur file yang tepat (CSV)
4. Membangun sistem yang dapat langsung digunakan dalam konteks bisnis nyata

### 1.3 User/Stakeholder

**Pengguna Utama Aplikasi:**
- **HR/Human Resource Manager**: Mengelola data karyawan, mutasi, dan administrasi SDM
- **Manager/Supervisor**: Melihat dan memantau data tim karyawan mereka
- **Admin Departemen**: Mengelola data karyawan per departemen
- **Karyawan**: Melihat data pribadi dan informasi karyawan lainnya (dengan akses terbatas)
- **Finance Team**: Mengakses data gaji dan informasi finansial karyawan untuk keperluan payroll

### 1.4 Tujuan Pembuatan Aplikasi bagi Pengguna (Karyawan Kantor)

AKRAB dirancang dengan tujuan untuk:

1. **Meningkatkan Efisiensi Operasional**: Mengurangi waktu yang dibutuhkan untuk mengelola data karyawan secara manual
2. **Mengurangi Kesalahan Data**: Meminimalkan human error dalam pencatatan data karyawan
3. **Aksesibilitas Data**: Memberikan akses mudah dan cepat terhadap informasi karyawan yang diperlukan
4. **Sentralisasi Data**: Menyimpan semua data karyawan dalam satu tempat terpusat dan terorganisir
5. **Mendukung Pengambilan Keputusan**: Menyediakan informasi yang akurat untuk mendukung pengambilan keputusan HR
6. **Compliance & Record Keeping**: Memastikan pencatatan data karyawan sesuai dengan standar perusahaan

### 1.5 Penjelasan Fitur

#### **Fitur 1: Menampilkan Semua Karyawan**
- Menampilkan daftar lengkap semua karyawan yang terdaftar dalam sistem
- Menampilkan informasi: ID, nama, departemen, posisi, dan status aktif
- Memudahkan user untuk melihat overview karyawan secara keseluruhan

#### **Fitur 2: Melihat Detail Karyawan**
- Menampilkan informasi lengkap karyawan berdasarkan ID unik
- Informasi meliputi: nama lengkap, email, telepon, departemen, posisi, gaji, tanggal masuk kerja, dan status
- Memungkinkan user untuk mendapatkan informasi detail tentang seorang karyawan

#### **Fitur 3: Menambahkan Karyawan Baru**
- Membuat record karyawan baru dengan mengisi form data lengkap
- Input data mencakup: nama depan, nama belakang, email, telepon, departemen, posisi, gaji, tanggal masuk kerja, dan status aktif
- Sistem otomatis memberikan ID unik untuk setiap karyawan baru

#### **Fitur 4: Mengubah Data Karyawan**
- Memperbarui informasi karyawan yang sudah ada
- Memungkinkan perubahan pada setiap field data karyawan
- Jika input kosong saat edit, nilai lama akan dipertahankan

#### **Fitur 5: Menghapus Karyawan**
- Menghapus record karyawan dari sistem
- Menghilangkan data dari database
- Operasi ini bersifat permanen dan memerlukan konfirmasi

#### **Fitur 6: Mencari Karyawan**
- Mencari karyawan berdasarkan kriteria: nama, departemen, atau posisi
- Menampilkan hasil pencarian yang sesuai dengan keyword yang dimasukkan
- Memudahkan user menemukan data karyawan spesifik dengan cepat

---

## 2. Flowchart Per Fitur

### **Fitur 1: Menampilkan Semua Karyawan**

```
┌─────────────────────────────────────┐
│   Mulai - Tampilkan Semua Karyawan  │
└────────────┬────────────────────────┘
             │
             ▼
    ┌────────────────────┐
    │ Baca file CSV      │
    │ (employees.csv)    │
    └────────┬───────────┘
             │
             ▼
    ┌────────────────────┐
    │ Apakah file ada?   │
    └────┬───────────┬───┘
         │ Ya        │ Tidak
         ▼           ▼
    ┌────────┐  ┌──────────────────┐
    │ Tampil │  │ Buat file kosong  │
    │ Data   │  │ dan tampilkan     │
    │        │  │ "Belum ada data"  │
    └────┬───┘  └──────┬───────────┘
         │              │
         └──────┬───────┘
                ▼
         ┌─────────────────┐
         │ Selesai - Kembali│
         │ ke Menu Utama    │
         └─────────────────┘
```

### **Fitur 2: Melihat Detail Karyawan**

```
┌──────────────────────────────────────┐
│   Mulai - Lihat Detail Karyawan      │
└────────────┬─────────────────────────┘
             │
             ▼
    ┌──────────────────────┐
    │ Input ID Karyawan    │
    └────────┬─────────────┘
             │
             ▼
    ┌────────────────────┐
    │ Cari di CSV        │
    │ berdasarkan ID     │
    └────┬───────────┬───┘
         │ Ditemukan │ Tidak Ditemukan
         ▼           ▼
    ┌────────┐  ┌──────────────────┐
    │ Tampil │  │ Tampilkan pesan   │
    │ Detail │  │ "Data tidak       │
    │        │  │ ditemukan"        │
    └────┬───┘  └──────┬───────────┘
         │              │
         └──────┬───────┘
                ▼
         ┌─────────────────┐
         │ Selesai - Kembali│
         │ ke Menu Utama    │
         └─────────────────┘
```

### **Fitur 3: Menambahkan Karyawan Baru**

```
┌──────────────────────────────────────┐
│   Mulai - Tambah Karyawan Baru       │
└────────────┬─────────────────────────┘
             │
             ▼
    ┌──────────────────────┐
    │ Input Data Karyawan: │
    │ - Nama Depan         │
    │ - Nama Belakang      │
    │ - Email              │
    │ - Telepon            │
    │ - Departemen         │
    │ - Posisi             │
    │ - Gaji               │
    │ - Tanggal Masuk      │
    │ - Status Aktif       │
    └────────┬─────────────┘
             │
             ▼
    ┌────────────────────┐
    │ Validasi Data      │
    │ (format, tipe)     │
    └────┬───────────┬───┘
         │ Valid     │ Tidak Valid
         ▼           ▼
    ┌────────┐  ┌──────────────────┐
    │ Generate│  │ Tampilkan error  │
    │ ID baru │  │ dan minta input  │
    │         │  │ ulang            │
    └────┬───┘  └──────┬───────────┘
         │              │
         └──────┬───────┘
                ▼
    ┌──────────────────────┐
    │ Tambah ke CSV        │
    │ (append data)        │
    └────────┬─────────────┘
             │
             ▼
    ┌──────────────────────┐
    │ Konfirmasi Sukses    │
    │ "Karyawan berhasil   │
    │ ditambahkan"         │
    └────────┬─────────────┘
             │
             ▼
         ┌─────────────────┐
         │ Selesai - Kembali│
         │ ke Menu Utama    │
         └─────────────────┘
```

### **Fitur 4: Mengubah Data Karyawan**

```
┌──────────────────────────────────────┐
│   Mulai - Ubah Data Karyawan         │
└────────────┬─────────────────────────┘
             │
             ▼
    ┌──────────────────────┐
    │ Input ID Karyawan    │
    └────────┬─────────────┘
             │
             ▼
    ┌────────────────────┐
    │ Cari di CSV        │
    │ berdasarkan ID     │
    └────┬───────────┬───┘
         │ Ditemukan │ Tidak Ditemukan
         ▼           ▼
    ┌─────────┐  ┌──────────────────┐
    │ Tampil  │  │ Tampilkan pesan   │
    │ Data    │  │ "Data tidak       │
    │ Lama    │  │ ditemukan"        │
    └────┬────┘  └──────┬───────────┘
         │               │
         └───────┬───────┘
                 ▼
    ┌──────────────────────┐
    │ Input Data Baru      │
    │ (atau kosongkan      │
    │ jika tidak diubah)   │
    └────────┬─────────────┘
             │
             ▼
    ┌────────────────────┐
    │ Validasi Data      │
    └────┬───────────┬───┘
         │ Valid     │ Tidak Valid
         ▼           ▼
    ┌─────────┐  ┌──────────────┐
    │ Update  │  │ Minta input  │
    │ di CSV  │  │ ulang        │
    └────┬────┘  └──────┬──────┘
         │               │
         └───────┬───────┘
                 ▼
    ┌──────────────────────┐
    │ Konfirmasi Sukses    │
    │ "Data berhasil       │
    │ diperbarui"          │
    └────────┬─────────────┘
             │
             ▼
         ┌─────────────────┐
         │ Selesai - Kembali│
         │ ke Menu Utama    │
         └─────────────────┘
```

### **Fitur 5: Menghapus Karyawan**

```
┌──────────────────────────────────────┐
│   Mulai - Hapus Karyawan             │
└────────────┬─────────────────────────┘
             │
             ▼
    ┌──────────────────────┐
    │ Input ID Karyawan    │
    └────────┬─────────────┘
             │
             ▼
    ┌────────────────────┐
    │ Cari di CSV        │
    │ berdasarkan ID     │
    └────┬───────────┬───┘
         │ Ditemukan │ Tidak Ditemukan
         ▼           ▼
    ┌─────────┐  ┌──────────────────┐
    │ Tampil  │  │ Tampilkan pesan   │
    │ Data    │  │ "Data tidak       │
    │         │  │ ditemukan"        │
    └────┬────┘  └──────┬───────────┘
         │               │
         └───────┬───────┘
                 ▼
    ┌──────────────────────┐
    │ Minta Konfirmasi     │
    │ Hapus? (Y/N)         │
    └────┬───────────┬─────┘
         │ Y (Ya)    │ N (Tidak)
         ▼           ▼
    ┌─────────┐  ┌──────────────┐
    │ Hapus   │  │ Batalkan     │
    │ dari    │  │ penghapusan  │
    │ CSV     │  │              │
    └────┬────┘  └──────┬──────┘
         │               │
         └───────┬───────┘
                 ▼
    ┌──────────────────────┐
    │ Konfirmasi Sukses    │
    │ "Data berhasil       │
    │ dihapus"             │
    └────────┬─────────────┘
             │
             ▼
         ┌─────────────────┐
         │ Selesai - Kembali│
         │ ke Menu Utama    │
         └─────────────────┘
```

### **Fitur 6: Mencari Karyawan**

```
┌──────────────────────────────────────┐
│   Mulai - Cari Karyawan              │
└────────────┬─────────────────────────┘
             │
             ▼
    ┌──────────────────────┐
    │ Pilih Kriteria:      │
    │ 1. Nama              │
    │ 2. Departemen        │
    │ 3. Posisi            │
    └────────┬─────────────┘
             │
             ▼
    ┌──────────────────────┐
    │ Input Keyword        │
    │ Pencarian            │
    └────────┬─────────────┘
             │
             ▼
    ┌────────────────────┐
    │ Cari di CSV        │
    │ sesuai kriteria    │
    └────┬───────────┬───┘
         │ Ditemukan │ Tidak Ditemukan
         ▼           ▼
    ┌──────────┐ ┌──────────────────┐
    │ Tampil   │ │ Tampilkan pesan   │
    │ Hasil    │ │ "Tidak ada hasil  │
    │ Pencarian│ │ pencarian"        │
    └────┬─────┘ └──────┬───────────┘
         │               │
         └───────┬───────┘
                 ▼
         ┌─────────────────┐
         │ Selesai - Kembali│
         │ ke Menu Utama    │
         └─────────────────┘
```

---

### 2.1 Minimum Requirements

**Persyaratan Sistem Minimum:**

| Aspek | Requirement |
|-------|-------------|
| **Sistem Operasi** | Windows, Linux, atau macOS |
| **Python** | Versi 3.7 atau lebih baru |
| **Memory (RAM)** | Minimum 512 MB |
| **Storage** | Minimum 100 MB untuk aplikasi dan data |
| **Dependensi** | Modul standar Python (`csv`, `os`, `datetime`) - Tidak diperlukan instalasi tambahan |

**Persyaratan Fungsional:**
- Dapat membaca dan menulis file CSV
- Dapat melakukan operasi CRUD lengkap
- Dapat melakukan pencarian data
- Dapat memberikan feedback/pesan kepada pengguna
- Dapat mengelola ID unik untuk setiap karyawan

---

### 2.2 Limitasi Aplikasi

**Batasan Teknis:**
1. **Single User**: AKRAB hanya mendukung satu pengguna pada saat yang bersamaan. Tidak ada fitur multi-user atau locking mekanisme.
2. **Data Storage**: Menggunakan file CSV lokal - tidak cocok untuk dataset sangat besar (>100,000 records)
3. **Keamanan Data**: Tidak ada enkripsi data dan tidak ada sistem autentikasi/login
4. **Validasi Email**: Validasi email hanya basic, tidak melakukan verifikasi domain
5. **Concurrent Access**: Jika multiple user mengakses file CSV secara bersamaan, dapat terjadi data conflict

**Batasan Fungsional:**
1. Tidak ada backup otomatis data
2. Tidak ada history/audit trail untuk tracking perubahan data
3. Tidak ada fitur export ke format lain (Excel, PDF, dll)
4. Tidak ada fitur role-based access control (RBAC)
5. Tidak ada soft delete - penghapusan bersifat permanent
6. Tidak ada fitur reporting atau analytics
7. Tidak ada image/file attachment untuk profil karyawan
8. Tidak ada notifikasi atau reminder system

**Batasan User Experience:**
1. Interface berbasis command-line (CLI) - kurang user-friendly untuk user non-teknis
2. Tidak ada GUI (Graphical User Interface)
3. Tidak ada real-time search atau filter
4. Tidak ada pagination di list view
5. Error message terkadang kurang informatif

---

### 2.3 Pengembangan Berikutnya

**Pengembangan Tahap 2 - Web-Based Interface:**
- Mengembangkan web interface menggunakan Flask/Django
- Implementasi responsive design untuk mobile compatibility
- Dashboard dengan statistik karyawan

**Pengembangan Tahap 3 - Database Migration:**
- Migrasi dari CSV ke database relasional (PostgreSQL/MySQL)
- Implementasi ORM (SQLAlchemy)
- Backup dan recovery system

**Pengembangan Tahap 4 - Security & Authentication:**
- Sistem login dan autentikasi user
- Role-based access control (Admin, Manager, HR, Employee)
- Enkripsi password dan sensitive data
- Audit trail untuk tracking semua perubahan

**Pengembangan Tahap 5 - Advanced Features:**
- Search dan filtering yang lebih powerful
- Export data ke Excel dan PDF
- Fitur import data dari file eksternal
- Report generation (laporan gaji, kehadiran, dll)
- Integration dengan sistem HR lainnya

**Pengembangan Tahap 6 - Mobile App:**
- Develop mobile application (iOS/Android)
- Offline mode capability
- Push notification untuk update penting

---

## 3. Credits

**Development:**
- **Firman Christian**: Peserta Capstone Project Module 1 Purwadhika Digital Technology School

**Built With:**
- **Python 3.x** - Programming Language
- **CSV Module** - Data Storage
- **OS & DateTime Module** - System Operations

**Institusi:**
- **Purwadhika Digital Technology School** - Pusat Pelatihan Profesional

**Supervisor/Mentor:**
- Median Hardiv Nugraha

---

## 4. License

AKRAB dibuat sebagai bagian dari Capstone Project Purwadhika Digital Technology School. Diizinkan untuk digunakan untuk keperluan pendidikan dan pembelajaran.

---

## 5. Catatan Penting

- File `employees.csv` akan otomatis dibuat jika belum ada
- Semua data disimpan dalam file CSV lokal
- Jika input kosong saat edit, nilai lama akan dipertahankan
- Nilai `salary` harus berupa angka valid
- Tanggal masuk harus menggunakan format `YYYY-MM-DD`
- Penghapusan data bersifat permanen dan tidak dapat di-undo

---
