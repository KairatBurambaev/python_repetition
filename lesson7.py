import os
import logging
import argparse

class FileRenameError(Exception):
    def __init__(self, message, file_name):
        self.message = message
        self.file_name = file_name

    def __str__(self):
        return f"Ошибка переименования файла: {self.message} - {self.file_name}"

def group_rename_files(desired_name, num_digits, original_extension, new_extension, name_range):
    directory = '/path'  # Путь к каталогу c файлами

    # Получаем список файлов в каталоге
    files = os.listdir(directory)

    # Фильтруем файлы по расширению
    files = [file for file in files if file.endswith(original_extension)]

    # Создание логгера
    logger = logging.getLogger('file_rename')
    logger.setLevel(logging.ERROR)

    # Создание обработчика логгера для записи в файл
    file_handler = logging.FileHandler('file_rename.log')
    file_handler.setLevel(logging.ERROR)

    # Создание обработчика логгера для вывода на консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    # Создание форматтера лога
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Привязка форматтера к обработчикам логгера
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Добавление обработчиков к логгеру
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Проходимся по каждому файлу и переименовываем его
    for i, file in enumerate(files):
        try:
            # Извлекаем диапазон символов из оригинального имени файла
            original_name = file[name_range[0]-1:name_range[1]]

            # Создаем новое имя файла с порядковым номером
            new_name = f"{desired_name}_{str(i+1).zfill(num_digits)}"

            # Переименовываем файл
            new_file = file.replace(original_name, new_name)
            new_file = os.path.splitext(new_file)[0] + new_extension

            # Полный путь к старому и новому файлу
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_file)

            # Переименование файла
            os.rename(old_path, new_path)

        except Exception as e:
            logger.error(str(e), exc_info=True)  # Запись ошибки в лог
            raise FileRenameError(str(e), file)

    logger.info("Файлы успешно переименованы.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File renaming script')
    parser.add_argument('desired_name', type=str, help='Desired name for the files')
    parser.add_argument('num_digits', type=int, help='Number of digits for the sequential numbering')
    parser.add_argument('original_extension', type=str, help='Original extension of the files')
    parser.add_argument('new_extension', type=str, help='New extension for the files')
    parser.add_argument('name_range', type=int, nargs=2, help='Range of characters to extract from the original file name')

    args = parser.parse_args()

    try:
        group_rename_files(args.desired_name, args.num_digits, args.original_extension, args.new_extension, args.name_range)
    except FileRenameError as e:
        print(e)