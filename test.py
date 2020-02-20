from linestickerdata import get_image_paths

paths = get_image_paths(folder="data", n=5, num_workers=2)
print(paths)