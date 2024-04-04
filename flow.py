from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import AppiumOptions
from login import Login
from age_recognition import Age_Recognition
from scroll import Scroll

desired_caps = dict(
    platformName='Android',
    deviceName='Galaxy A6',
    platformVersion='8.0.0',
    automationName='UiAutomator2',
    # app='C:\\Users\\tramp\\Downloads\\vitalgain.jp_24.04.02_240402.apk',
    appActivity='com.genkimiru.app.presentation.splash.SplashActivity',
    # appActivity='VitalGain',
    appPackage='vitalgain.jp',
)
appium_option = AppiumOptions()
appium_option.load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_option)
driver.implicitly_wait(2)
#
scroll = Scroll(driver)
login = Login(driver)
login.login()
aRecognition = Age_Recognition(driver)
aRecognition.age_recognition()
aRecognition.select_photo()
