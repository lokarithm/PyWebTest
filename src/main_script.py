from selenium import webdriver

from configurations.driver import Driver
from configuration_manager import ConfigurationManager
from managers.test_manager import TestManager


def main():
    # Initialize configuration
    configurationManager = ConfigurationManager()
    configuration = configurationManager.initialize()
    driver = Driver()
    testManager = TestManager(driver)


if __name__ == "__main__":
    main()
