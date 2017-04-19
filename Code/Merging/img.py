import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pylab

img1 = cv2.imread('10.jpg')
img2 = cv2.imread('output_10.jpg')
img3 = cv2.imread('10_before.jpg')
img4 = cv2.imread('10_after.jpg')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)


plt.subplot(221), plt.imshow(img1),plt.title("Original Image")
plt.subplot(222), plt.imshow(img2),plt.title("Detecting Line Segments")
plt.subplot(223), plt.imshow(img3),plt.title("Image with Line Segments")
plt.subplot(224), plt.imshow(img4),plt.title("After Merging and Filtering")

plt.tight_layout()
pylab.savefig('merge.eps', format='eps', dpi=150, bbox_inches='tight')
