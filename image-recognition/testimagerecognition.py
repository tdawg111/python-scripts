from PIL import Image
from collections import Counter
import numpy as np

def what_number_is_this(file_path):
    matched_array = []
    load_examples = open('number_array_examples.txt', 'r').read()
    load_examples = load_examples.split('\n')

    image = Image.open(file_path)
    image_as_array = np.array(image)
    image_array_as_list = image_as_array.tolist()

    subject_in_question = str(image_array_as_list)
    
    for each_example in load_examples:
        try:
            if each_example != '':
                split = each_example.split('::')
                current_number = split[0]
                current_pixel_array = split[1]
                
                each_pixel_example = current_pixel_array.split('],')
                each_pixel_in_question = subject_in_question.split('],')

                pixel = 0

                while pixel < len(each_pixel_example):
                    if each_pixel_example[pixel] == each_pixel_in_question[pixel]:
                        matched_array.append(int(current_number))

                    pixel += 1
        except Exception as e:
            print(str(e))
        
    counts = Counter(matched_array)
    print(counts)
    print(counts.most_common(1))

if __name__ == '__main__':
    what_number_is_this('images/test.png')
    
