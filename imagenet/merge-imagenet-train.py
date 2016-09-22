import sys
import os

input_file_prefix = sys.argv[1]
output_file_name = sys.argv[2]
num_parts = int(sys.argv[3])

# os.system('mkdir %s' % output_dir_root)
input_lines_multi_part = []
total_lines = 0
for i in range(num_parts):
  input_train_label_file_name = '%s.%i' % (input_file_prefix, i)
  input_train_label_file = open(input_train_label_file_name, 'r')
  input_lines = []
  for line in input_train_label_file:
    input_lines.append(line)
  input_lines_multi_part.append(input_lines)
  total_lines = total_lines + len(input_lines)

outputfile = open(output_file_name, 'w')
for i in range(total_lines):
  part_id = i % num_parts
  line_id = i / num_parts
  outputfile.write(input_lines_multi_part[part_id][line_id])
outputfile.close()
