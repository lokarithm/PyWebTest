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
                json_array = json.load(json_file)
                configurations = []

                for item in json_array:
                    url = item['url']
                    user = User(item['user']['username'],
                                item['user']['password'])
                    testCase = item['test_case']

                    configuration = Configuration(url)
                    configuration.user = user
                    configuration.testCase = testCase

                    configurations.append(configuration)
                return configurations
        except FileNotFoundError:
            print(
                f'ConfigurationManager - Error: file {self.fileName} is not found!')
