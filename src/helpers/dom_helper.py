import time
import helpers.print_helper as ph

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import ElementNotInteractableException


class DomHelper:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_css_selector(self, selector, retry_num=3, retry_time_interval=2):
        try:
            dom = self.driver.find_element_by_css_selector(selector)
            return dom
        except NoSuchElementException:
            print(f"Selector: {selector} does NOT exist")
            if retry_time_interval > 0:
                ph.countDown("Retry", retry_time_interval-1)
                self.find_element_by_css_selector(selector)
            return None

    def find_elements_by_css_selector(self, selector, retry_num=3, retry_time_interval=2):
        try:
            dom = self.driver.find_elements_by_css_selector(selector)
            return dom
        except NoSuchElementException:
            print(f"Selector: {selector} does NOT exist")
            if retry_time_interval > 0:
                ph.countDown("Retry", retry_time_interval-1)
                self.find_elements_by_css_selector(selector)
            return None

    def find_element_by_id(self, selector, retry_num=3, retry_time_interval=2):
        try:
            dom = self.driver.find_element_by_id(selector)
            return dom
        except NoSuchElementException:
            print(f"Selector: {selector} does NOT exist")
            if retry_time_interval > 0:
                ph.countDown("Retry", retry_time_interval-1)
                self.find_element_by_id(selector)
            return None

    def find_element_by_class_name(self, selector, retry_num=3, retry_time_interval=2):
        try:
            dom = self.driver.find_element_by_class_name(selector)
            return dom
        except NoSuchElementException:
            print(f"Selector: {selector} does NOT exist")
            if retry_time_interval > 0:
                ph.countDown("Retry", retry_time_interval-1)
                self.find_element_by_class_name(selector)
            return None
