from PIL import Image
import numpy as np
import rasterio
from rasterio.transform import from_bounds
import os
from os.path import join

# Set the coordinates of the upper left and lower right corners of the image as floats
upper_left = ('lat', 'lon')
lower_right = ('lat', 'lon')

latest_img = sorted(os.listdir('input'), key=lambda x: os.path.getmtime(os.path.join('input', x)))[0]
input_img = join('input', latest_img)
dir_name = latest_img.split(".")[0]
output_folder = join('output', dir_name)
os.makedirs(output_folder, exist_ok=True)

def create_geotiff(image_path, output_folder, upper_left, lower_right):
    img = Image.open(image_path)
    img = img.convert('RGB')
    img_array = np.array(img)
    height, width = img_array.shape[:2]
    transform = from_bounds(upper_left[1], lower_right[0], lower_right[1], upper_left[0], width, height)
    output_tiff_path = join(output_folder, f'{dir_name}.tiff')

    with rasterio.open(
        output_tiff_path,
        'w',
        driver='GTiff',
        height=height,
        width=width,
        count=3,
        dtype=img_array.dtype,
        crs='EPSG:4326',
        transform=transform,
    ) as dst:
        for i in range(3):
            dst.write(img_array[:, :, i], i + 1)

    return output_tiff_path

geotiff_path = create_geotiff(input_img, output_folder, upper_left, lower_right)