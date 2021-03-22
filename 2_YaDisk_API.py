import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        url = 'https://cloud-api.yandex.net/'
        version = 'v1/'
        path = 'disk/'
        url_full = url + version + path
        method_upl_req = 'resources/upload'
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'OAuth ' + self.token}
        params = {'path': 'disk:/text.txt'}

        upload_get = requests.get(url_full + method_upl_req, params=params, headers=headers)
        if upload_get.status_code // 100 == 4:
            return 'Ошибка'
        else:
            with open(file_path, 'rb') as f:
                upload_put = requests.put(upload_get.json().get('href'), files={'file': f})
            if upload_put.status_code // 100 == 4:
                return 'Ошибка'
            else:
                return 'Файл успешно загружен'

if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload(r"C:\Users\SESAK\Desktop\Projects\API\text.txt")
    print(result)