import csv
from typing import List

FILE_PATH_IN = '/Users/luizvictorsantos/SyngentaProjects/protector-backup/files/striderlib_2020_03_13_21_15_01.txt'
FILE_PATH_OUT = '/Users/luizvictorsantos/SyngentaProjects/protector-backup/files/out.txt'
GET_ELEMENT_PEER_POSITION = {4, 8}


def open_file_csv(file_name: str) -> List[List[str]]:
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        file_rows = list()
        for row in spamreader:
            content = [element + ";" for element in row if element]
            content = "".join(content)
            content = content.split(";")
            if GET_ELEMENT_PEER_POSITION:
                for position in GET_ELEMENT_PEER_POSITION:
                    file_rows.append(content[position])
            else:
                file_rows.append(content)
    return file_rows


def write_file_csv(file_name: str, content: List[str]):
    with open(file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for row in content:
            spamwriter.writerow(row)


if __name__ == '__main__':
    content_file = open_file_csv(FILE_PATH_IN)
    write_file_csv(FILE_PATH_OUT, content_file)
