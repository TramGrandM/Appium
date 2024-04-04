import time


class ScrollTop:
    def __init__(self, driver):
        self.driver = driver

    def scroll_top(self):
        device_size = self.driver.get_window_size()
        start_x = device_size['width'] / 2
        start_y = device_size['height'] * 0.3
        end_x = device_size['width'] / 2
        end_y = device_size['height'] * 0.7
        self.driver.swipe(start_x, end_x, start_y, end_y)
