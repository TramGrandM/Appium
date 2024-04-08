import time

import psycopg2
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from login import Login
from age_recognition import Age_Recognition
from scroll import Scroll
from connect_healthsource import Connection
from step import Step
from dashboard_settings import Dashboard_setting
# from connect_db import Connect_db
from sleep import Sleep

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

# connect_database
conn = psycopg2.connect(
    user="genki_dev",
    password="genkipw123456",
    database="genki",
    host="stg-db.genkimiru.jp",
    port="5432"
)
cur = conn.cursor()
cur.execute(
    "SELECT user_id, total_sleep_time, deep, light, rem , wake FROM user_health_source_sleep_history WHERE user_id = '1482' AND start_date = '2024-01-24 00:00:00' ")
rows = cur.fetchall()
print(type(rows))
print(rows)

for row in rows:
    print(row)
    print("Total", row[1])
cur.close()
conn.close()
# connect_database

# scroll
scroll = Scroll(driver)
# scroll

# login
login = Login(driver)
login.login()
# login
# step
step = Step(driver)
step.step()
# step
driver.back()
time.sleep(3)
# sleep
sleep = Sleep(driver)
sleep.sleep()
# sleep



# age_recognition
# aRecognition = Age_Recognition(driver)
#
# aRecognition.age_recognition()
# # aRecognition.select_photo()
# aRecognition.take_a_picture()
# age_recognition
#
# driver.back()

# connect_db
# connectdb = Connect_db(driver)
# connectdb.connect_db()
# connect_db

# connect health source
# connect = Connection(driver)
# connect.connection()
# connect health source



# dashboard_setting
# db_setting = Dashboard_setting(driver)
# db_setting.dashboard_setting()
# dashboard_setting
