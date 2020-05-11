import os
import json

from models.configuration import Configuration
from models.user import User


class ConfigurationManager:
    def __init__(self, fileName='config.json'):
        self.fileName = fileName

    def initialize(self):
        try:
            with open(self.fileName, 'r') as json_file:
                data = json.load(json_file)
                url = data['url']
                user = User(data['user']['username'], data['user']['password'])

                configuration = Configuration(url)
                configuration.user = user

                return configuration
        except FileNotFoundError:
            print(
                f'ConfigurationManager - Error: file {self.fileName} is not found!')
