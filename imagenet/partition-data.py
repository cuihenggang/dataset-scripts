import sys
import os

label_file = sys.argv[1]
train_or_val = sys.argv[2]
num_parts = int(sys.argv[3])
output_dir_root = sys.argv[4]

# output_dir_root = '%iparts' %  (num_parts)
# os.system('mkdir %s' % output_dir_root)
output_label_files = []
for i in range(num_parts):
  output_label_file_name = '%s.txt.%i' % (train_or_val, i)
  output_label_files.append(open(os.path.join(output_dir_root, output_label_file_name), 'w'))

# ln directories
label_file_fd = open(label_file, 'r')
count  = 0
for line in label_file_fd:
  part_id = count % num_parts
  output_label_files[part_id].write(line)
  count = count + 1
  if count % 1000 == 0:
    print count

for i in range(num_parts):
  output_label_files[i].close()
