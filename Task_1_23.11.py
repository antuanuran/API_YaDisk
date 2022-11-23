import requests
import yadisk

# Класс для загрузки файла на Яндекс Диск
class Load_yadisk:

    # передача токена, заголовков согласно документации Яндекс Апи: https://yandex.ru/dev/disk/api/concepts/quickstart.html и URL для GET-запроса
    def __init__(self, token):
        self.token = token
        self.headers = {
                        'Content-Type': 'application/json',
                        'Authorization': f'{self.token}'
                       }
        self.url_get = 'https://cloud-api.yandex.net/v1/disk/resources/upload'


    # метод для получения временной защитной ссылки URL на загрузку файла. Получаем в ответе временную URL по ключу 'href'
    def get_link(self, file_name):
        params =      {
                        'path': file_name,
                        'overwrite': 'true'                     """данный параметр необходим если файл уже есть на диске"""
                      }
        response = requests.get(self.url_get, headers=self.headers, params=params).json()
        return response['href']


    # Метод загружает файлы  на яндекс диск
    def upload(self, disk_n, file_n):
        href = self.get_link(disk_n)
        requests.put(href, data=open(file_n, 'rb'))

if __name__ == '__main__':
    name_disk = 'file_disk.pdf'
    name_file = 'file_load.pdf'
    token_str = '***********************ССЫЛКА_НА_ТОКЕН'

    loader = Load_yadisk(token_str)
    loader.upload(name_disk, name_file)







