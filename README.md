# Proxy Formatter HTTP://

`proxy-formatter-http://` adalah alat sederhana yang digunakan untuk memformat daftar proxy agar dimulai dengan `http://` jika belum. Skrip ini membaca daftar proxy dari sebuah file teks, memeriksa setiap baris, dan menambahkan awalan `http://` pada proxy yang tidak memiliki awalan tersebut, kemudian menyimpannya ke file baru dengan nama unik.

## Fitur

- Membaca daftar proxy dari file teks.
- Menambahkan awalan `http://` ke proxy yang belum memiliki awalan `http://` atau `https://`.
- Menyimpan hasilnya ke file teks baru dengan nama unik, misalnya `proxy_siap_pakai1.txt`, `proxy_siap_pakai2.txt`, dan seterusnya.

## Persyaratan

- Python 3.x
- File input dalam format teks (misalnya `proxy.txt`).

## Instalasi

1. Clone repository ini ke komputer Anda:

   ```bash
   git clone https://github.com/Dheryldz/proxy-formatter-http-
   cd (the folder)
   python run.py
   ```
