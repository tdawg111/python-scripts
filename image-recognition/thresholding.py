from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from statistics import mean

def threshold(image_array):
    balance_array = []
    new_array = image_array

    for each_row in image_array:
        for each_pixel in each_row:
            average = mean(each_pixel[0:3])
            balance_array.append(average)

    balance = mean(balance_array)
    for each_row in new_array:
        for each_pix in each_row:
            if mean(each_pix[:3]) > balance:
                each_pix[0] = 255
                each_pix[1] = 255
                each_pix[2] = 255
                each_pix[3] = 255
            else:
                each_pix[0] = 0
                each_pix[1] = 0
                each_pix[2] = 0
                each_pix[3] = 255
    return new_array

image1 = Image.open('images/numbers/0.1.png')
image1_as_array = np.array(image1)
image2 = Image.open('images/numbers/y0.4.png')
image2_as_array = np.array(image2)
image3 = Image.open('images/numbers/y0.5.png')
image3_as_array = np.array(image3)
image4 = Image.open('images/sentdex.png')
image4_as_array = np.array(image4)

# comment out the next 4 lines to see the original images
image1_as_array = threshold(image1_as_array)
image2_as_array = threshold(image2_as_array)
image3_as_array = threshold(image3_as_array)
image4_as_array = threshold(image4_as_array)

figure = plt.figure()
figure1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
figure2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
figure3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
figure4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

figure1.imshow(image1_as_array)
figure2.imshow(image2_as_array)
figure3.imshow(image3_as_array)
figure4.imshow(image4_as_array)

plt.show()
