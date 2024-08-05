import chromedriver_autoinstaller
import pytesseract
from PIL import Image
import os
import time
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from input_data_model import InputDataModel
from selenium.webdriver.chrome.options import Options



path = r""

img = Image.open(path)
text = pytesseract.image_to_string(img)
result = text.strip()


