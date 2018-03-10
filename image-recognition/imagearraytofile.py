from PIL import Image
import numpy as np

def read_png_to_file():
    number_array_examples = open('number_array_examples.txt', 'a')

    for each_number in range(10):
        for sub_number in range(1, 10):
            #print(str(each_number) + '.' + str(sub_number))
            image_path = 'images/numbers/' + str(each_number) + '.' + str(sub_number) + '.png'
            image = Image.open(image_path)
            image_as_array = np.array(image)
            image_array_as_list = str(image_as_array.tolist())

            #print(image_array_as_list)
            line_to_output = str(each_number) + '::' + image_array_as_list + '\n'
            number_array_examples.write(line_to_output)

if __name__ == '__main__':
    read_png_to_file()
