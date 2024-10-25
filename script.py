import cv2
import numpy as np
import matplotlib.pyplot as plt

# Atualize com o path da sua imagem
PATH_IMG = 'imagem.jpeg'
imagem = cv2.imread(PATH_IMG)

# Converter a imagem para escala de cinza
imagem_monocromatiza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

mediana = np.median(imagem_monocromatiza)

_, imagem_threshold = cv2.threshold(imagem_monocromatiza, mediana, 255, cv2.THRESH_BINARY)

imagem_canny = cv2.Canny(imagem_monocromatiza, 100, 200)

# Salvar as imagens processadas
cv2.imwrite('imagem_threshold.jpg', imagem_threshold)
cv2.imwrite('imagem_canny.jpg', imagem_canny)

# Exibir as imagens originais e processadas
plt.figure(figsize=(10, 6))
plt.subplot(1, 3, 1)
plt.title('Imagem Original')
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Thresholding')
plt.imshow(imagem_threshold, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Canny Edge Detection')
plt.imshow(imagem_canny, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
