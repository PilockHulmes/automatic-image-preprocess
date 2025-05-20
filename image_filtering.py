from waifuc.action import (
    ModeConvertAction, ClassFilterAction, MinAreaFilterAction, FilterSimilarAction, CCIPAction, 
    HeadCountAction, RatingFilterAction, FaceCountAction, PersonSplitAction, AlignMinSizeAction,
    PaddingAlignAction,
)
from waifuc.export import SaveExporter
from waifuc.source import LocalSource

img_dir = "D:/Grabber/fu_xuan"
output_dir = "D:/train/filtered/fu_xuan"

source = LocalSource(img_dir)
source.attach(
    ModeConvertAction(mode="RGB", force_background="white"), # change all the images to RGB format, for the PNG images with transparent background, it adds a white background to them
    ClassFilterAction(["illustration", "bangumi"]), # no comic or 3d
# RatingFilterAction(["safe", "r18"]), # filter images with rating, safe r15 r18
    HeadCountAction(max_count=2), #ensures that no more than 2 individuals appear in each image.
    MinAreaFilterAction(1024), # filter out the images smaller than 1024x1024.
    FilterSimilarAction("all"), # filter duplicated images

    # human processing
    FaceCountAction(1),  # drop images with 0 or >1 faces
    PersonSplitAction(),  # crop for each person
    FaceCountAction(1),
    CCIPAction(min_val_count=15), # evaluates 15 image samples using the CCIP metric, removing images that do not feature the specified character.
    AlignMinSizeAction(800), # if min(height, weight) > 800, resize it to 800

    PaddingAlignAction((1024, 1024)),  # align to 1024x1024
    FilterSimilarAction('all'),  # filter again
).export(SaveExporter(output_dir))