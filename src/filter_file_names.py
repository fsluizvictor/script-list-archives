from datetime import datetime

import config
import adapter_database
import adapter_csv


def process():
    start = datetime.now()

    archives = adapter_csv.list_files_directory()

    archives.remove("/Users/luizvictorsantos/SyngentaProjects/protector-backup/files/originals_2/.DS_Store")

    for archive in archives:
        print('open archive ', archive)
        content_file = adapter_csv.open_file_csv(archive)

        archive = archive.replace('/Users/luizvictorsantos/SyngentaProjects/protector-backup/files/originals_2/', '')
        file_path = config.FILE_PATH_OUT_TXT + archive
        print('new archive ', file_path)
        adapter_csv.write_file_csv(file_path.replace('.txt', '_path_size.txt'), content_file)

        file_path = config.FILE_PATH_OUT_SQLITE + archive
        print('new archive ', file_path)
        con, cur = adapter_database.create_connection(file_path.replace('.txt', '_path_size.db'))
        archive = archive.replace('.txt', '')
        archive = archive.replace('-', '')
        adapter_database.create_table(cur, archive)
        adapter_database.insert_items(cur, content_file, archive)
        adapter_database.finish_persistence_process(con)
    end = datetime.now()
    print(f"time in seconds to generate the archives: {(end - start).total_seconds()} ")


if __name__ == '__main__':
    process()
