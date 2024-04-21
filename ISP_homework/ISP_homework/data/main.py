import os
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

def main():
    # Define the correct path to the image
    image_path = "C:/Users/nguye/Downloads/ISP_homework/ISP_homework/data/baby.tiff"

    # Check if the image file exists to avoid FileNotFoundError
    if not os.path.exists(image_path):
        print("File not found:", image_path)
        return

    # Define transformation constants
    white = 16383
    black = 0
    red = 1.628906
    green = 1.0
    blue = 1.386719

    # Load the image using skimage
    image = io.imread(image_path)
    plt.imshow(image)
    plt.title('Loaded Image')
    plt.show()

    # Extract image dimensions
    height, width = image.shape[:2]

    # Calculate bits per pixel
    bitsPerPixel = image.dtype.itemsize * 8

    # Convert image to a floating point data type for processing
    dpArray = image.astype(np.float64)

    # Calculate the scaling factor and shift for linear transformation
    scale_denom = max(white - black, 1e-10)  # Ensure the denominator is not zero
    scale = 1.0 / scale_denom
    shift = -np.float64(black) * scale

    # Apply the linear transformation
    imageLinear = dpArray * scale + shift

    # Clip values to range [0, 1]
    imageLinear = np.clip(imageLinear, 0, 1)

    print("Bits per pixel:", bitsPerPixel)
    print("Width:", width)
    print("Height:", height)

if __name__ == "__main__":
    main()
