import random
import string
import os
import io
from captcha.image import ImageCaptcha, random_color

def generate_captcha():
    letters = string.ascii_letters
    digits = string.digits
    random_str = ''.join([random.choice(digits+letters) for j in range(4)])
    width, height = 170, 80

    generator = ImageCaptcha(width=width, height=height)
    img = generator.create_captcha_image(chars=random_str, color=random_color(1, 255), background=random_color(1, 255))
    
    for i in range(1, 3):
        generator.create_noise_dots(img, random_color(1, 255))
        generator.create_noise_curve(img, random_color(1, 255))

    img.show()
    
    fileName = "saveImg"
    if not os.path.exists(fileName):
        os.mkdir(fileName)
    img.save("%s/%s.png" % (fileName, random_str))
    
    buffer = io.BytesIO()
    img.save(buffer, 'PNG')
    image_data = buffer.getvalue()
    buffer.close()

    # return random_str, image_data

generate_captcha()