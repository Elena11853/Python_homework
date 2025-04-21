from db_connector import DBConnector

# подставьте свои значения
user = 
password =  
host = 'localhost'
port = '5432'
db = 'QA'

def test_database_operations():
    db_connector = DBConnector(user, password, host, port, db)

    # Проверяем что строка таблицы пустая до начала теста
    testing_row_title = db_connector.select()

    assert testing_row_title is None, "Строка должна быть пустая на начало теста"

    # Проверяем что корректно вставляются значения
    db_connector.insert('insert')
    testing_row_title = db_connector.select()

    assert testing_row_title == 'insert', "Поле title должно содержать текст 'insert' после добавления строки"

    # Проверяем что корректно обновляются значения
    db_connector.update('update')
    testing_row_title = db_connector.select()

    assert testing_row_title == 'update', "Поле title должно содержать текст 'uppdate' после обновления строки"

    # Проверяем что корректно удаляются значения
    db_connector.delete()
    testing_row_title = db_connector.select()
    
    assert testing_row_title is None, "Строка должна быть пустая после удаления"