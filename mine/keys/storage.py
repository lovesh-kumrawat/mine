import os
from configparser import ConfigParser


@lambda iife: iife()
class Storage:

    name: str = "Key-Record"
    
    keys = None
    config_path: str = "mine/keys/config.ini"
    
    config = ConfigParser()
    config.read(config_path)
    
    @property
    def user_path(self) -> str:
        return self.config.get('USER', 'PATH').format(home=os.path.expanduser('~'))
    
    @user_path.setter
    def user_path(self, path: str) -> None:
        self.config.set('USER', 'PATH', path)
    
    @user_path.deleter
    def user_path(self) -> None:
        self.config.remove_option('USER', 'PATH')

    @staticmethod
    def save() -> None:
        
        with open(Storage.config_path, 'w') as fp:
            Storage.config.write(fp)
