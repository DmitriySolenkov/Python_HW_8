import os
import json
import csv
import pickle


def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size


def save_directory_info(directory):
    info_list = []
    for dirpath, dirnames, filenames in os.walk(directory):
        dir_size = get_directory_size(dirpath)
        info_list.append({
            'name': dirpath,
            'type': 'Directory',
            'size': dir_size
        })
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            info_list.append({
                'name': filename,
                'type': 'File',
                'size': file_size
            })

    with open('directory_info.json', 'w', encoding='utf-8') as json_file:
        json.dump(info_list, json_file, indent=4)

    with open('directory_info.csv', 'w', newline='') as csv_file:
        fieldnames = ['name', 'type', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(info_list)

    with open('directory_info.pickle', 'wb') as pickle_file:
        pickle.dump(info_list, pickle_file)


save_directory_info("./Contain")
