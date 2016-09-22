import sys
import os

filename_path = sys.argv[1]
input_dir = sys.argv[2]
output_dir = sys.argv[3]

filename_fd = open(filename_path, 'r')
for line in filename_fd:
  filename = line.split()[0]
  filename_base = os.path.basename(filename)
  filename_base = filename_base.split('.')[0]
  inputfile = os.path.join(input_dir, filename)
  outputfile = os.path.join(output_dir, filename_base)
  mkdir_cmd = 'mkdir -p -m 755 %s' % outputfile
  print mkdir_cmd
  os.system(mkdir_cmd)
  ffmpeg_cmd = 'ffmpeg -i %s -r 30 %s/%s.%%4d.jpg' % (inputfile, outputfile, filename_base)
  print ffmpeg_cmd
  os.system(ffmpeg_cmd)
