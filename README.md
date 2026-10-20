# SecureInventoryApp - DevSecOps Pipeline Project

## 1. Nama Aplikasi & Fungsinya
**SecureInventoryApp** adalah aplikasi modular berbasis Python untuk mengelola inventaris barang dan autentikasi pengguna secara aman. Aplikasi ini memiliki fitur:
- Registrasi dan verifikasi pengguna menggunakan algoritma hashing SHA-256 dengan *salt*.
- Pencatatan stok barang, pembaruan kuantitas, dan kalkulasi nilai total inventaris.
- Sanitasi input pengguna dan kalkulasi diskon dengan validasi batas keamanan.

## 2. Bahasa & Framework yang Digunakan
- **Bahasa Pemrograman:** Python 3.11
- **Testing Framework:** `unittest` & `pytest`
- **SAST Tool:** Bandit (Python AST Security Scanner) / SonarQube
- **CI/CD Platform:** GitHub Actions (`ubuntu-latest`)

## 3. Cara Menjalankan Aplikasi & Unit Test
1. Clone repository ini:
   ```bash
   git clone [https://github.com/username-anda/devsecops-p5-nim.git](https://github.com/adityadwiprs190/devsecops-p5-0110223125-adityadwiprasetyo.git)
   cd devsecops-p5-0110223125-adityadwiprasetyo
