import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray
import os

# ------------------------------
# Step 1: Normalize image to uint8 (0–255)
# ------------------------------
def normalize_image(image):
    norm_img = (image - np.min(image)) * (255 / (np.max(image) - np.min(image)))
    return norm_img.astype('uint8')

# ------------------------------
# Step 2: Compute histogram
# ------------------------------
def compute_histogram(image):
    hist = np.zeros(256)
    height, width = image.shape
    for i in range(height):
        for j in range(width):
            hist[image[i, j]] += 1
    hist /= (height * width)  # Normalize
    return hist

# ------------------------------
# Step 3: Apply histogram equalization
# ------------------------------
def histogram_equalization(image, hist):
    cdf = np.cumsum(hist)  # Compute the CDF
    height, width = image.shape
    eq_image = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            eq_image[i, j] = int(cdf[image[i, j]] * 255)  # Map to new intensity

    return eq_image

# ------------------------------
# Step 4: Display image and histogram
# ------------------------------
def display_image_and_hist(image, title):
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.bar(np.arange(256), compute_histogram(image))
    plt.title("Histogram")
    plt.show()

# ------------------------------
# Step 5: Process any image with safety
# ------------------------------
def process_image(path, title="Image"):
    try:
        print(f"\nProcessing: {title}")
        image = io.imread(path)

        # Convert to grayscale if it's a color image
        if image.ndim == 3:
            gray = rgb2gray(image)
        else:
            gray = image

        # Normalize image
        norm_img = normalize_image(gray)
        display_image_and_hist(norm_img, title + " (Original)")

        # Compute histogram and perform histogram equalization
        hist = compute_histogram(norm_img)
        eq_img = histogram_equalization(norm_img, hist)
        display_image_and_hist(eq_img, title + " (Equalized)")

    except FileNotFoundError:
        print(f"❌ File not found: {path}")
    except Exception as e:
        print(f"⚠️ Error processing {title}: {e}")

# ------------------------------
# Process multiple images
# ------------------------------
images = [
    ("crowd-grayscale.png", "Crowd"),
    ("bobmarley.jpg", "Bob Marley"),
    ("lowconimage.png", "Low Contrast"),
]

for path, title in images:
    process_image(path, title)
