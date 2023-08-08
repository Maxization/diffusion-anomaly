import os
from PIL import Image
import numpy as np

path = '../../kaggle_3m/'
patients = os.listdir(path)

for patient in patients:
  patient_folder = path + patient + '/'

  if not os.path.exists(patient_folder + 'diseased'):
    os.makedirs(patient_folder + 'diseased')

  if not os.path.exists(patient_folder + 'healthy'):
    os.makedirs(patient_folder + 'healthy')

  images = os.listdir(patient_folder)

  for image in images:
    if image == 'diseased' or image == 'healthy' or '_mask' in image:
      continue

    mask = image[:-4] + '_mask.tif'
    print(mask)

    img = Image.open(patient_folder + mask)
    arr = np.array(img)

    dest = 'diseased/'
    if np.all(arr ==0):
      dest = 'healthy/'

    #os.replace(patient_folder + mask, patient_folder + dest + mask)
    os.replace(patient_folder + image, patient_folder + dest + image)
    os.remove(patient_folder + mask)
    print('Moved!')
