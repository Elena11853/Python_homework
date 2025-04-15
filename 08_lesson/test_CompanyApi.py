import requests

key = ''
Base_url = 'https://yougile.com'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + key
    }
id_project = ""

#позитивный (Создание проекта)
def test_creating_a_project_positive():
    body = {
        'title': 'Test1'
        }
    resp = requests.post(Base_url + '/api-v2/projects', json = body, headers = headers)
    assert resp.status_code == 201
#негативный тест(проект без названия)
def test_creating_a_project_negative():
    body = {
        'title': ''
        }
    resp = requests.post(Base_url + '/api-v2/projects', json=body, headers=headers)
    assert resp.status_code == 400

# позитивный (Получение по id)
def test_get_by_id_positive_positive():
    resp = requests.get(f"{Base_url}/api-v2/projects/{id_project}", headers = headers)
    assert resp.status_code == 200

# негативный (несуществующий id)
def test_get_by_id_negative():
    resp = requests.get(f"{Base_url}/api-v2/projects/{123}", headers=headers)
    assert resp.status_code == 404

# позитивный (Изменение проекта)
def test_changing_the_project_positive():
    body = {
    'title': 'to change'
    }
    resp = requests.put(f"{Base_url}/api-v2/projects/{id_project}", json = body, headers = headers)
    assert resp.status_code == 200

#негативный (метод post, вместо put)
def test_changing_the_project_negative():
    body = {
    'title': 'to change'
    }
    resp = requests.post(f"{Base_url}/api-v2/projects/{id_project}", json = body, headers = headers)
    assert resp.status_code == 404