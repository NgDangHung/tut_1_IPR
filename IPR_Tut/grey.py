from PIL import Image

def convert_to_grayscale(image_path, output_path):
    image = Image.open(image_path)

    grayscale_image = image.convert('L')

    grayscale_image.save(output_path)

    print(f"Grayscale image saved as {output_path}")


convert_to_grayscale('Nguyễn Đăng Hùng_2001040085.jpg', 'IPR_Tut/images/grayscale.jpeg')