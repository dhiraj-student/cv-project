# Histogram Equalization

This project demonstrates the concept and implementation of **Histogram Equalization**, a fundamental technique in image processing used to enhance the contrast of images. It is particularly effective for images that are too bright or too dark.

## What is Histogram Equalization?

Histogram Equalization is a method that improves the contrast of an image by modifying the intensity distribution of the histogram. It redistributes pixel intensity values to span the full dynamic range, thus making features in the image more distinguishable.

## Features

- Read and display grayscale images  
- Compute and plot the original image histogram  
- Apply histogram equalization algorithm  
- Display the equalized image alongside its histogram  
- Visual and statistical comparison between original and enhanced images  

## Technologies Used

- Python 3  
- OpenCV (`cv2`)  
- Matplotlib (for histogram plotting)  
- NumPy (for pixel manipulation)  

## How to Run

1. Make sure you have Python 3 installed.  
2. Install required libraries:  
   ```bash
   pip install opencv-python matplotlib numpy
