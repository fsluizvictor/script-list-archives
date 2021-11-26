import sqlite3
from sqlite3 import Cursor, Connection
from typing import List

import config


def create_connection(file_path: str) -> (Connection, Cursor):
    con = sqlite3.connect(file_path)
    cur = con.cursor()
    return con, cur


def create_table(cur: Cursor, table_name: str):
    cur.execute(f"create table {table_name} (path, size)")


def insert_items(cur: Cursor, values: List[List[str]], table_name: str):
    for value in values:
        cur.executemany(f"insert into {table_name} values (?,?)", (value,))


def finish_persistence_process(con: Connection):
    con.commit()
    con.close()
