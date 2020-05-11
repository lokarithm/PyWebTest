from .user import User


class Configuration:
    def __init__(self, url):
        self.url = url
        self._user = None

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user
