from sqlalchemy import text, create_engine

class DBConnector:
    def __init__(self, user: str, password: str, host: str, port: str, db: str):
        self.engine = create_engine('postgresql+psycopg2://'+user+':'+password+'@'+host+':'+port+'/'+db+'')
        self.connection = self.engine.connect()
        self._get_last_id()

    
    def _get_last_id(self):
        query = text('SELECT max(subject_id) FROM subject')

        res = self.connection.execute(query)
        for row in res:
            max_id = row[0] if row[0] else 0
            self.id = max_id + 1

    def select(self):      
        title: str | None = None

        query = text('SELECT subject_title FROM subject WHERE subject_id = :id')
        values = {'id': self.id}

        res = self.connection.execute(query, values)
        for row in res:
            if (row[0]):
                title = row[0]
        
        return title

    def insert(self, title="inserted_title"):      
        query = text('INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)')
        values = {'id': self.id, 'title': title}

        self.connection.execute(query, values)
        self.connection.commit()

    def update(self, title="updated_title"):
        query = text('UPDATE subject SET subject_title=:new_title WHERE subject_id = :id')
        values = {'id': self.id, 'new_title': title}

        self.connection.execute(query, values)
        self.connection.commit()

    def delete(self):
        query = text('DELETE FROM subject WHERE subject_id=:id')
        values = {'id': self.id}

        self.connection.execute(query, values)
        self.connection.commit()