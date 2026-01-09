import numpy as np
from PIL import Image
import os

# https://files.erasmusmagazine.nl/app/uploads/2024/05/14155517/TUe-TU-Eindhoven-Atlas-gebouw_Wesley-Klop-1280x854.jpg    - image source


# https://imagemagick.org/#gsc.tab=0   - software to convert it to black and white


image = Image.open("./task6/campus_bw.jpg")  # load image

w, h = image.size
print(f"Dimensions: {w}x{h}")
og_size = round(w * h * 8 /1024, 2)
print(f"Original size: {og_size} KB")   # size with no compression 

# file_size = os.path.getsize("./task6/campus_bw.jpg")    
# print(f"File size: {file_size / 1024:.2f} KB")  # size with compression by JPG

A = np.array(image, dtype=np.float64)  # convert image to numpy array

u, s, vT = np.linalg.svd(A, full_matrices=True)  # compute SVD 


def truncate(k, show=False, save=True):
    u2 = u[:, :k]   # truncate u to first `k` column vectors
    s2 = s[:k]      # truncate s to first `k` (sigma) values 
    vT2 = vT[:k,:]    # truncate vT to first `k` row vectors

    A2 = u2 @ np.diag(s2) @ vT2   # compute new A - image
    clipped_A2 = np.clip(A2, 0, 255).astype(np.uint8)   # fix data type
    new_image = Image.fromarray(clipped_A2)   # load image
    
    if save: new_image.save(f"./task6/campus_k{k}.jpg")  # save image
    if show: new_image.show()

    size = round((k * w + k * h + k * 1) * 8 /1024, 2)  # file size w/o JPG compression
    print(f"k={k:<3} -> size: {size:<7} KB | saving: {100 - (size / og_size * 100):<5.2f} %")


for k in [5, 10, 25, 50, 75, 100, 150, 200, 500]:  # try these values - we should mention only 3 :)
    truncate(k)
    
    