### 1. Напишите функцию для транспонирования матрицы 

### 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление. 

### 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

### 4. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

### 5. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии.

### 6. Создайте функцию генератор чисел Фибоначчи.

### Урок 7. Напишите функцию группового переименования файлов. Она должна:
#### 1. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
#### 2. принимать параметр количество цифр в порядковом номере.
#### 3. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
#### 4. принимать параметр расширение конечного файла.
#### 5. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

### Урок 8. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
#### 1. Для дочерних объектов указывайте родительскую директорию.
#### 2. Для каждого объекта укажите файл это или директория.
#### 3. Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

### Урок 10. Создайте класс-фабрику.
#### 1. Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
#### 2. Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики. 

### Урок 11. Создайте класс Матрица.
#### 1. Добавьте методы для:
○вывода на печать,
○сравнения,
○сложения,
○*умножения матриц

### Урок 12. Создайте класс студента.
#### 1. Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
#### 2. Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
#### 3. Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
#### 4. Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

### Урок 13. Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.
### проделал в lesson7.py, lesson8.py, lesson10.py

### Финальное задание. Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров.
### проделал в lesson7.py, lesson8.py, lesson10.py