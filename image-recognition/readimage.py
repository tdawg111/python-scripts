from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#image = Image.open('images/dot.png')
#image = Image.open('images/dotndot.png')
#image = Image.open('images/numbers/0.4.png')
#image = Image.open('images/numbers/y0.4.png')
image = Image.open('images/numbers/y0.5.png')
image_as_array = np.asarray(image)
print(image_as_array)

plt.imshow(image_as_array)
plt.show()
