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
from health_assessment import Health_Assessment
from ketone import Ketone
from change_avt import Change_avt
from edit_profile import Edit_profile
from quit_smoke import Quit_smoke
from share_data import Share_data

desired_caps = dict(
    platformName='Android',
    deviceName='Galaxy A6',
    platformVersion='8.0.0',
    automationName='UiAutomator2',
    # app='C:\\Users\\tramp\\Downloads\\vitalgain.jp_24.04.15_240415.apk',
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

# time.sleep(10)
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
# # weight
# weight = Weight(driver)
# weight.weight()
# # weight
# # water
# water = Water(driver)
# water.water()
# # water
# # nutrition
# nutrition = Nutrition(driver)
# nutrition.nutrition()
# # nutrition
# # blood pressure
# bpressure = BloodPressure(driver)
# bpressure.bloodPressure()
# # blood pressure
# # # Spo2
# # spo2 = SpO2(driver)
# # spo2.spo2()
# # # Spo2
# # grip strength
# grip = Grip(driver)
# grip.grip()
# # grip strength
# # ketone
# ketone = Ketone(driver)
# ketone.ketone()
# # ketone
# # glucose
# glu = Glucose(driver)
# glu.glucose()
# # glucose
# # quit smoking
# quits = Quit_smoke(driver)
# quits.quit_smoke()
# # quit smoking
# # # age_recognition
# # aRecognition = Age_Recognition(driver)
# # aRecognition.age_recognition()
# # aRecognition.select_photo()
# # time.sleep(3)
# # aRecognition.take_a_picture()
# # # age_recognition
#
# # share_data
# share = Share_data(driver)
# share.share_data()
# # share_data

# # health_assessment
# health = Health_Assessment(driver)
# health.health_assessment()
# # health_assessment
# # logout
# logout = Logout(driver)
# logout.logout()
# # logout
# # register
# register = Register(driver)
# register.register()
# # register
# # change_avt
# change = Change_avt(driver)
# change.change_avt()
# # change_avt
# time.sleep(3)

# edit profile
editpr = Edit_profile(driver)
editpr.edit_profile()
# edit profile

# # connect health source
# connect = Connection(driver)
# connect.connection()
# # connect health source
# dashboard_setting
# db_setting = Dashboard_setting(driver)
# db_setting.dashboard_setting()
# dashboard_setting
