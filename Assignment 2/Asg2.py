import numpy as np
import cv2
from matplotlib import pyplot as plt

def apply_low_pass_filter(image, cutoff_frequency):
    # Biến đổi Fourier của hình ảnh đầu vào
    f_image = np.fft.fft2(image)
    fshift = np.fft.fftshift(f_image)

    # Tạo ma trận filter để làm mờ (lọc thông thấp)
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow - cutoff_frequency:crow + cutoff_frequency, ccol - cutoff_frequency:ccol + cutoff_frequency] = 1

    # Áp dụng filter vào hình ảnh trong không gian tần số
    fshift_filtered = fshift * mask

    # Biến đổi Fourier ngược để lấy hình ảnh đã xử lý
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    return img_back

def apply_high_pass_filter(image, cutoff_frequency):
    # Biến đổi Fourier của hình ảnh đầu vào
    f_image = np.fft.fft2(image)
    fshift = np.fft.fftshift(f_image)

    # Tạo ma trận filter để làm sắc nét (lọc thông cao)
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    
    # Giảm kích thước của vùng chênh lệch (kernel)
    mask = np.ones((rows, cols), np.uint8)
    mask[crow - cutoff_frequency:crow + cutoff_frequency, ccol - cutoff_frequency:ccol + cutoff_frequency] = 0

    # Áp dụng filter vào hình ảnh trong không gian tần số
    fshift_filtered = fshift * mask

    # Biến đổi Fourier ngược để lấy hình ảnh đã xử lý
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    return img_back


# Đọc hình ảnh
image = cv2.imread('IPR_Tut/Assignment 2/image/blur.jpeg', 0)  # Đọc hình ảnh dưới dạng ảnh xám

# Áp dụng bộ lọc thông thấp với một ngưỡng cắt cụ thể
cutoff_frequency_low = 30
blurred_image = apply_low_pass_filter(image, cutoff_frequency_low)

# Áp dụng bộ lọc thông cao với một ngưỡng cắt cụ thể
cutoff_frequency_high = 30
sharpened_image = apply_high_pass_filter(image, cutoff_frequency_high)

# Hiển thị hình ảnh gốc, hình ảnh đã làm mờ và hình ảnh đã làm sắc nét
plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(blurred_image, cmap='gray')
plt.title('Blurred Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(sharpened_image, cmap='gray')
plt.title('Sharpened Image'), plt.xticks([]), plt.yticks([])
plt.show()
