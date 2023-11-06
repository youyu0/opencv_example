from rembg import remove
from PIL import Image
import cv2
import matplotlib.pyplot as plt

from google.colab.patches import cv2_imshow


input_path = 'p.png'
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
plt.imshow(output)
# img = cv2.imread('output.png')
# cv2_imshow(img)
