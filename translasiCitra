import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def translateImage(image, tx, ty):
    # Mendapatkan ukuran gambar
    height, width = image.shape[:2]
    
    # Membuat gambar kosong dengan ukuran baru (untuk translasi)
    translated_image = np.zeros_like(image)
    
    # Melakukan translasi
    for y in range(height):
        for x in range(width):
            # Koordinat baru
            new_x = x + tx
            new_y = y + ty
            
            # Memastikan koordinat baru tidak keluar dari batas gambar
            if 0 <= new_x < width and 0 <= new_y < height:
                translated_image[new_y, new_x] = image[y, x]
    
    return translated_image

# Load gambar
image = img.imread('D:\\gunung.jpg')

# Jika gambar memiliki 4 saluran (RGBA), konversi ke RGB
if image.shape[-1] == 4:
    image = image[:, :, :3]

# Translasi gambar (tx = 50 piksel ke kanan, ty = 30 piksel ke bawah)
tx, ty = 50, 30
translated_image = translateImage(image, tx, ty)

# Menampilkan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title(f"Translated Image (tx={tx}, ty={ty})")
plt.imshow(translated_image)

plt.show()
