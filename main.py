import requests


class YaUploader:
    def __init__(self, token: str, url: str):
        self.token = token
        self.url = url

    def upload(self, file_path: str, disk_file_path):

        headers = {
            'Content-Type': 'image/jpg',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": disk_file_path, "overwrite": "true"}

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        response = requests.get(upload_url, headers=headers, params=params)

        link = response.json()
        href = link.get("href", "")

        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()

        if response.status_code == 201:
            print("успех")


if __name__ == '__main__':

    token = "AQAAAAAokS16AADLWxzgAUZKC0wAtGFUCLfEIkc"
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    path_to_file = "C:/Users/Igor/Downloads/1564314090_3.jpg"

    uploader = YaUploader(token, url)
    uploader.upload(path_to_file, "Загрузки")




