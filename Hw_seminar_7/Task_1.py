# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil

file_name = input('Введите название файла, который хотите отсортировать: ')

def sort_file(file_name: str):
    if os.path.exists(file_name):
        pict_directory = 'picture'
        text_directory = 'text'
        video_directory = 'video'
        os.makedirs(pict_directory, exist_ok=True)  # Создаем директорию, если она не существует
        os.makedirs(text_directory, exist_ok=True)
        os.makedirs(video_directory, exist_ok=True)
        _, extension = os.path.splitext(file_name)
        pict_extensions = ['.png', '.jpeg', '.gif', '.raw', '.tiff', '.bmp', '.psd']
        text_extensions = ['.doc', '.docx', '.txt', '.pdf', '.rtf', '.scv', '.xls']
        video_extensions = ['.mp4', '.mpg', '.mpe', '.divx', '.avi', '.rm', '.ogv']
        if extension in pict_extensions:
            dest_picture = os.path.join(pict_directory, file_name)
            try:
                shutil.move(file_name, dest_picture)
                print("Файл успешно перемещен в: ", dest_picture)
            except IsADirectoryError:
                print("Исходное местоположение - это файл, а местоположение назначения - это директория.")
        elif extension in text_extensions:
            dest_text = os.path.join(text_directory, file_name)
            try:
                shutil.move(file_name, dest_text)
                print("Файл успешно перемещен в: ", dest_text)
            except IsADirectoryError:
                print("Исходное местоположение - это файл, а местоположение назначения - это директория.")
        elif extension in video_extensions:
            dest_video = os.path.join(video_directory, file_name)
            try:
                shutil.move(file_name, dest_video)
                print("Файл успешно перемещен в: ", dest_video)
            except IsADirectoryError:
                print("Исходное местоположение - это файл, а местоположение назначения - это директория.")
        else:
            print("Расширение файла не поддерживается.")
    else:
        print("Файл не существует.")

sort_file(file_name)