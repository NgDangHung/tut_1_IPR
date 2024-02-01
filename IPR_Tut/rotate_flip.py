from PIL import Image, ImageOps

def rotating_image(input_path, output_path, degress):

    image = Image.open(input_path)

    image_roated = image.rotate(degress)

    image_roated.save(output_path)

    print(f"Image saved as {output_path}")

rotating_image('IPR_Tut/images/demo.jpeg', 'IPR_Tut/images/rotate.jpeg', 45)

def fliping_image(input_path, output_path, flip_type):

    image = Image.open(input_path)

    if flip_type == 'horizontal':
        flipped_image = ImageOps.mirror(image)
    elif flip_type == 'vertical':
        flipped_image = ImageOps.flip(image)
    else:
        raise ValueError("Invalid input type. Use 'horizontal' or 'vertical'")
    
    flipped_image.save(output_path)

fliping_image('IPR_Tut/images/demo.jpeg', 'IPR_Tut/images/fliping.jpeg', 'vertical')
