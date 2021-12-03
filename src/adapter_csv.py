import csv
import config
import str_utils
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
                    index = config.GET_ELEMENT_PEER_POSITION[0]
                    if str_utils.find_regex(row[index], config.HAS_SQL) or str_utils.find_regex(row[index],
                                                                                                config.REGEX_FARMS_ID):
                        if str_utils.find_regex(row[index], config.REGEX_FARMS_ID):
                            str_utils.apply_regex(row[index])
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
