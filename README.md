# 🔐 Implementasi Algoritma RC4 - Python (From Scratch)

Tugas ini merupakan implementasi algoritma **RC4 (Rivest Cipher 4)**, sebuah *Symmetric Stream Cipher*, yang dibuat tanpa menggunakan library kriptografi eksternal untuk memenuhi kriteria tugas mata kuliah **Keamanan Data**.

## 📝 Deskripsi Proyek
Program ini mendemonstrasikan proses enkripsi dan dekripsi teks menggunakan algoritma RC4. Pengguna dapat memasukkan pesan (*plaintext*) dan kunci rahasia secara bebas, kemudian program akan mengolahnya melalui tahapan matematis RC4 untuk menghasilkan *ciphertext* dalam format Hexadecimal.

### Fitur Utama:
- **Key Scheduling Algorithm (KSA):** Inisialisasi dan pengacakan S-Box 256-bit.
- **Pseudo-Random Generation Algorithm (PRGA):** Pembangkitan aliran kunci (*keystream*).
- **XOR Operation:** Proses utama pengubahan data menjadi kode rahasia.

---

## 🚀 Cara Menjalankan
Pastikan Anda sudah menginstal **Python 3.x** di perangkat Anda.

1. Clone repositori ini atau download file `pipio.py`.
2. Buka terminal atau command prompt di direktori file tersebut.
3. Jalankan perintah berikut:
   ```bash
   python pipio.py
