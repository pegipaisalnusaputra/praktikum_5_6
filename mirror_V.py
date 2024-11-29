import numpy as np
import imageio as img
import matplotlib.pyplot as plt

# gambar
image = img.imread('D:\\gunung.jpg')

# Membuat mirror vertikal
mirrored_image = np.flip(image, axis=0)

# Menampilkan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Mirrored Vertical")
plt.imshow(mirrored_image)

plt.show()