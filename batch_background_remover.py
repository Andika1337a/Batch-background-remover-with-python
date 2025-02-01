import os
from rembg import remove
from PIL import Image

def find_image_files(directory, extensions=['.jpg', '.jpeg', '.png', '.bmp', '.gif']):
    """
    Mencari file gambar di direktori tertentu berdasarkan ekstensi.
    """
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                image_files.append(os.path.join(root, file))
    return image_files

def remove_background(input_path, output_path):
    """
    Menghapus latar belakang dari gambar dan menyimpan hasilnya.
    """
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print(f"Latar belakang dihapus: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Gagal memproses {input_path}: {e}")

def process_directory(input_dir, output_dir):
    """
    Memproses semua file gambar di direktori input dan menyimpan hasilnya di direktori output.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_files = find_image_files(input_dir)
    if not image_files:
        print("Tidak ada file gambar yang ditemukan di direktori input.")
        return

    for img_path in image_files:
        # Buat nama file output
        img_name = os.path.basename(img_path)
        output_path = os.path.join(output_dir, os.path.splitext(img_name)[0] + "_nobg.png")
        
        # Proses penghapusan latar belakang
        remove_background(img_path, output_path)

# Contoh penggunaan
input_directory = "path/to/input/directory"  # Ganti dengan path direktori input Anda
output_directory = "path/to/output/directory"  # Ganti dengan path direktori output Anda

process_directory(input_directory, output_directory)
