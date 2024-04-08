import time


class Scroll:
    def __init__(self, driver):
        self.driver = driver

    def scroll(self):
        device_size = self.driver.get_window_size()
        start_x = device_size['width'] / 2
        start_y = device_size['height'] * 0.3
        end_x = device_size['width'] / 2
        end_y = device_size['height'] * 0.65
        self.driver.swipe(start_y, end_y, start_x, end_x)
