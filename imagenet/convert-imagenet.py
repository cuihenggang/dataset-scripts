import sys
import os

root_dir = sys.argv[1]
tars = os.listdir(root_dir)
count0 = 0
for tar in tars:
  if (not tar.endswith('tar')):
    continue
  print '%i of %i' % (count0, len(tars))
  count0 = count0 + 1
  tar_path = os.path.join(root_dir, tar)
  print tar_path
  image_dir = '%s.images' % (tar_path)
  mkdir_cmd = 'mkdir %s' % (image_dir)
  print mkdir_cmd
  os.system(mkdir_cmd)
  untar_cmd = 'tar xvf %s -C %s' % (tar_path, image_dir)
  print untar_cmd
  os.system(untar_cmd)
  # images = os.listdir(image_dir)
  # count1 = 0
  # for image in images:
    # print '%i of %i / %i of %i' % (count1, len(images), count0, len(tars))
    # count1 = count1 + 1
    # image_path = os.path.join(image_dir, image)
    # convert_cmd = 'convert -resize 256x256\! %s %s' % (image_path, image_path)
    # print convert_cmd
    # os.system(convert_cmd)
  delete_tar_cmd = 'rm %s' % (tar_path)
  print delete_tar_cmd
  os.system(delete_tar_cmd)
  