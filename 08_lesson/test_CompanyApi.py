import requests

class CompanyApi:
    def __init__(self, url) -> None:
        self.url = url

    #my_company_id = 'fcfc8fc7-77eb-4b3f-9c08-84b7323c02ae'

    def get_a_list(self, my_login, my_password):
        creds = {
            'login': my_login('text'),
            'password': my_password,
        }
        resp = requests.post(self.url + '/api-v2/auth/companies', json=creds)
        my_company_id= resp.json()["id"]
        return my_company_id()

    # Получить токен авторизации
    def authorization_key(self, my_login, my_password, my_company_id):
        creds = {
            'login': my_login,
            'password': my_password,
            'companyId': my_company_id
            }
        resp = requests.post(self.url + '/api-v2/auth/keys/get', json=creds)
        Bearer = resp.json()["key"]
        return Bearer()

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
       
    


