import requests

class CompanyApi:

    # Инициализация
    def __init__(self, url) -> None:
        self.url = url

    # Получить токен авторизации
    def authorization_key(self, login, password, company_id):
        creds = {
            'login': login,
            'password': password,
            'companyId': company_id
            }
        resp = requests.post(self.url + '/api-v2/auth/keys/get', json=creds)
        return resp.json()["key"]

    # Создание проекта
    def creating_a_project(self, title = 'text'):
        project = {
        'title': title    
        }
        resp = requests.post(self.url + '/api-v2/projects', json=project)
        id_project = resp.json()["id"]
        return id_project()
    
    #Получение по id
    def get_by_id(self):
        resp = requests.get(self.url + '/api-v2/projects/{id_project}, params=params_to_add')
        return resp.json()["id"]

    
    #Изменение проекта
    def changing_the_project(self, title = 'text'):
        modified_project = {
        'title': title
        }
        resp = requests.put(self.url + '/api-v2/projects/{id}', json = modified_project)
        return resp.json()["id"]
       
    


