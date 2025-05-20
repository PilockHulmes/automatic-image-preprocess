from imgutils.metrics import anime_dbaesthetic
import glob
import os
from tqdm import tqdm
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
os.environ["HF_ENDPOINT"] = "https://huggingface.co"

image_dir = "D:/train/filtered/fu_xuan"
image_path = glob.glob(os.path.join(image_dir, "*.jpg"))

white_list = ["masterpiece", "best"]

with tqdm(total = len(image_path), desc = "Processing") as pbar:
    for path in image_path:
        score = anime_dbaesthetic(path)
        if score[0] not in white_list:
            os.remove(path)
        
        pbar.update(1)

print("Processing Complete!")
