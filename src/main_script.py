from selenium import webdriver

from configuration_manager import ConfigurationManager
from managers.test_manager import TestManager


def main():
    # Initialize configuration
    configurationManager = ConfigurationManager()
    configurations = configurationManager.initialize()
    
    testManager = TestManager(configurations)
    testManager.run_test()


if __name__ == "__main__":
    main()
