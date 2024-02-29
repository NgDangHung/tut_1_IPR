import cv2

def resize_and_threshold(image_path, output_path, width=None, height=None, threshold_value=None):
    # Read the image
    image = cv2.imread(image_path, cv2.COLOR_BGR2GRAY)

    # Resize the image if width and height are specified
    if width is not None and height is not None:
        image = cv2.resize(image, (width, height))

    # Apply binary thresholding
    _, thresholded = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Write the processed image to the output path
    cv2.imwrite(output_path, thresholded)

    print("Image processing completed and saved to", output_path)

if __name__ == "__main__":
    # Path to the input image
    input_image_path = "IPR_Tut/Assignment1/image/demo.jpeg"

    # Path to save the processed image
    output_image_path = "IPR_Tut/Assignment1/image/resized_image.jpeg"

    # Width and height for resizing (optional)
    # Set either width or height, or both to None to maintain aspect ratio
    width = 300
    height = 400

    # Threshold value for binary thresholding
    threshold_value = 127

    # Perform image resizing and thresholding
    resize_and_threshold(input_image_path, output_image_path, width, height, threshold_value)
