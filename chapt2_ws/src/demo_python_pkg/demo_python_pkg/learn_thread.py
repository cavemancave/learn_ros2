import threading
import requests

class Download:
    def download(self, url, callback_world_count):
        print(f"thread Id:{threading.get_ident()}: Start download {url}")
        response = requests.get(url)
        response.encoding = 'utf-8'
        callback_world_count(url, response.text)

    def start_download(self, url, callback_world_count):
        thread= threading.Thread(target=self.download, args=(url, callback_world_count))
        thread.start()

def world_count(url, result):
    print(f"{url}:{len(result)}->{result[:5]}")

def main():
    download = Download()
    download.start_download('http://0.0.0.0:8000/novel1.txt', world_count)
    download.start_download('http://0.0.0.0:8000/novel2.txt', world_count)
    download.start_download('http://0.0.0.0:8000/novel3.txt', world_count)