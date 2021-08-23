from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    def __init__(self, window_size='1920x1480'):
        self.window_size = window_size

    def initializeChromeDriver(self, is_headless=False):
        chrome_options = self.setupChromeBrowserOptions(is_headless)
        return webdriver.Chrome(chrome_options=chrome_options)

    def setupChromeBrowserOptions(self, is_headless):
        chrome_options = webdriver.ChromeOptions()

        ua = UserAgent()
        userAgent = ua.random
        print("userAgent", userAgent)
        chrome_options.add_argument(f'user-agent={userAgent}')
        # Chrome arguments
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--enable-javascript")
        chrome_options.add_argument("--js-flags=--harmony")

        chrome_options.add_argument('--enable-audio-service-sandbox')
        chrome_options.add_argument('--flag-switches-begin')
        chrome_options.add_argument('--flag-switches-end')
        chrome_options.add_argument('--lang=en')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size='+self.window_size)
        chrome_options.add_experimental_option("detach", True)

        if is_headless:
            chrome_options.add_argument('--headless')

        return chrome_options
