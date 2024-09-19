#Author: Alexia Melo
import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity, mean_squared_error
from skimage.transform import resize
import cv2

def find_difference(image1, image2, use_gray=True, save_diff=False, diff_filename="difference_image.png"):
    assert image1.shape == image2.shape, "As imagens precisam ter o mesmo formato."

    if use_gray:
        image1 = rgb2gray(image1)
        image2 = rgb2gray(image2)

    score, difference_image = structural_similarity(image1, image2, full=True, multichannel=not use_gray)
    mse_value = mean_squared_error(image1, image2)
    
    print(f"Similaridade entre as imagens: {score}")
    print(f"Erro quadrático médio (MSE): {mse_value}")

    normalized_difference_image = (difference_image - np.min(difference_image)) / (np.ptp(difference_image))
    
    if save_diff:
        cv2.imwrite(diff_filename, (normalized_difference_image * 255).astype(np.uint8))
    
    return normalized_difference_image

def transfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image

def resize_images(image1, image2, output_shape):
    resized_image1 = resize(image1, output_shape, anti_aliasing=True)
    resized_image2 = resize(image2, output_shape, anti_aliasing=True)
    return resized_image1, resized_image2

def apply_mask(image, mask):
    assert image.shape[:2] == mask.shape, "A máscara deve ter o mesmo tamanho que a imagem."
    return np.where(mask[..., None], image, 0)
