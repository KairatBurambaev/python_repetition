import os
import json
import csv
import pickle

def traverse_directory(directory):
    result = []
    total_size = 0

    for root, dirs, files in os.walk(directory):
        dir_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        total_size += dir_size

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            result.append({
                'name': file,
                'path': file_path,
                'type': 'file',
                'size': file_size,
                'parent_directory': os.path.dirname(file_path)
            })

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            result.append({
                'name': dir,
                'path': dir_path,
                'type': 'directory',
                'size': dir_size,
                'parent_directory': os.path.dirname(dir_path)
            })

    return result, total_size

def save_to_json(data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, file_name):
    keys = data[0].keys()
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, keys)
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, file_name):
    with open(file_name, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

directory = '/path/to/directory' # Ввести свой путь
result, total_size = traverse_directory(directory)

save_to_json(result, 'result.json')
save_to_csv(result, 'result.csv')
save_to_pickle(result, 'result.pickle')

print(f"Total directory size: {total_size} bytes")