from sqlalchemy import create_engine
from object import Object
from sql_queries import insert_object, create_table, set_object_top_level, check_object_is_full, get_objects


def test_service1(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    object = Object(
        name = "test_name",
        capacity = 48,
        amount_of_people = 26,
        is_full = 0,
        top_level = 1,
        likes = 73,
    )
    insert_object(conn, object)

    objects_lst = get_objects(conn)
    assert len(objects_lst) == 4
    last_object = objects_lst[-1]
    assert last_object.name == "test_name"

def test_service3(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    set_object_top_level(conn,level_value=2, object_id=0)
    object = get_objects(conn)
    assert object[0].top_level == 2
    engine.dispose(conn_with_data)

def test_service2(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    check_object_is_full(conn)
    object = get_objects(conn)
    assert object[0].is_full == 0
    engine.dispose(conn_with_data)






