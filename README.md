# Batch-background-remover-with-python

*pip install rembg pillow*

# Contoh penggunaan
input_directory = "path/to/input/directory"  # Ganti dengan path direktori input Anda
output_directory = "path/to/output/directory"  # Ganti dengan path direktori output Anda

process_directory(input_directory, output_directory)
```

### Fitur yang Ditambahkan:
1. **Pencarian File Gambar**:
   - Skrip akan mencari file gambar dengan ekstensi `.jpg`, `.jpeg`, `.png`, `.bmp`, dan `.gif` di direktori yang ditentukan.
   - Anda bisa menyesuaikan ekstensi yang dicari dengan mengubah parameter `extensions` di fungsi `find_image_files`.

2. **Proses Batch**:
   - Semua file gambar yang ditemukan di direktori input akan diproses satu per satu.
   - Hasilnya akan disimpan di direktori output dengan nama file yang sama, tetapi ditambahkan `_nobg.png` di akhir nama file.

3. **Pembuatan Direktori Output**:
   - Jika direktori output belum ada, skrip akan membuatnya secara otomatis.

### Cara Menggunakan:
1. Simpan skrip di atas ke file Python, misalnya `batch_background_remover.py`.
2. Ganti `input_directory` dan `output_directory` dengan path direktori yang sesuai.
3. Jalankan skrip dengan perintah:
   ```bash
   python batch_background_remover.py
   ```
4. Skrip akan memproses semua file gambar di direktori input dan menyimpan hasilnya di direktori output.

### Contoh Struktur Direktori:
- **Input Directory**:
  ```
  /path/to/input/directory
  ├── image1.jpg
  ├── image2.png
  └── subfolder/image3.jpeg
  ```

- **Output Directory**:
  ```
  /path/to/output/directory
  ├── image1_nobg.png
  ├── image2_nobg.png
  └── subfolder/image3_nobg.png
  ```
