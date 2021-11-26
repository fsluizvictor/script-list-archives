import sqlite3
from sqlite3 import Cursor, Connection
from typing import List

import config


def create_connection(file_path: str) -> (Connection, Cursor):
    con = sqlite3.connect(file_path)
    cur = con.cursor()
    return con, cur


def create_table(cur: Cursor):
    cur.execute('''
    CREATE TABLE info_archives (path text, size real)
    ''')


def insert_items(cur: Cursor, values: List[List[str]]):
    for value in values:
        cur.executemany(f"INSERT INTO info_archives VALUES (?,?)", value)


def finish_persistence_process(con: Connection):
    con.commit()
    con.close()
