import sys
import os
from PIL import Image

thumbnailSize = (480,480)

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)

# check if new/ exist, and if not, create

if not os.path.exists(output_folder):
  os.makedirs(output_folder)

# loop through input-images,
# convert to png, save to new
# folder

for filename in os.listdir(image_folder):
  img = Image.open(f'{image_folder}{filename}')
  print(img.size)
  img = img.resize(thumbnailSize)
  img.thumbnail(thumbnailSize)
  print(img.size)

  clean_name = os.path.splitext(filename)[0]
  img.save(f'{output_folder}{clean_name}.png', 'png')
  print('image saved!')