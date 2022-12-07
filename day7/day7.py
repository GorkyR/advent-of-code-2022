from sys import argv
from os.path import join as path, dirname as dir

with open(path(dir(argv[0]), 'input.txt'), 'r') as file:
    input = file.read()

filesystem = {}
current_path = []


def directory(path):
    output_directory = filesystem
    for directory in path:
        if directory not in output_directory.keys():
            output_directory[directory] = {'__type': 'dir'}
        output_directory = output_directory[directory]
    return output_directory


lines = input.splitlines()
for line in lines:
    if line.startswith('$ cd'):
        dir = line.split(' ')[-1]
        if dir == '..':
            current_path.pop()
        elif dir == '/':
            current_path = ['/']
        else:
            current_path.append(dir)
        continue
    elif line == '$ ls' or line.startswith('dir '):
        continue
    size, filename = line.split(' ')
    directory(current_path)[filename] = {'__type': 'file', 'size': int(size)}

directory_sizes = []


def directory_size(fs, path=[]):
    size = sum([item['size'] if item['__type'] == 'file' else directory_size(
        item, path + [key]) for key, item in fs.items() if key != '__type'])
    directory_sizes.append(['/'.join(path).replace('//', '/'), size])
    return size


directory_size(filesystem, [])

print(sum((size for _, size in directory_sizes if size <= 100_000)))

total_used_space = directory_sizes[-1][1]
space_needed = 30_000_000 - (70_000_000 - total_used_space)

print(min([size for _, size in directory_sizes if size >= space_needed]))
