import sys
import os
import subprocess

input_file_name = sys.argv[1]

input_file = open(input_file_name, 'r')
count = 0
for line in input_file:
  strs = line.split()
  file_name = strs[0]
  key = '%08d_%s' % (count, file_name)
  print key
  count = count + 1
