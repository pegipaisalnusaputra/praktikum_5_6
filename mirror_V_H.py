import numpy as np
import imageio as img
import matplotlib.pyplot as plt

# gambar
image = img.imread('D:\\gunung.jpg')

# Membuat mirror vertikal dan horizontal
mirrored_image = np.flip(np.flip(image, axis=0), axis=1)

# Menampilkan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Mirrored Vertically & Horizontally")
plt.imshow(mirrored_image)

plt.show()
