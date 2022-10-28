import platform
import click
import requests
from excaption import NotValidURL
from access import github_access
from update import download, get_sys_info
import subprocess
from storge import Storage


class Github(Storage):
    def __init__(self, url):
        super().__init__()
        self.__url = self.url = url
        self.ext = None
        self.__app_list = list()
        self.name = url.split('/')[-1]
        self.__is_exists(url)


    @property
    def ext(self):
        return self.__ext


    @ext.setter
    def ext(self, value):
        self.__ext = value


    @property
    def url(self):
        return self.__url


    @url.setter
    def url(self, value):
        if isinstance(value, str):
            api_endpoint = f'https://api.github.com/repos/{value}/releases/latest'
            self.__url = api_endpoint
        else:
            raise NotValidURL(value)


    def get_latest_release(self) -> str:
        release = requests.get(self.url, headers=github_access())
        if release.status_code == 200:
            release = release.json()
            return release['assets_url']
        raise NotValidURL()


    def get_latest_assets(self) -> None:
        assets_url = self.get_latest_release()
        assets = requests.get(assets_url, headers=github_access())
        self.__app_list = assets.json()


    def find_app(self) -> dict:
        platform_info = get_sys_info()
        sys_type = '64' if platform_info.machine.lower().endswith('64') else '32'
        if platform.system().lower() == 'windows':
            for app in self.__app_list:
                if self.ext is not None:
                    if app['name'].endswith(self.ext):
                        return app
                if sys_type in app['name'] and app['name'].endswith('msi'):
                    return app


    def install(self):
        self.get_latest_assets()
        app = self.find_app()
        click.secho('🔽 Downloading', fg='yellow')
        download(app['browser_download_url'], app['name'])
        subprocess.check_call(f'{app["name"]}', shell=True, stdout=subprocess.DEVNULL)
        click.secho('🎉 Installed Success', fg='yellow')


    def __is_exists(self, url):
        doc_id = url.split('/')[0].lower()
        if self.is_exists(doc_id):
            return True
        return False


g = Github('PowerShell/powershell')