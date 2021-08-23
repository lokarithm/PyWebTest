import calendar
import time

from calendar import monthrange
from datetime import datetime as dt

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configurations.driver import Driver
from helpers.dom_type import DomType
from helpers.dom_helper import DomHelper
from helpers.alert_helper import AlertHelper
from models.configuration import Configuration

class TestManager:
    def __init__(self, configurations):
        self.driver = driver = Driver()
        self.configurations = configurations

    def run_test(self):
        for config in self.configurations:
            driver = self.driver.initializeChromeDriver(config.is_headless)
            driver.get(config.url)
            driver.close()