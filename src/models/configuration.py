from .user import User


class Configuration:
    def __init__(self, url):
        self.url = url
        self._user = None
        self._testCase = None
        self._is_headless = False

    @property
    def is_headless(self):
        return self._is_headless

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

    @is_headless.setter
    def is_headless(self, is_headless):
        self._is_headless = is_headless
