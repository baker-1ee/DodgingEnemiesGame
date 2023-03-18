from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    with Image.open(input_image_path) as image:
        image.thumbnail(size)
        image.save(output_image_path)
