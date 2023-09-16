# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


path = '/Users/mike/Documents/Notes/tasks.md'

def parse_path(path: str):
    prefix, *_, suffix = path.split('.')
    file_path = '/'.join(prefix.split('/')[:-1])
    name_file = '/'.join(prefix.split('/')[-1:])
    file_tulp = ('File path: ' + file_path,
                 'File name: ' + name_file,
                 'File extension: ' + suffix)
    print(file_tulp)

parse_path(path)
