import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import os  # Import the os module for handling file paths

def load_and_normalize_image(path):
    """Load an image and normalize it to float values between 0 and 1."""
    image = io.imread(path)
    return image.astype(np.float64) / 255.0

def white_world_balancing(image_float):
    """Apply white world white balancing to the image."""
    max_values = np.max(image_float, axis=(0, 1))
    return image_float / max_values

def gray_world_balancing(image_float):
    """Apply gray world white balancing to the image."""
    mean_values = np.mean(image_float, axis=(0, 1))
    return image_float / mean_values

def custom_scale_balancing(image_float, scales):
    """Apply custom scale balancing based on the provided scales."""
    for i, scale in enumerate(scales):
        image_float[:, :, i] *= scale
    return np.clip(image_float, 0, 1)

def display_images(images, titles, figsize=(12, 8)):
    """Display a list of images with corresponding titles."""
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=figsize)
    for ax, image, title in zip(axes.flatten(), images, titles):
        ax.imshow(image)
        ax.set_title(title)
    plt.tight_layout()
    plt.show()

# Define the correct base directory and construct the file paths
base_dir = "C:/Users/nguye/Downloads/ISP_homework/ISP_homework"
image_path = os.path.join(base_dir, "data/baby.jpeg")  # Use os.path.join to ensure correct path formation

# Load and normalize the image
image_float = load_and_normalize_image(image_path)

# Apply different white balancing techniques
white_balanced = white_world_balancing(image_float)
gray_balanced = gray_world_balancing(image_float)
scales = [1.628906, 1.00000, 1.386719]
scaled_balanced = custom_scale_balancing(image_float.copy(), scales)
scaled_balanced_uint8 = (scaled_balanced * 255).astype(np.uint8)

# Display results
images = [io.imread(image_path), white_balanced, gray_balanced, scaled_balanced_uint8]
titles = ['Original Image', 'White World White Balanced', 'Gray World White Balanced', 'Scaled White Balanced']
display_images(images, titles)
