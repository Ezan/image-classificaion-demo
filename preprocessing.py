import os
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize


def cleanup():
    target = []
    images = []
    flat_data = []

    DATADIR = 'data/images'
    CATEGORIES = ["cocci_bacteria", "bacilli_bacteria", "spirilla_bacteria", "vibrios_bacteria",
                  "spirochaetes_bacteria"]

    # preprocess
    # resize
    # flatten
    for category in CATEGORIES:
        # print(category)
        class_num = CATEGORIES.index(category)
        path = os.path.join(DATADIR, category)
        for img in os.listdir(path):
            img_array = imread(os.path.join(path, img))
            img_resized = resize(img_array, (150, 150, 3))  # Normalizes the value form 0 to 1
            flat_data.append(img_resized.flatten())
            images.append(img_resized)
            target.append((class_num))
            # print(img_array.shape)
            # plt.imshow(img_array)
            # plt.show()
    flat_data = np.array(flat_data)
    target = np.array((target))
    images = np.array(images)
    return flat_data, target

# print(len(flat_data))
# print(target)

# unique, count = np.unique(target, return_counts=True)
# plt.bar(CATEGORIES, count)
# plt.show()

# split data into train and test
