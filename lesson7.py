import os

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
            raise FileRenameError(str(e), file)

    print("Файлы успешно переименованы.")

group_rename_files("new_file", 3, ".jpeg", ".png", [3, 6])