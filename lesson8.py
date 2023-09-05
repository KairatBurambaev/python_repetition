import os
import json
import csv
import pickle
import logging
import argparse

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
        logger.error(str(e), exc_info=True)
        raise TraverseDirectoryError(directory)


def save_to_json(data, file_name):
    try:
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    except Exception as e:
        logger.error(str(e), exc_info=True)
        raise SaveDataError(file_name)


def save_to_csv(data, file_name):
    try:
        keys = data[0].keys()
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

    except Exception as e:
        logger.error(str(e), exc_info=True)
        raise SaveDataError(file_name)

def save_to_pickle(data, file_name):
    try:
        with open(file_name, 'wb') as pickle_file:
            pickle.dump(data, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)

    except Exception as e:
        logger.error(str(e), exc_info=True)
        raise SaveDataError(file_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Directory traversal and data saving script')
    parser.add_argument('directory', type=str, help='Directory to traverse')
    parser.add_argument('--json', action='store_true', help='Save data as JSON')
    parser.add_argument('--csv', action='store_true', help='Save data as CSV')
    parser.add_argument('--pickle', action='store_true', help='Save data as pickle')

    args = parser.parse_args()

    logger = logging.getLogger('traverse_and_save')
    logger.setLevel(logging.ERROR)

    file_handler = logging.FileHandler('traverse_and_save.log')
    file_handler.setLevel(logging.ERROR)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    try:
        result, total_size = traverse_directory(args.directory)

        if args.json:
            save_to_json(result, 'result.json')
            print("Data saved as JSON.")

        if args.csv:
            save_to_csv(result, 'result.csv')
            print("Data saved as CSV.")

        if args.pickle:
            save_to_pickle(result, 'result.pickle')
            print("Data saved as pickle.")

    except TraverseDirectoryError as e:
        print(str(e))

    except SaveDataError as e:
        print(str(e))