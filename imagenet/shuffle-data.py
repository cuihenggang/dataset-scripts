import sys
import os
from random import shuffle

train_or_val = sys.argv[1]
num_parts = int(sys.argv[2])

output_train_label_files = []
output_val_label_files = []
for i in range(num_parts):
  input_label_file_name = '%iparts/%s.txt.%i' % (num_parts, train_or_val, i)
  input_label_file = open(input_label_file_name, 'r')
  output_label_file_name = '%iparts/%s.shuffled.txt.%i' % (num_parts, train_or_val, i)
  output_label_file = open(output_label_file_name, 'w')
  lines = []
  for line in input_label_file:
    lines.append(line)
  shuffle(lines)
  for line in lines:
    output_label_file.write(line)
  input_label_file.close()
  output_label_file.close()
