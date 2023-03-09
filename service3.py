import time
from sql_queries import create_table, set_object_top_level, get_objects
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        objects = get_objects(conn)
        for object in objects:
            if object.likes > 20:
                set_object_top_level(1, object.id)
            else:
                set_object_top_level(2, object.id)
        print("updated")
        time.sleep(10)