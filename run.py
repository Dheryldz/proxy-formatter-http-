import os

# Nama file input dan output dasar
nama_file_input = 'proxy.txt'
nama_file_output_basename = 'proxy_siap_pakai.txt'

# Membaca file proxy.txt
with open(nama_file_input, 'r') as file:
    baris_proxy = file.readlines()

# Memproses setiap baris agar dimulai dengan 'http://'
baris_rapi = []
for baris in baris_proxy:
    baris = baris.strip()  # Menghapus spasi atau karakter newline di awal/akhir
    if not baris.startswith('http://') and not baris.startswith('https://'):
        baris = f'http://{baris}'
    baris_rapi.append(baris)

# Menentukan nama file output yang tidak akan menimpa file yang ada
counter = 1
while True:
    nama_file_output = f"{nama_file_output_basename}{counter}.txt"
    if not os.path.exists(nama_file_output):
        break
    counter += 1

# Menulis ke file yang baru
with open(nama_file_output, 'w') as file:
    file.write('\n'.join(baris_rapi))

print(f"File berhasil dirapikan dan disimpan sebagai '{nama_file_output}'.")
