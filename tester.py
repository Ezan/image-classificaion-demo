# Testing a brand new Image
from skimage.io import imread
from skimage.transform import resize
import matplotlib.pyplot as plt
from predicter import getModel
import numpy as np

flat_data = []
CATEGORIES = ["cocci_bacteria", "bacilli_bacteria", "spirilla_bacteria", "vibrios_bacteria",
              "spirochaetes_bacteria"]
url = input('Enter you rURL')
img = imread(url)
img_resized = resize(img, (150, 150, 3))
flat_data.append(img_resized.flatten())
flat_data = np.array(flat_data)
print(img.shape)
plt.imshow(img_resized)
model = getModel()
y_out = model.predict(flat_data)
y_out = CATEGORIES[y_out[0]]
plt.show()
print(f' PREDICTED OUTPUT: {y_out}')
