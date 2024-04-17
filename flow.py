import time
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from login import Login
from age_recognition import Age_Recognition
from connect_healthsource import Connection
from step import Step
from dashboard_settings import Dashboard_setting
from sleep import Sleep
from weight import Weight
from nutrition import Nutrition
from grip import Grip
from blood_presure import BloodPressure
from spo2 import SpO2
from glucose import Glucose
from water import Water
from logout import Logout
from register import Register

desired_caps = dict(
    platformName='Android',
    deviceName='Galaxy A6',
    platformVersion='8.0.0',
    automationName='UiAutomator2',
    # app='C:\\Users\\tramp\\Downloads\\vitalgain.jp_24.04.03_240403.apk',
    appActivity='com.genkimiru.app.presentation.splash.SplashActivity',
    # appActivity='VitalGain',
    appPackage='vitalgain.jp',
    # language='ja-JP'
)
appium_option = AppiumOptions()
appium_option.load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=appium_option)
driver.implicitly_wait(3)
# language = driver.execute_script('mobile: shell', {'command': 'getprop persist.sys.locale'})
# print("Language:", language)

# # connect_database
# conn = psycopg2.connect(
#     user="genki_dev",
#     password="genkipw123456",
#     database="genki",
#     host="stg-db.genkimiru.jp",
#     port="5432"
# )
# cur = conn.cursor()
# cur.execute(
#     "SELECT user_id, total_sleep_time, deep, light, rem , wake FROM user_health_source_sleep_history WHERE user_id = '1482' AND start_date = '2024-01-24 00:00:00' ")
# rows = cur.fetchall()
# print(type(rows))
# print(rows)
#
# for row in rows:
#     print(row)
#     print("Total", row[1])
# cur.close()
# conn.close()
# # connect_database

# login
login = Login(driver)
login.login()
# login

# # nutrition
# nutrition = Nutrition(driver)
# nutrition.nutrition()
# # nutrition
# time.sleep(3)
# driver.back()
# time.sleep(3)
# # blood pressure
# bpressure = BloodPressure(driver)
# bpressure.bloodPressure()
# # blood pressure
# # driver.back()
# time.sleep(3)
# # Spo2
# spo2 = SpO2(driver)
# spo2.spo2()
# # Spo2
# # driver.back()
# # time.sleep(3)
# # step
# step = Step(driver)
# step.step()
# # step
# driver.back()
# time.sleep(3)
# # sleep
# sleep = Sleep(driver)
# sleep.sleep()
# # sleep
# driver.back()
# time.sleep(3)
# # glucose
# glu = Glucose(driver)
# glu.glucose()
# # glucose
# # driver.back()
# # time.sleep(3)
# # age_recognition
# aRecognition = Age_Recognition(driver)
# aRecognition.age_recognition()
# aRecognition.select_photo()
# time.sleep(3)
# aRecognition.take_a_picture()
# # age_recognition
# driver.back()
# time.sleep(3)
# # weight
# weight = Weight(driver)
# weight.weight()
# # weight
# # driver.back()
# # time.sleep(3)
# # grip strength
# grip = Grip(driver)
# grip.grip()
# # grip strength
# # driver.back()
# # time.sleep(3)

# water
water = Water(driver)
water.water()
# water
# logout
logout = Logout(driver)
logout.logout()
# logout

# register
register = Register(driver)
register.register()
# register

# connect health source
# connect = Connection(driver)
# connect.connection()
# connect health source


# dashboard_setting
# db_setting = Dashboard_setting(driver)
# db_setting.dashboard_setting()
# dashboard_setting
