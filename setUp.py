from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions


class SetUp:
    def __init__(self):
        self.desired_caps = None

    def setup(self):
        self.desired_caps = dict(
            platformName='Android',
            deviceName='Galaxy A6',
            platformVersion='8.0.0',
            automationName='UiAutomator2',
            app='C:\\Users\\tramp\\Downloads\\vitalgain.jp_24.03.12_240312.apk',
            appActivity='com.genkimiru.app.presentation.splash.SplashActivity',
            appPackage='vitalgain.jp'
        )

        # appium_option = AppiumOptions()
        # appium_option.load_capabilities(self.desired_caps)
        # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_option)
        # driver.implicitly_wait(2)

        return self.desired_caps

