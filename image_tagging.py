from imgutils.tagging import get_wd14_tags, drop_overlap_tags, tags_to_text
import os
import glob
from PIL import Image
from tqdm import tqdm

Image.MAX_IMAGE_PIXELS = None
os.environ["HF_ENDPOINT"] = "https://huggingface.co"

image_dir = "D:/train/filtered/fu_xuan/"
image_path = glob.glob(os.path.join(image_dir, "*.jpg")) + glob.glob(os.path.join(image_dir, "*.png"))

text_path = glob.glob(os.path.join(image_dir, "*.txt"))
text_name = [os.path.basename(path) for path in text_path]

with tqdm(total=len(image_path), desc="Processing") as pbar:
    for p in image_path:
        if os.path.basename(p).split(".")[0] + ".txt" in text_name: # skip the images that already been tagged
            pbar.update(1)
            continue
        else:
            chars, features = get_wd14_tags(p, model_name="EVA02_Large", no_underline=True, drop_overlap=True, fmt=("character", "general"))
            tags = {**chars, **features}
            tags = tags_to_text(tags, use_escape=True)

            fname, _ = os.path.splitext(p)
            print("saved file name:",fname)
            with open(fname + ".txt", "w", encoding="utf-8") as f:
                f.write(tags)
            
            pbar.update(1)

print("Tagging Complete!")