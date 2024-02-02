import adbutils
import time

import pytest
import retry
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException


#设置终端的参数项


class Test_App:

    @pytest.fixture
    def driver(self):
        app_dict = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "Huawei",
            "appPackage": "com.baidu.tieba",
            "appActivity": "com.baidu.tieba.tblauncher.MainTabActivity",
            "noReset": True,
        }
        i=0
        while i==0:
            try:
                driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", app_dict)
                time.sleep(15)
                i = 1
                yield driver
                driver.quit()
            except Exception:
                time.sleep(15)


    def test_fatiezi(self,driver):

        TouchAction(driver).tap(x=535, y=1862).perform()
        time.sleep(3)
        TouchAction(driver).tap(x=283, y=208).perform()
        time.sleep(3)
        TouchAction(driver).tap(x=208, y=225).perform()
        time.sleep(1)
        biaoti = "这是帖子标题"
        zengwen="这是帖子正文哈哈哈哈哈哈哈哈哈哈哈"
        try:
            el2 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText")
            el2.send_keys(biaoti)
        except NoSuchElementException:
            el2 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText")

            el2.send_keys(biaoti)
        time.sleep(2)
        TouchAction(driver).tap(x=151, y=378).perform()
        try:
            el2 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText")
            el2.send_keys(zengwen)
        except NoSuchElementException:
            el2 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText")
            el2.send_keys(zengwen)

        #发图片
        TouchAction(driver).tap(x=190, y=853).perform()
        time.sleep(2)
        TouchAction(driver).tap(x=509, y=221).perform()
        time.sleep(2)
        el2 = driver.find_element(by=MobileBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.View")
        el2.click()
        time.sleep(2)

        #选择吧
        time.sleep(1)
        TouchAction(driver).tap(x=726, y=1168).perform()
        time.sleep(1)
        el2 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText")
        el2.click()
        time.sleep(1)
        el2.send_keys("哈哈哈")
        time.sleep(4)
        TouchAction(driver).tap(x=100, y=517).perform()
        time.sleep(1)


        # 选择话题
        TouchAction(driver).tap(x=375, y=1395).perform()
        time.sleep(4)
        el1 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.EditText")
        el1.click()
        el1.send_keys("哈哈哈哈哈")
        el2 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout")
        el2.click()
        time.sleep(3)

        #默认同步到主页
        tongbu=False
        if  tongbu==False:
            TouchAction(driver).tap(x=46, y=1797).perform()
        #发帖子
        TouchAction(driver).tap(x=983, y=97).perform()
        time.sleep(4)
        assert biaoti in driver.page_source and zengwen in driver.page_source
        time.sleep(15)


    def test_pinlun(self,driver):
        # driver.refresh()
        try:
            el1 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]")
            el1.click()
            # driver.back()
        except Exception:
            el1 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]")
            el1.click()
        time.sleep(5)

        el1 = driver.find_element(by=MobileBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.TextView")
        el1.click()

        time.sleep(5)
        el2 = driver.find_element(by=MobileBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
        content="66666666"
        el2.send_keys(content)

        el3 = driver.find_element(by=MobileBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.view.View")
        el3.click()
        time.sleep(5)
        time.sleep(2)
        assert content in driver.page_source





