import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from model_data_in import *
from selenium.webdriver.common.by import By
import time
import random
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys


def get_init_driver() -> WebDriver:
    # driver = Driver(uc=True)
    driver = webdriver.Chrome()
    time.sleep(0.5)
    # driver.maximize_window()
    driver.set_window_size(900, 900)
    time.sleep(0.5)
    return driver


def wait_for_element(driver: WebDriver, x_path: str, max_wait_time_s: float):
    max_wait_time_s *= 100
    for time_s in range(1, int(max_wait_time_s), 1):
        try:
            driver.find_element(By.XPATH, x_path)
            return 0
        except:
            pass
        time.sleep(1 / 100)
    return 1


def main():
    data_model = DataModel()
    driver = get_init_driver()
    driver.get(data_model.url_start)
    time.sleep(1)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    total_s = end_time - start_time
    total_m = int(total_s / 60)
    total_s = int(total_s - total_m * 60)
    print(f"")
    print(f"#####################################")
    print(f"Total time: {total_m}m {total_s}s")
    print(f"#####################################")
