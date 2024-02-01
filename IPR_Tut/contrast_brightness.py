from PIL import Image, ImageEnhance

def adjust_brightness(input_path, output_path, factor):
    image = Image.open(input_path)

    enhancer = ImageEnhance.Brightness(image)

    adjusted_image = enhancer.enhance(factor)

    adjusted_image.save(output_path)

adjust_brightness('IPR_Tut/images/demo.jpeg', 'IPR_Tut/images/brightness.jpeg', 0.5)


def adjust_contrast(input_path, output_path, factor):
    image = Image.open(input_path)

    enhancer = ImageEnhance.Contrast(image)

    adjusted_image = enhancer.enhance(factor)

    adjusted_image.save(output_path)

adjust_contrast('IPR_Tut/images/demo.jpeg', 'IPR_Tut/images/contrast.jpeg', 2.0)

