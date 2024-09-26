from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from linebot import LineBotApi
from linebot.models import TextSendMessage

acToken = 'zzZxhNQcgLFKgGJnSTLxebqKWWlpTxMdCMhafgUZjk1t2EtbE9vNHU578lhbtPPTqcb4eSAmwtd1SOKd1pOXdzyK8zBiiWM6hx+9S5aZy1kDjjfaJ2Fabq20ripkSGLTd1Qi7KEhE0RDbAZweX+fnwdB04t89/1O/w1cDnyilFU='
userID = 'U41539f029351102369df316425003bbc'
def line_message(message):
    line_bot_api = LineBotApi(acToken)
    line_bot_api.push_message(userID, TextSendMessage(text=message))
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
        element1 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//td[@data-title='登記名稱']"))
        )
        # 打印內容
        element2 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//td[@data-title='登記現況']"))
        )
        message ="%s %s"%(element1.text,element2.text)
        print(message)
        driver.quit
        return message
    except TimeoutException:
        # 捕捉到 TimeoutException 時執行的代碼
        return "查無此公司"
user = input("請輸入統一編號:")
if len(user)!=8:
    print("請輸入八位數")
else:
    line_message(search(user))
    #search(user)