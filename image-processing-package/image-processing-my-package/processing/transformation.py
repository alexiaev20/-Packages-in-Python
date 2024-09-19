#Author: Alexia Melo
from skimage.transform import resize

def resize_image(image, proportion_height=1.0, proportion_width=1.0):
    assert 0 < proportion_height <= 1, "A proporção de altura deve estar entre 0 e 1."
    assert 0 < proportion_width <= 1, "A proporção de largura deve estar entre 0 e 1."

    try:
        height = round(image.shape[0] * proportion_height)
        width = round(image.shape[1] * proportion_width)
        image_resized = resize(image, (height, width), anti_aliasing=True)
        return image_resized
    except Exception as e:
        print(f"Erro ao redimensionar a imagem: {e}")
        return None

def resize_to_dimensions(image, target_height, target_width):
    try:
        image_resized = resize(image, (target_height, target_width), anti_aliasing=True)
        return image_resized
    except Exception as e:
        print(f"Erro ao redimensionar para as dimensões especificadas: {e}")
        return None
