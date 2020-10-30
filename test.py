from linestickerdata import get_image_paths

paths = get_image_paths(folder="dataofficial", n=5, num_workers=1, seed=0)
print(paths)