import json
from Consumer import consumer
from Consumer import postgresDB
import psycopg2

conn = postgresDB.getconnection()
if conn:
    print("CONNECTION")


def deserializer(data):
    return json.loads(data.decode("utf-8"))


def insertDB(item):

    itemid = item.get("id")
    first_name = item.get("first_name")
    last_name = item.get("last_name")
    gender = item.get("gender")
    dob = item.get("date_of_birth")
    uni = item.get("university")

    query = (f"INSERT INTO persons(id, first_name, last_name, gender, date_of_birth, university)"
             f"VALUES ({itemid}, '{first_name}', '{last_name}',"
             f"'{gender}', '{dob}', '{uni}')")

    try:
        curs = conn.cursor()
        curs.execute(query)
        conn.commit()
        print("ITEM added successfully!")

    except psycopg2.ProgrammingError as syntax_err:
        print(syntax_err)
        curs.execute("ROLLBACK")

    finally:
        curs.close()


if conn:
    for msg in consumer:
        message = deserializer(msg.value)
        insertDB(message)
