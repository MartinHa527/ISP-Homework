import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d
import os  # Import os module for handling file paths

def demosaic_bilinear(raw_image):
    # Define the new set of coordinates where interpolation will occur
    old_x = np.arange(raw_image.shape[1])
    old_y = np.arange(raw_image.shape[0])
    new_x = np.linspace(0, raw_image.shape[1] - 1, 2 * raw_image.shape[1])
    new_y = np.linspace(0, raw_image.shape[0] - 1, 2 * raw_image.shape[0])

    # Create a function to perform bilinear interpolation on a single channel
    def interpolate_channel(channel):
        interp_func = interp2d(old_x, old_y, channel, kind='linear')
        return interp_func(new_x, new_y)

    # Apply the interpolation to each channel
    interpolated_channels = [interpolate_channel(raw_image[:, :, i]) for i in range(3)]

    # Stack the interpolated channels to form the final image
    return np.stack(interpolated_channels, axis=-1).astype(np.uint8)

# Define the correct base directory and construct the file paths
base_dir = "C:/Users/nguye/Downloads/ISP_homework/ISP_homework"  # Adjusted path to include correct directory
image_path = os.path.join(base_dir, "data/baby.jpeg")  # Construct path using os.path.join

# Load the image
image = io.imread(image_path)
image = image.astype(np.uint8)

# Perform bilinear interpolation
interpolated_image = demosaic_bilinear(image)

# Display the interpolated image
plt.imshow(interpolated_image)
plt.title('Bilinear Interpolated Image')
plt.show()
