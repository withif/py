import time

from selenium.webdriver.common.by import By


#登录前提
def entry_Prerequisite(username,password,browser,url):
    browser.get(url)
    username_input = browser.find_element('id', 'username')
    password_input = browser.find_element('id', 'password')
    submit_button = browser.find_element('id', 'login_btn')
    username_input.send_keys(username)
    password_input.send_keys(password)
    submit_button.click()
    time.sleep(1)

#进入银行卡管理
def enter_B_C_M(browser):
    gerenzhongxin = browser.find_element(By.XPATH, "//*[contains(@class, 'mdi mdi-account-location')]")
    # 获取 <i> 元素后面的文本
    parent_element = gerenzhongxin.find_element(By.XPATH, '..')
    parent_element2 = parent_element.find_element(By.XPATH, '..')  # 获取到a标签
    parent_element2.click()
    time.sleep(1)
    # 使用 XPath 定位包含特定 href 属性的 <a> 元素
    href_value = "/user/personal/toBankCard.html"  # 替换成你要查找的 href 值
    a_element = browser.find_element(By.XPATH, f"//a[@href='{href_value}']")
    a_element.click()
    time.sleep(1)