import sys
import os
import subprocess

input_file_name = sys.argv[1]
batch_size = int(sys.argv[2])

input_file = open(input_file_name, 'r')
count = 0
starting_key = ""
key_batch_size = 0
for line in input_file:
  if count % batch_size == 0:
    if starting_key != "":
      print '%s %i' % (starting_key, key_batch_size)
      starting_key = ""
      key_batch_size = 0
    strs = line.split()
    file_name = strs[0]
    starting_key = '%08d_%s' % (count, file_name)
  key_batch_size = key_batch_size + 1
  count = count + 1

# Print the last key batch
assert starting_key != ""
print '%s %i' % (starting_key, key_batch_size)
