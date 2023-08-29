import os
import json
import csv
import pickle

class TraverseDirectoryError(Exception):
    def __init__(self, directory):
        self.directory = directory

    def __str__(self):
        return f"TraverseDirectoryError: Не удалось пройти по каталогу '{self.directory}'"


class SaveDataError(Exception):
    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return f"SaveDataError: Не удалось сохранить данные в файл '{self.file_name}'"


def traverse_directory(directory):
    try:
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

    except Exception as e:
        raise TraverseDirectoryError(directory)


def save_to_json(data, file_name):
    try:
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    except Exception as e:
        raise SaveDataError(file_name)


def save_to_csv(data, file_name):
    try:
        keys = data[0].keys()
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, keys)
            writer.writeheader()
            writer.writerows(data)

    except Exception as e:
        raise SaveDataError(file_name)


def save_to_pickle(data, file_name):
    try:
        with open(file_name, 'wb') as pickle_file:
            pickle.dump(data, pickle_file)

    except Exception as e:
        raise SaveDataError(file_name)


try:
    directory = '/path/to/directory'  # Ввести свой путь
    result, total_size = traverse_directory(directory)

    save_to_json(result, 'result.json')
    save_to_csv(result, 'result.csv')
    save_to_pickle(result, 'result.pickle')

    print(f"Total directory size: {total_size} bytes")

except TraverseDirectoryError as e:
    print(str(e))

except SaveDataError as e:
    print(str(e))

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")