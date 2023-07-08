# Author Ryan Arya Pramudya
# GitHub https://github.com/ryanaryap
import re

# Membaca daftar URL dari file teks
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    # Membersihkan URL dari karakter newline dan spasi tambahan
    urls = [url.strip() for url in urls]
    return urls

# Mengambil URL depan dan menambahkan protokol
def extract_domain(url):
    pattern = r"(https?://)([\w.-]+)"
    match = re.match(pattern, url)
    if match:
        protocol = match.group(1)
        domain = match.group(2)
        return protocol + domain
    else:
        return None

# Meminta pengguna untuk memasukkan path file
file_path = input("Masukkan path file teks: ")

# Membaca daftar URL dari file
urls = read_urls_from_file(file_path)

# Ekstraksi URL depan dan menambahkan protokol
output_lines = []
for url in urls:
    domain = extract_domain(url)
    if domain:
        output_lines.append(domain)
    else:
        output_lines.append("URL tidak valid: " + url)

# Menyimpan output ke dalam file result.txt
output_file_path = "result.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write('\n'.join(output_lines))

print("Output telah disimpan dalam file", output_file_path)
