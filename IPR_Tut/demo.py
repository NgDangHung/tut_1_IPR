import cv2

img_path = "IPR_Tut/images/Nguyễn Đăng Hùng_2001040085.jpg"

img = cv2.imread(img_path)

if img is not None:
    # Hiển thị ảnh
    cv2.imshow("Image", img)

    # Đợi cho đến khi người dùng nhấn một phím bất kỳ để đóng cửa sổ
    cv2.waitKey(0)

    # Đóng cửa sổ
    cv2.destroyAllWindows()
else:
    print("Không thể đọc được ảnh. Đường dẫn có thể không chính xác.")
