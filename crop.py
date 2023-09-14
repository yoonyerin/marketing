from PIL import Image, PngImagePlugin

import numpy as np

def pil_resize_image_center_crop(image, size):
    image_height, image_width, _ = image.shape
    width, height = size

    width_target_ratio = width * 1.0 / image_width
    height_target_ratio = height * 1.0 / image_height
    ratio = max(width_target_ratio, height_target_ratio)

    pil_image = Image.fromarray(image)
    resized_pil_image = pil_image.resize((int(image_width * ratio), int(image_height * ratio)))
    resized_pil_image_width, resized_pil_image_height = resized_pil_image.size
    x1 = ((resized_pil_image_width - width) / 2)
    y1 = ((resized_pil_image_height - height) / 2)
    x2 = x1 + width
    y2 = y1 + height
    cropped_pil_image = resized_pil_image.crop((x1, y1, x2, y2))

    return np.array(cropped_pil_image)

image="./src3.jpg"
image=Image.open(image)
image=np.array(image)
image=pil_resize_image_center_crop(image, (1920, 1280))
image=Image.fromarray(image)
image.save("./new_src3.jpg")