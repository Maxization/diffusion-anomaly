import os
import cv2
import numpy as np

path = 'E:/experiment3/PredictionAnomaly/'
images = os.listdir(path)

for image in images:
  if os.path.isdir(image):
    continue

  result_path = path + 'Heatmap/'
  if not os.path.exists(result_path):
    os.mkdir(result_path)

  if 'diff' in image:
    img = cv2.imread(path + image, 0)
    img = np.flipud(img)
    heatmap = cv2.applyColorMap(img, cv2.COLORMAP_HOT)
    cv2.imwrite(result_path + image, heatmap)
