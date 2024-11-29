import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomPlus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y / factor)
            ori_x = int(x / factor)

            imgZoom[y, x] = image[ori_y, ori_x]

    return imgZoom

# Load gambar
image = img.imread('D:\\gunung.jpg')

# Jika gambar memiliki 4 saluran (RGBA), konversi ke RGB
if image.shape[-1] == 4:
    image = image[:, :, :3]

# Zoom memperbesar (skala 2.0)
factor = 2.0
imgZoom = zoomPlus(image, factor)

# Simpan hasil
img.imwrite("D:\\zoom_plus.jpg", imgZoom)

# Menampilkan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Zoom Plus Image")
plt.imshow(imgZoom)

plt.show()
