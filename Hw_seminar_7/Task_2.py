# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя,
# если оно передано. Далее счётчик файлов и расширение

import os


def group_rename_files(target_name: str, num_digits: int, source_extension: str, destination_extension: str,
                       name_range=None):
    source_files = [file for file in os.listdir() if file.endswith(source_extension)]

    for i, source_file in enumerate(source_files, start=1):
        source_file_name, source_file_extension = os.path.splitext(source_file)

        if name_range:
            source_file_name = source_file_name[name_range[0] - 1:name_range[1]]

        new_name = f"{source_file_name}_{target_name}_{str(i).zfill(num_digits)}{destination_extension}"

        # Проверяем, существует ли файл с таким именем, и если да, генерируем новое уникальное имя
        while os.path.exists(new_name):
            i += 1
            new_name = f"{source_file_name}_{target_name}_{str(i).zfill(num_digits)}{destination_extension}"

        os.rename(source_file, new_name)


group_rename_files("new_file", 3, ".doc", ".xsl", (3, 6))


