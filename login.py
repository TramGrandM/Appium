import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        try:
            alert = self.driver.find_element(AppiumBy.ID, 'com.android.packageinstaller:id/permission_allow_button')
            alert.click()
            time.sleep(3)
            form = self.driver.find_element(AppiumBy.XPATH,
                                            '(//android.widget.LinearLayout[@resource-id="com.google.android.gms:id/container"])[2]')
            form.click()
            login_btn = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/activity_intro_log_in_btn')
            login_btn.click()
            username = self.driver.find_element(AppiumBy.ID, "vitalgain.jp:id/login_username_edt")
            username.send_keys("huyentram")
            password = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/login_password_edt')
            password.click()
            password.send_keys('12345678')
            self.driver.hide_keyboard()
            btn = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/login_btn')
            btn.click()
            time.sleep(10)
            alert_1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'vitalgain.jp:id/right_button')))
            if alert_1.is_displayed():
                alert_1.click()
            btn_ok = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'vitalgain.jp:id/left_button')))
            if btn_ok.is_displayed():
                btn_ok.click()
            # alert_1 = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/right_button')
            # alert_1.click()
            # time.sleep(3)
            # btn_ok = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/left_button')
            # btn_ok.click()
        except Exception as e:
            print('EX', e)
        finally:
            print('done')
