import time
import random

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import proxy_util


def generate_random_numbers():
    random_numbers = [random.random() for _ in range(3)]
    return random_numbers


def cnt1(str_):
    num = 0
    elements = driver.find_elements(By.XPATH, f'{str_}')
    # print(elements)
    for element in elements:
        num += 1
    return num




# 显式等待页面加载完成
# wait = WebDriverWait(driver, 10)
# wait.until(EC.visibility_of_element_located((By.ID, "q1")))

while 1:



    # 打开浏览器并访问问卷星问卷链接
    driver = webdriver.Chrome()
    driver.get("https://www.wjx.cn/vm/mBCoTJp.aspx")

    chrome_options = Options()
    # 设置无头浏览器
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 滑块防止检测
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

    # 将webdriver属性置为undefined
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
                            })



    # 使用CSS 选择器定位输入框
    # input_box = driver.find_element(By.CSS_SELECTOR, "input[type='text'][id='q1']")
    # input_box.send_keys('电子商务')
    #
    # driver.find_element(By.XPATH, '//input[@id="q25"]').send_keys("根本不在意")
    # driver.find_element(By.XPATH, '//input[@id="q26"]').send_keys("不在意")
    for i in range(1, 44):

        num = cnt1(f'//div[@class="field ui-field-contain"][{i}]/div[@class="ui-controlgroup '
                   'column1"]/div[@class="ui-radio"]')
        if num:
            click_num = random.randint(1, num)

            driver.find_element(By.XPATH, f'//div[@class="field ui-field-contain"][{i}]/div[@class="ui-controlgroup '
                                          f'column1"]/div[@class="ui-radio"][{click_num}]').click()

        else:

            num = cnt1(f'//div[@class="field ui-field-contain"][{i}]/div[@class="ui-controlgroup '
                       'column1"]/div[@class="ui-checkbox"]')

            suiji = random.randint(1, num)
            if suiji == 1:
                suiji += 1

            for m in range(1, suiji):
                click_num = random.randint(1, num)
                try:
                    driver.find_element(By.XPATH,
                                        f'//div[@class="field ui-field-contain"][{i}]/div[@class="ui-controlgroup '
                                        f'column1"]/div[@class="ui-checkbox"][{click_num}]').click()
                except selenium.common.exceptions.NoSuchElementException:
                    continue

    driver.find_element(By.XPATH, '//div[@class="submitbtn mainBgColor"]').click()

    # time.sleep(2200)
    try:
        confirm = driver.find_element(By.XPATH, '//div[@class="rect-top"]')
        confirm.click()
        validation = driver.find_element(By.XPATH, '//div[@class="rect-top"]')
        validation.click()
    except selenium.common.exceptions.NoSuchElementException:
        continue

    time.sleep(1000)
    driver.quit()


