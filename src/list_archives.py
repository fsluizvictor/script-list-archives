import subprocess
from datetime import datetime


def list_archives(file_name):
    with open(file_name, 'w') as f:
        process = subprocess.Popen(
            ['tarsnap', '--keyfile', '/Users/', '--list-archives'],
            stdout=f)
        process.communicate()
        print('Finished.')


def sort_archives(file_name):
    with open(file_name, 'r') as f:
        datetime_list = []
        for line in f.readlines():
            datetime_str = line[11:30]
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d_%H-%M-%S')
            datetime_list.append(datetime_object)
            datetime_sorted_list = sorted(datetime_list)
            print(f'{line.strip()};{datetime_object}')
        for datetime_object in datetime_sorted_list:
            print(datetime_object)


def list_archives_content(file_name, archive):
    with open(file_name, 'w') as f:
        process = subprocess.Popen(
            ['tarsnap', '-tv', '--keyfile', '/Users/', '-f',
             archive],
            stdout=f)
        process.communicate()
        print('Finished.')


if __name__ == '__main__':
    # file = 'archives_list.txt'
    # list_archives(file)
    # sort_archives(file)
    list_archives_content('striderlib_2020_03_13_21_15_01.txt', 'striderlib-2020-03-13_21-15-01')