import os
from PIL import Image

pwd = os.getcwd()
print(pwd)

img_dir = 'assigment-2-images'
file = open('ratings.txt', 'w', encoding='utf-8')
user_question = 'On a scale of 1 to 7, how much do you think the person is happy?'
    
for filename in os.listdir(img_dir):
    f = os.path.join(pwd, img_dir, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        img.show()
        rating = input(user_question)
        file.write(filename)
        file.write(',')
        file.write(rating)
        file.write('\n')

file.close()