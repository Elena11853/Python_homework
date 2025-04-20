from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:Beklin@localhost:5432/QA"

def test_insert():
    db = create_engine(db_connection_string)
    connection = db.connect()
    sql_query = text("INSERT INTO subject (subject_title, subject_id) VALUES (:subject_title, :id)")
    #rows = db.execute(sql, title = 'Russian checkers', id =17)
    connection.execute(sql_query, {subject_title:'Test', id: 17 })

#sql = text("insert into company(\"name\") values (:new_name)")

def test_update():
    db = create_engine(db_connection_string)
    connection = db.connect()
    sql_query = text("update subject set subject_title = 'Stavropol checkers' where subject_id = 17")
    connection.execute(sql_query)


def test_delete():
    db = create_engine(db_connection_string)
    connection = db.connect()
    sql_query = text("delete from subject  where subject_id = 17")
    connection.execute(sql_query)


def test_insert():
    db = create_engine(db_connection_string)
    connection = db.connect()
    try:
        # Вставка записи
        sql_query = text("INSERT INTO subject (subject_title, subject_id) VALUES ('Russian checkers', 17);")
        connection.execute(sql_query)

        # Выборка свежей записи из базы данных
        select_query = text("SELECT * FROM subject WHERE subject_title = 'Russian checkers';")
        result = connection.execute(select_query).fetchone()

        # Проверка существования записи
        assert result is not None, "Запись не найдена!"
        assert result['subject_title'] == 'Russian checkers', "Название компании неверное!"
    except Exception as e:
        print(f"Ошибка: {e}")

def test_update():
    db = create_engine(db_connection_string)
    connection = db.connect()
    try:
        # Проверка, что такая запись существует до обновления
        select_initial_query = text("SELECT * FROM subject WHERE subject_id = 17;")
        initial_record = connection.execute(select_initial_query).fetchone()
        assert initial_record is not None, "Запись с данным ID не найдена!"
        assert initial_record["subject_title"] != "Stavropol checkers", "Название уже равно новому значению!"

        # Обновление записи
        update_query = text("UPDATE subject SET subject_title = 'Stavropol checkers' WHERE subject_id = 17;")
        connection.execute(update_query)

        # Проверка, что запись изменилась
        select_updated_query = text("SELECT * FROM subject WHERE subject_id = 17;")
        updated_record = connection.execute(select_updated_query).fetchone()
        assert updated_record is not None, "Обновленная запись не найдена!"
        assert updated_record["subject_title"] == "Stavropol checkers", "Новое название не совпадает с ожиданием!"
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        connection.close()

def test_delete():
    db = create_engine(db_connection_string)
    connection = db.connect()
    try:
        # Шаг 1: Проверяем, что запись с subject_id = 17 существует ДО удаления
        before_delete_query = text("SELECT COUNT(*) FROM subject WHERE subject_id = 17;")
        record_count_before = connection.execute(before_delete_query).scalar()
        assert record_count_before > 0, "Запись с subject_id = 17 отсутствует перед удалением."

        # Шаг 2: Выполнение удаления
        delete_query = text("DELETE FROM subject WHERE subject_id = 17;")
        connection.execute(delete_query)

        # Шаг 3: Проверяем, что запись была удалена ПОСЛЕ удаления
        after_delete_query = text("SELECT COUNT(*) FROM subject WHERE subject_id = 17;")
        record_count_after = connection.execute(after_delete_query).scalar()
        assert record_count_after == 0, "Запись с subject_id = 17 осталась после удаления."
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        connection.close()


