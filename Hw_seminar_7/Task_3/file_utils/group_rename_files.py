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