import os
import numpy as np
import matplotlib.pyplot as plt
import rawpy
from skimage import io, color

def plot_grayscale_image(image_path):
    """Load an RGB image, convert it to grayscale, and display it."""
    image = io.imread(image_path)
    grayscale_image = color.rgb2gray(image)
    
    plt.imshow(grayscale_image, cmap='gray')
    plt.title('Grayscale Image')
    plt.show()

def get_bayer_pattern_from_raw(raw_file):
    """Retrieve the Bayer pattern from a RAW file."""
    with rawpy.imread(raw_file) as raw:
        bayer_pattern = raw.raw_pattern
        bayer_pattern_str = "".join([chr(raw.color_desc[i]) for i in bayer_pattern.flatten()])
    
    return bayer_pattern, bayer_pattern_str

# Base directory for data
base_dir = "C:/Users/nguye/Downloads/ISP_homework/ISP_homework"

# Usage example for displaying a grayscale image from an RGB JPEG.
image_path = os.path.join(base_dir, "data/baby.jpeg")
plot_grayscale_image(image_path)

# Usage example for getting the Bayer pattern from a RAW file.
image_path_raw = os.path.join(base_dir, "data/baby.nef")
bayer_pattern, bayer_pattern_str = get_bayer_pattern_from_raw(image_path_raw)
print("Bayer pattern (numerical):", bayer_pattern)
print("Bayer pattern (string):", bayer_pattern_str)
