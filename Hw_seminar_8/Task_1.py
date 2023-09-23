# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов
# и директорий.

import os
import json
import csv
import pickle
def recursive_dir(path: str, output_dir: str):
    def save_results_as_json(results):
        with open(os.path.join(output_dir, 'results.json'), 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, ensure_ascii=False, indent=4)

    def save_results_as_csv(results):
        csv_file = os.path.join(output_dir, 'results.csv')
        with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
            csv_write = csv.DictWriter(csv_file, fieldnames=["Тип объекта", "Название", "Размер"], dialect='excel-tab',
quoting=csv.QUOTE_ALL)
            csv_write.writeheader()
            for result in results:
                csv_write.writerow(result)

    def save_results_as_pickle(results):
        with open(os.path.join(output_dir, 'results.pkl'), 'wb') as pickle_file:
            pickle.dump(results, pickle_file)

    results = []
    for root, dirs, files in os.walk(path):
        path = root.split(os.sep)
        total_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        #print((len(path) - 1) * '---', os.path.basename(root), 'Размер директории: ', total_size)
        results.append({'Тип объекта': 'Директория', 'Название': os.path.basename(root), 'Размер': total_size})

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            #print(len(path) * '---', file, 'Размер файла : ' ,file_size)
            results.append({'Тип объекта': 'Папка', 'Название': file, 'Размер': file_size})

    save_results_as_json(results)
    save_results_as_csv(results)
    save_results_as_pickle(results)


path = 'For_task_1'
output_directory = 'output'
os.makedirs(output_directory, exist_ok=True)

recursive_dir(path, output_directory)




