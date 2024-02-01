from PIL import Image


def resize_image(input_path, output_path , new_width, new_height):
    image = Image.open(input_path)

    resize_image = image.resize((new_width, new_height))

    resize_image.save(output_path)

    print(f"Resize image saved as {output_path}")


resize_image('IPR_Tut/images/demo.jpeg', 'IPR_Tut/images/resizeImage.jpeg', 400, 300)

def crop_image(input_path, output_path, crop_box):
    image = Image.open(input_path)

    crop_image = image.crop(crop_box)

    crop_image.save(output_path)

    print(f"Crop image saved as {output_path}")

new_size = (200, 850, 2800, 2200)
crop_image('IPR_Tut/images/demo.jpeg', 'IPR_Tut/images/cropImage.jpeg', new_size)