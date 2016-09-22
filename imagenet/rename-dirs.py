import sys
import os

root_dir = sys.argv[1]
dirs = os.listdir(root_dir)

for dir in dirs:
  dir_path = os.path.join(root_dir, dir)
  renamed_dir = dir_path[:-11]
  rename_cmd = 'mv %s %s' % (dir_path, renamed_dir)
  print rename_cmd
  os.system(rename_cmd)
