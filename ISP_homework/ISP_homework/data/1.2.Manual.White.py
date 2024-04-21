import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib.backend_bases import MouseButton
import os

# Define the correct path for the image file
base_dir = "C:/Users/nguye/Downloads/ISP_homework/ISP_homework"  # Adjusted path to include correct directory
image_path = os.path.join(base_dir, "data/baby.jpeg")  # Construct path using os.path.join

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: No such file or directory: '{image_path}'")
else:
    # Load the image
    image = imread(image_path)

    # Set up the plot for user input
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(image)
    ax.set_title("Select a white patch of the screen")
    print("Click on the top-left and bottom-right corners of the patch.")

    # Get user input for the coordinates of the patch
    coords = plt.ginput(n=2, timeout=0, show_clicks=True, mouse_add=MouseButton.LEFT, mouse_pop=MouseButton.RIGHT, mouse_stop=MouseButton.MIDDLE)
    plt.close()

    # Ensure coordinates are integers and within image bounds
    coords = np.array(coords, dtype=int)
    coords = np.clip(coords, [0, 0], [image.shape[1] - 1, image.shape[0] - 1])

    # Extract the selected patch from the image
    patch = image[coords[0][1]:coords[1][1], coords[0][0]:coords[1][0]]
    r_mean, g_mean, b_mean = np.mean(patch, axis=(0, 1))

    # Compute weights for normalization
    weight_r = 1 / r_mean if r_mean else 1
    weight_g = 1 / g_mean if g_mean else 1
    weight_b = 1 / b_mean if b_mean else 1

    # Normalize the image based on the extracted white patch
    normalized_image = np.zeros_like(image, dtype=np.float64)
    normalized_image[:, :, 0] = image[:, :, 0] * weight_r
    normalized_image[:, :, 1] = image[:, :, 1] * weight_g
    normalized_image[:, :, 2] = image[:, :, 2] * weight_b
    normalized_image = np.clip(normalized_image, 0, 1)  # Ensure pixel values are valid

    # Display the original and white-balanced images
    fig, axs = plt.subplots(1, 2, figsize=(20, 10))
    axs[0].imshow(image)
    axs[0].set_title('Original Image')
    axs[1].imshow(normalized_image)
    axs[1].set_title('White Balanced Image')
plt.show()
