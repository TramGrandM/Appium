import random
import time
from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find


class Register:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def register(self):
        register = self.driver.find_element(AppiumBy.XPATH,
                                            '//android.widget.Button[@resource-id="vitalgain.jp:id/activity_intro_register_btn"]')
        register.click()
        time.sleep(3)
        smartp = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/register_smartphone_device_tv')
        smartp.click()
        time.sleep(2)
        self.driver.tap([(350, 800)])
        skip = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/register_skip_button')
        skip.click()
        uname = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_account_username_edt"]')
        i = random.randint(1, 1000)
        uname.send_keys(f"autotest{i}")
        email = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_account_email_edt"]')
        email.send_keys(f"email{i}@gmail.com")
        passw = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_account_password_edt"]')
        passw.send_keys("12345678")
        fname = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_account_firstname_edt"]')
        fname.send_keys(f"fname{i}")
        lname = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_account_lastname_edt"]')
        lname.send_keys(f"lname{i}")
        next_btn = self.driver.find_element(AppiumBy.XPATH,
                                            '//android.widget.Button[@resource-id="vitalgain.jp:id/register_account_next_btn"]')
        next_btn.click()
        register_btn = self.driver.find_element(AppiumBy.XPATH,
                                                '//android.widget.Button[@resource-id="vitalgain.jp:id/register_account_complete_btn"]')
        register_btn.click()
        print("Register - Done!")
