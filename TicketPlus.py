import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://ticketplus.com.tw/order/05c28296f9416bd4e768cac32e8baaa9/970b2bcbca7e04910154fb688e0550cd" #輸入網址

BrowserCount = 2    #輸入瀏覽器數

Account = ""      #輸入帳號
Password = ""    #輸入密碼

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # 最大化視窗
    prefs = {"profile.managed_default_content_settings.images": 2}  # 不載入圖片
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def auto_ticket(driver):
    wait = WebDriverWait(driver, 10)
    waitbtn = WebDriverWait(driver, 1)
    try:
        # 區域
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[1]//div[1]/button[@class='v-expansion-panel-header']")))
        testbutton = driver.find_element(By.XPATH, "//div[1]//div[1]/button[@class='v-expansion-panel-header']")
        testbutton.send_keys(Keys.RETURN)

        # 自動刷新
        while True:
            try:
                # 張數            
                waitbtn.until(EC.presence_of_element_located((By.XPATH, "//div[2]/div/button[2]")))
                plusbutton = driver.find_element(By.XPATH, "//div[2]/div/button[2]")
                plusbutton.click()

                # 下一步
                nextStep = driver.find_element(By.XPATH, "//button/span[contains(text(), '下一步')]")
                nextStep.click()
                print("搶票中!!!")
            except Exception as e:
                wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '更新票數')]")))
                button = driver.find_element(By.XPATH, "//span[contains(text(), '更新票數')]")
                driver.execute_script("arguments[0].click();", button)
                print("刷新!!!")
    except:
        print("❌ 發生錯誤，重新執行搶票")
        auto_ticket(driver)

def TicketPlus(driver):
    wait = WebDriverWait(driver, 10)
    try:
        # 自動確認
        # subbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '確定')]")))
        # driver.execute_script("arguments[0].click();", subbutton)

        # 自動登入
        wait.until(EC.presence_of_element_located((By.ID, "MazPhoneNumberInput-20_phone_number")))
        phone_input = driver.find_element(By.ID, "MazPhoneNumberInput-20_phone_number")
        phone_input.clear()  # 清除舊值
        phone_input.send_keys(Account)

        pw_input = driver.find_element(By.ID, "input-26")
        pw_input.clear()  # 清除舊值
        pw_input.send_keys(Password)
        pw_input.send_keys(Keys.RETURN)

        auto_ticket(driver)
    except Exception as e:
        print("❌ 發生錯誤，重新執行登入")
        TicketPlus(driver)
    finally:
        input("按 Enter 鍵關閉瀏覽器...")
        driver.quit()

def run_ticketplus_instance():
    driver = setup_driver()
    driver.get(URL)
    TicketPlus(driver)

if __name__ == '__main__':
    threads = []
    
    for i in range(BrowserCount):# 同時開啟i個瀏覽器
        t = threading.Thread(target=run_ticketplus_instance)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
