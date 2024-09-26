from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException

def search(user):
    driver = webdriver.Chrome()
    # 開啟目標網站
    driver.get("https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do")  # 將此網址換成你的目標網站
    driver.maximize_window()
    # 使用 class 屬性查找輸入框
    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
    )
    #輸入使用者資料
    input_box.send_keys(user)
    # 查找具有 class="btn btn-primary" 的按鈕
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
    )
    # 點擊按鈕
    button.click()
    try:
        link = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='舊版表格格式']"))
        )
        link.click()
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//td[@data-title='登記名稱']"))
        )
        # 打印內容
        print(element.text)
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//td[@data-title='登記現況']"))
        )
        print(element.text)
        driver.quit
    except TimeoutException:
        # 捕捉到 TimeoutException 時執行的代碼
        print("查無此公司")
#user = input("請輸入統一編號:")
user = "1231211"
if len(user)!=8:
    print("請輸入八位數")
else:
    search(user)