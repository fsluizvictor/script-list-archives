import csv
import config
import adapter_database
from typing import List


def open_file_csv(file_name: str) -> List[List[str]]:
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
    return file_rows


def write_file_csv(file_name: str, content: List[List[str]]):
    with open(file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for row in content:
            spamwriter.writerow(row)


def process():
    for archive in config.FILE_NAMES:
        file_path = config.FILE_PATH_IN + archive
        content_file = open_file_csv(file_path)
        write_file_csv(file_path.replace('.txt', '_path_size.txt'), content_file)

        con, cur = adapter_database.create_connection(file_path.replace('.txt', '_path_size.db'))
        archive = archive.replace('.txt', '')
        archive = archive.replace('-', '')
        adapter_database.create_table(cur, archive)
        adapter_database.insert_items(cur, content_file, archive)
        adapter_database.finish_persistence_process(con)


if __name__ == '__main__':
    process()
