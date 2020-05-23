from .user import User


class Configuration:
    def __init__(self, url):
        self.url = url
        self._user = None
        self._testCase = None

    @property
    def testCase(self):
        return self._testCase

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @testCase.setter
    def testCase(self, testCase):
        self._testCase = testCase
