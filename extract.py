import rasterio

def get_corner_coordinates(geotiff_path):
    with rasterio.open(geotiff_path) as dataset:
        bounds = dataset.bounds
        corners = {
            'top_left': (bounds.left, bounds.top),
            'top_right': (bounds.right, bounds.top),
            'bottom_left': (bounds.left, bounds.bottom),
            'bottom_right': (bounds.right, bounds.bottom)
        }
        return corners

if __name__ == "__main__":
    geotiff_path = 'output/Gjenesia/Gjenesia.tiff'
    corners = get_corner_coordinates(geotiff_path)
    for corner, coord in corners.items():
        print(f"{corner}: {coord}")
