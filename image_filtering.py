from waifuc.action import ModeConvertAction, ClassFilterAction, MinAreaFilterAction, FilterSimilarAction
from waifuc.export import SaveExporter
from waifuc.source import LocalSource

img_dir = "/your img folder/"
output_dir = "/your output folder/"

source = LocalSource(img_dir)
source.attach(
    ModeConvertAction(mode="RGB", force_background="white"),
    ClassFilterAction(["illustration", "bangumi"]),
    MinAreaFilterAction(1024),
    FilterSimilarAction("all"),
).export(SaveExporter(output_dir))