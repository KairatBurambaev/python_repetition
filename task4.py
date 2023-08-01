import os

def split_path(file_path):
    path, file_name = os.path.split(file_path)
    file_name, extension = os.path.splitext(file_name)
    return path, file_name, extension

file_path = '/home/user/Documents/homework.txt'
result = split_path(file_path)
print(result)