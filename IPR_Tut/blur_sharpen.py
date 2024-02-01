from PIL import Image, ImageFilter

def blur_image(input_path, output_path, radius):
    
    image = Image.open(input_path)

    blured_image = image.filter(ImageFilter.GaussianBlur(radius=radius))

    blured_image.save(output_path)

blur_image('IPR_Tut/images/demo.jpeg', 'IPR_Tut/images/blur.jpeg', 4)

def sharpen_image(input_path, output_path, factor):
    
    image = Image.open(input_path)

    sharpened_image = image.filter(ImageFilter.UnsharpMask(radius = 2, percent = factor, threshold = 1))

    sharpened_image.save(output_path)

sharpen_image('IPR_Tut/images/demo.jpeg', 'IPR_Tut/images/sharpen.jpeg', 2)    