import time
from sql_queries import create_table, check_object_is_full
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        check_object_is_full(conn)
        print("updated")
        time.sleep(5)