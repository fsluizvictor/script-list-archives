import csv
import os

import config
from typing import List


def open_file_csv(file_name: str) -> List[List[str]]:
    try:
        with open(file_name, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            file_rows = list()
            content_row = list()
            for row in spamreader:
                content = [element + ";" for element in row if element]
                content = "".join(content)
                content = content.split(";")
                if config.GET_ELEMENT_PEER_POSITION:
                    for position in config.GET_ELEMENT_PEER_POSITION:
                        content_row.append(content[position])
                else:
                    content_row.append(content)
                file_rows.append(content_row)
                content_row = list()
    except FileNotFoundError:
        print('file not found')

    return file_rows


def write_file_csv(file_name: str, content: List[List[str]]):
    with open(file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for row in content:
            spamwriter.writerow(row)


def list_files_directory() -> List[str]:
    file_names = list()
    for filename in os.listdir(config.FILE_PATH_IN):
        with open(os.path.join(config.FILE_PATH_IN, filename), 'r') as f:
            file_names.append(f.name)
    return file_names

