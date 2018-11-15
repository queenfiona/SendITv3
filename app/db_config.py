"""Docstring for db_config file."""
import psycopg2

url = "host = localhost dbname = sendit user = app password = app"


def connection(url):
    """Docstring for connection method."""
    connection_to_db = psycopg2.connect(url)
    return connection_to_db


def init_db():
    """Docstring for init_db method."""
    connection_to_db = psycopg2.connect(url)
    return connection_to_db


def tables():
    """Docstring for tables method."""
    orders = """CREATE TABLE IF NOT EXISTS orders(
    parcel_id serial PRIMARY KEY,
    username CHARACTER VARYING(200) NOT NULL,
    item_shipped CHARACTER VARYING(200) NOT NULL,
    origin CHARACTER VARYING(200) NOT NULL,
    destination CHARACTER VARYING(200) NOT NULL,
    weight serial NOT NULL,
    status CHARACTER VARYING(200) NOT NULL);"""
    query = [orders]
    return query


def create_tables():
    """Docstring for create_tables method."""
    tables_to_create = tables()
    connection_to_db = connection(url)
    cursor = connection_to_db.cursor()
    for table in tables_to_create:
        cursor.execute(table)
    connection_to_db.commit()


def destroy_tables():
    """Docstring for destroy tables method."""
    connection_to_db = connection(url)
    cursor = connection_to_db.cursor()
    drop_orders = """DROP TABLE IF EXISTS orders CASCADE"""
    queries = [drop_orders]
    for table_to_drop in queries:
        cursor.execute(table_to_drop)
    connection_to_db.commit()
