import sys
import os

root_dir = sys.argv[1]
images = os.listdir(root_dir)
count0 = 0
for image in images:
  print '%i of %i' % (count0, len(images))
  count0 = count0 + 1
  image_path = os.path.join(root_dir, image)
  convert_cmd = 'convert -resize 256x256\! %s %s' % (image_path, image_path)
  os.system(convert_cmd)
