from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.add_argument("user-data-dir=C:\\Users\\khali\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directory=Profile 1")

PATH = r"C:\Users\khali\OneDrive\Desktop\FollowerTracker\chromedriver_win32\chromedriver.exe"
service = Service(executable_path=PATH)


def get_html(link):
    browser = webdriver.Chrome(service=service, options=options)
    browser.get(link)
    html = browser.page_source
    time.sleep(2)
    browser.quit()
    
    return html
