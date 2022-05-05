import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str, host: str):
        self.token = token
        self.host = host

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_uploads_link(self,path):
        url = f'{self.host}/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        pprint(response.json())
        return response.json().get('href')




    def upload(self, file_path: str,file_name: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_link = self.get_uploads_link(file_path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        return response.status_code


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    HOST = 'https://cloud-api.yandex.net:443'
    path_to_file = '/main2.py'
    token = 'AQAAAAA6V87mAADLW1dKDlEyvUKgtP9prsHI_TY'
    uploader = YaUploader(token, HOST)
    result = uploader.upload(path_to_file, 'main2.py')
    print(result)