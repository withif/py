from telnetlib import EC
import pandas as pd
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains

import gongnen
from selenium.webdriver.support import expected_conditions as EC
import pymysql
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import  time

from selenium.webdriver.support.wait import WebDriverWait

import shujuku
class Test_Web:

    data1 = pd.read_excel("C:/Users/36017/Desktop/2.xlsx", sheet_name='Sheet1')


    # @pytest.fixture(params=['firefox', 'chrome'])
    # def browser(self,request):
    #     browser_name = request.param        #request.param 获取了 params 列表中的每个值，这些值会按顺序提供给 fixture，然后用于执行测试。
    #     if browser_name == 'firefox':
    #         driver = webdriver.Firefox()
    #     elif browser_name == 'chrome':
    #         driver = webdriver.Chrome()
    #     else:
    #         print("错误")
    #         return
    #     yield driver
    #
    #     driver.quit()

    @pytest.fixture
    def browser(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    #登录
    @pytest.mark.parametrize("id,func,uname,pwd,preresult,result",data1.values)
    def test_login(self,browser,id,func,uname,pwd,preresult,result):
        # browser= webdriver.Chrome()
        # browser = webdriver.Firefox()
        url = 'http://127.0.0.1:90'
        username =uname
        password = pwd
        browser = browser
        gongnen.entry_Prerequisite(username, password, browser, url)
        if "个人理财系统" in browser.page_source or "后台管理系统" in browser.page_source:
            print("登陆成功")
            assert "个人理财系统" in browser.page_source or "后台管理系统" in browser.page_source
        elif "密码错误" in browser.page_source or "用户名不存在" in browser.page_source:
            print("登陆失败")
            assert "密码错误" in browser.page_source or "用户名不存在" in browser.page_source
        # assert "个人理财系统" in browser.page_source
        # browser.quit()
        time.sleep(2)

    data2 = pd.read_excel("C:/Users/36017/Desktop/2.xlsx", sheet_name='Sheet2')
    # 注册
    @pytest.mark.parametrize("id,func,uname,pwd,pwd2,preresult,result", data2.values)
    def test_registration(self,browser,id,func,uname,pwd,pwd2,preresult,result):        #http://localhost:90/toregister.html

        result1=    shujuku.select()

        # browser = webdriver.Chrome()      #google
        # browser = webdriver.Firefox()       #firefox
        browser.get('http://localhost:90/toregister.html')
        username_input = browser.find_element('id', 'username')
        password_input = browser.find_element('id', 'password')
        repassword_input = browser.find_element('id', 'repassword')
        submit_button = browser.find_element('id', 'login_btn')

        if pd.isna(uname)==False:
            username_input.send_keys(uname)
        if pd.isna(pwd)==False:
            password_input.send_keys(pwd)
        if pd.isna(pwd2)==False:
            repassword_input.send_keys(pwd2)
        submit_button.click()
        time.sleep(0.5)
        result2 = shujuku.select()

        time.sleep(1)
        if len(result2)-1 == len(result1):      #注册成功
            print("注册成功")
            assert len(result2)-1 == len(result1)
        elif len(result2) == len(result1):        #注册失败
            print("注册失败")
            assert len(result2) == len(result1)   #正确写法

    data3 = pd.read_excel("C:/Users/36017/Desktop/2.xlsx", sheet_name='Sheet3')
    # 开卡
    @pytest.mark.parametrize("id,func,uname,pwd,bankname,banknum,cardtype,preresult,result", data3.values)
    def test_Bank_card_management(self,browser,id,func,uname,pwd,bankname,banknum,cardtype,preresult,result):
        result1=    shujuku.select_bankCard()
        # username,password,browser,url
        url='http://127.0.0.1:90'
        username=uname
        password=pwd
        browser=browser
        gongnen.entry_Prerequisite(username,password,browser,url)
        #先登录


        gongnen.enter_B_C_M(browser)        #进入个人中心的银行卡管理



        # 新增
        xinzeng = browser.find_element('id', 'bankCard_add_modal_btn')
        xinzeng.click()
        time.sleep(1)
        # 输入银行
        cardBank_add_input = browser.find_element('id', 'cardBank_add_input')
        if pd.isna(bankname)==False:
            cardBank_add_input.send_keys(bankname)
        # 输入卡号
        cardNum_add_input = browser.find_element('id', 'cardNum_add_input')
        if pd.isna(banknum)==False:
            cardNum_add_input.send_keys(banknum[0:-1])

        modal_element = browser.find_element(By.ID, 'bankCardAddModal')
        radio_button_1 = modal_element.find_element(By.XPATH, '//input[@type="radio" and @name="type" and @value="1"]')
        radio_button_2 = modal_element.find_element(By.XPATH, '//input[@type="radio" and @name="type" and @value="2"]')
        form = modal_element.find_element(By.CLASS_NAME, "form-horizontal")
        box = form.find_element(By.CLASS_NAME, "example-box")
        # 在包含标签的 div 元素中查找所有的 label 元素
        label_elements = box.find_elements(By.TAG_NAME, 'label')

        if pd.isna(cardtype)==False:
            if (cardtype == "借记卡"):
                if not radio_button_1.is_selected():
                    label_elements[0].click()
            elif cardtype == "信用卡":
                if not radio_button_2.is_selected():
                    label_elements[1].click()
                    # 使用JavaScript点击元素
                    # browser.execute_script("arguments[0].click();", radio_button_2)
                    time.sleep(1)
        time.sleep(0.5)
        baocun = browser.find_element('id', 'bankCard_save_btn')
        baocun.click()
        time.sleep(1)
        result2=    shujuku.select_bankCard()
        time.sleep(0.5)

        if len(result2)==len(result1) :
            print("开卡失败")
            browser.save_screenshot("开卡失败")
            assert len(result2)==len(result1)
        elif result2!=result1:
            print("开卡成功")
            browser.save_screenshot("开卡成功")
            assert len(result2)-1==len(result1)


    data4 = pd.read_excel("C:/Users/36017/Desktop/2.xlsx", sheet_name='Sheet4')
    # 删除卡
    @pytest.mark.parametrize("id,func,uname,pwd,exec,preresult,result", data4.values)
    def test_Bank_card_delete(self,browser,id,func,uname,pwd,exec,preresult,result):
        result1=    shujuku.select_bankCard()
        # browser = webdriver.Chrome()
        # browser = webdriver.Firefox()
        url = 'http://127.0.0.1:90'
        username =uname
        password = pwd
        browser = browser
        gongnen.entry_Prerequisite(username, password, browser, url)
        # 先登录

        gongnen.enter_B_C_M(browser)        #进入个人中心的银行卡管理

        shanchu = browser.find_element(By.XPATH, "//*[contains(@class, 'btn btn-danger delete_btn')]")
        shanchu.click()
        time.sleep(1)
        div_element = browser.find_element(By.XPATH, "//*[contains(@class, 'jconfirm-buttons')]")
        # 获取 <div> 元素下的 <button> 元素
        button_element = div_element.find_elements(By.TAG_NAME, 'button')
        if exec=="确认":
            button_element[0].click()
        elif exec=="取消":
            button_element[1].click()
            time.sleep(0.5)
            # 确认取消
            div_element = browser.find_element(By.XPATH, "//*[contains(@class, 'jconfirm-buttons')]")
            # print(div_element.is_displayed())
            queren = div_element.find_element(By.TAG_NAME,"button")
            queren.click()
        time.sleep(2)


        # 重新设一个默认卡
        # 使用 XPath 定位按钮元素
        moren = browser.find_element(By.XPATH, "//button[@class='btn default_btn']")
        # moren=    browser.find_element(By.CLASS_NAME,"btn default_btn")
        moren.click()
        time.sleep(1)

        result2=shujuku.select_bankCard()
        if len(result2)==len(result1):
            print("删除卡失败")
            assert len(result2)==len(result1)
        elif len(result2)+1==len(result1):
            print("删除卡成功")
            assert len(result2)+1==len(result1)
        # browser.quit()

    data5 = pd.read_excel("C:/Users/36017/Desktop/2.xlsx", sheet_name='Sheet5')
    #卡编辑
    @pytest.mark.parametrize("id,func,uname,pwd,bankname,banknum,banktype,preresult,result", data5.values)
    def test_Bank_card_editor(self,browser,id,func,uname,pwd,bankname,banknum,banktype,preresult,result):
        # browser = webdriver.Chrome()
        # browser = webdriver.Firefox()
        url = 'http://127.0.0.1:90'
        username = uname
        password = pwd
        browser = browser
        gongnen.entry_Prerequisite(username, password, browser, url)
        # 先登录
        gongnen.enter_B_C_M(browser)        #进入个人中心的银行卡管理
        # 编辑
        bianji = browser.find_element(By.XPATH, "//*[contains(@class, 'btn btn-primary update_btn')]")
        bianji.click()
        time.sleep(0.5)

        # 输入银行卡
        cardBank_update_input_value = ""
        cardBank_update_input = browser.find_element('id', 'cardBank_update_input')
        if pd.isna(bankname) == False:
            cardBank_update_input_value = bankname

        if(cardBank_update_input_value!=""):
            cardBank_update_input.clear()
            cardBank_update_input.send_keys(cardBank_update_input_value)



        time.sleep(1)
        # 获取模态框元素
        modal_element = browser.find_element(By.ID, 'bankCardUpdateModal')
        # print(modal_element.is_displayed())

        # # 点击模态框外的区域
        # ActionChains(browser).move_to_element_with_offset(modal_element, -1000, -1000).click().perform()
        radio_button_1=    modal_element.find_element(By.XPATH,'//input[@type="radio" and @name="type" and @value="1"]')
        radio_button_2 = modal_element.find_element(By.XPATH, '//input[@type="radio" and @name="type" and @value="2"]')
        form= modal_element.find_element(By.CLASS_NAME,"form-horizontal")
        box=form.find_element(By.CLASS_NAME,"example-box")
        # 在包含标签的 div 元素中查找所有的 label 元素
        label_elements = box.find_elements(By.TAG_NAME, 'label')

        xingyongka = ""
        if pd.isna(banktype) == False:
            xingyongka = banktype
        # 如果元素可见，再执行点击操作
        if (xingyongka == "借记卡"):
            if not radio_button_1.is_selected():
                label_elements[0].click()
        elif xingyongka == "信用卡" :
            if not radio_button_2.is_selected():
                label_elements[1].click()
                # 使用JavaScript点击元素
                # browser.execute_script("arguments[0].click();", radio_button_2)
                time.sleep(1)

        cardNum_update_input = browser.find_element('id', 'cardNum_update_input')
        cardNum_update_input_value=""
        if pd.isna(banknum) is False  :
            cardNum_update_input_value = banknum[0:-1]

        if (cardNum_update_input_value != ""):
            cardNum_update_input.clear()
            cardNum_update_input.send_keys(cardNum_update_input_value)
        bankCard_update_btn = modal_element.find_element('id', 'bankCard_update_btn')
        bankCard_update_btn.click()
        time.sleep(1)
        succeed = False
        try:
            kuang = modal_element.find_element(By.CLASS_NAME, "form-horizontal")
            help_block = kuang.find_elements(By.CLASS_NAME, 'help-block')
            for i in help_block:
                if "不合法" in i.text:
                    succeed = True
        except StaleElementReferenceException:
            succeed=False
        time.sleep(1)
        if succeed:
            print("卡编辑失败")
        else:
            print("卡编辑成功")



    data6 = pd.read_excel("C:/Users/36017/Desktop/2.xlsx", sheet_name='Sheet6')
    # 买入基金理财

    @pytest.mark.parametrize("id,func,uname,pwd,way,cardpwd,productname,preresult,result", data6.values)
    def test_money_management(self,browser,id,func,uname,pwd,way,cardpwd,productname,preresult,result):
        url = 'http://127.0.0.1:90'
        username = uname
        password = pwd
        browser = browser
        gongnen.entry_Prerequisite(username, password, browser, url)
        # 先登录
        id = shujuku.getId(username, password)

        money1 = shujuku.getmoney(id)

        gerenlicai = browser.find_element(By.XPATH, "//aside[@id='leftbaraside']/div[2]/nav/ul/li[2]")
        gerenlicai.click()
        time.sleep(1)
        href_value=""
        if way=="零钱理财":
            href_value = "/user/finance/toChangeMoney.html"
        elif way=="期限理财":
            href_value = "/user/finance/toTermFinancial.html"
        elif way=="基金理财":
            href_value = "/user/finance/toFundProduct.html"
        linqianlicai = browser.find_element(By.XPATH, "//a[@href = '"+href_value+"']")
        linqianlicai.click()
        time.sleep(1)

        product = browser.find_element(By.XPATH, "//button[@buybtnname='" + productname + "']/span")
        product.click()
        time.sleep(1)

        cardpassword = browser.find_element(By.XPATH, '//div[@id="layui-layer1"]/div[2]/input')
        if pd.isna(cardpwd) == False:
            cardpassword.send_keys(cardpwd)
        time.sleep(1)

        quedin = browser.find_element(By.XPATH, "//div[@id='layui-layer1']//a[@class='layui-layer-btn0']")
        quedin.click()
        time.sleep(1)

        quedin = browser.find_element(By.XPATH, "//div[@class='jconfirm-buttons']/button")
        quedin.click()
        time.sleep(1)

        money2 = shujuku.getmoney(id)

        if money1 == money2:
            print("购买失败")
            assert money1 == money2
        elif money2 < money1:
            print("购买成功")
            assert money2 < money1



    data7 = pd.read_excel("C:/Users/36017/Desktop/2.xlsx", sheet_name='Sheet7')
    # 申请网贷用例
    @pytest.mark.parametrize("id,func,uname,pwd,money1,time1,audit,succeed,preresult,result", data7.values)
    def test_secure_online_loan(self,browser,id,func,uname,pwd,money1,time1,audit,succeed,preresult,result):
        url = 'http://127.0.0.1:90'
        gongnen.entry_Prerequisite(uname, pwd, browser, url)
        # 先登录
        id=    shujuku.getId(uname,pwd)

        result1= shujuku.select_loan(id)
        # print(result1)
        # class="nav-item nav-item-has-subnav"
        ziziyuansu=   browser.find_element(By.XPATH, "//*[contains(@class, 'mdi mdi-wrench')]")
        ziyuansu=    ziziyuansu.find_element(By.XPATH,"..")
        jinrongongju=ziyuansu.find_element(By.XPATH,"..")
        jinrongongju.click()
        time.sleep(1)
        # href = "/user/tools/toApplyLoan.html"
        href_value = "/user/tools/toApplyLoan.html"
        a_element = browser.find_element(By.XPATH, f"//a[@href='{href_value}']")
        a_element.click()
        time.sleep(1)

        money_value=money1
        date_value=time1
        money_input=    browser.find_element("id","amount")
        money_input.send_keys(money_value)
        termy_input = browser.find_element("id", "term")
        termy_input.send_keys(date_value)
        submit = browser.find_element("id", "submit")
        submit.click()
        time.sleep(0.5)
        jconfirm_buttons=browser.find_element(By.CLASS_NAME,"jconfirm-buttons")
        # print(jconfirm_buttons.is_displayed())
        btns=    jconfirm_buttons.find_elements(By.TAG_NAME,"button")
        # btn[0]是确定 btn[1]是取消
        queding=btns[0]
        queding.click()
        time.sleep(2)
        result2=shujuku.select_loan(id)
        if pd.isna(audit)==False:           #审核
            if 1==audit:
                gongnen.entry_Prerequisite("admin","123456",browser,url)
                wangdaiguanli = browser.find_element(By.XPATH,'//*[@id="leftbaraside"]/div[2]/nav/ul/li[5]')
                wangdaiguanli.click()
                time.sleep(0.5)
                wangdaishenhe=  browser.find_element(By.XPATH,'//*[@id="leftbaraside"]/div[2]/nav/ul/li[5]/ul/li[1]/a')
                wangdaishenhe.click()
                time.sleep(0.5)
                div1=  browser.find_element(By.CLASS_NAME,'col-md-5')
                ul=    div1.find_element(By.TAG_NAME,"ul")
                ui = ul.find_elements(By.XPATH, ".//li")
                moooo=len(ui)+1
                moye= browser.find_element(By.XPATH,'/html/body/div/div/main/div/div/div/div/div[3]/div[2]/nav/ul/li['+str(moooo)+']/a')
                print(len(ui))
                moye.click()
                time.sleep(3)
                loan_id=    shujuku.get_loan_id(id)
                # 使用 XPath 定位按钮
                table=   browser.find_element(By.TAG_NAME,"table")
                rows = table.find_elements(By.TAG_NAME, "tr")
                print(len(rows))
                hang=len(rows)-1
                button1 = browser.find_element(By.XPATH,'/html/body/div/div/main/div/div/div/div/div[2]/div/table/tbody/tr['+str(hang)+']/td[7]/button[1]')
                button1.click()
                time.sleep(0.5)
                queding = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button[1]')
                quexiao = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button[2]')
                queding.click()
                time.sleep(3)
        if (result2) == (result1):
            print("申请网贷用例失败")
            assert (result2) == (result1)
        elif (result2) == (result1)+1:
            print("申请网贷用例成功")
            assert (result2) == (result1)+1

