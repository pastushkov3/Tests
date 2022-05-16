import  requests

token = 'AQAAAAAJicrsAADLW3WYB5818EMholz6BfhXEI4'

def create_folder(name_folder):
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
            }
    params = {'path': f'/{name_folder}/'}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code

def search_folder(name_folder):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    params = {'path': f'/{name_folder}/'}
    response = requests.get(url, headers=headers, params=params)
    return response.status_code

search_folder('test')