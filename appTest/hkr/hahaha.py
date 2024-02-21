import adbutils
import time

import pandas
import pytest
import retry
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#设置终端的参数项


class APP:

    def fatiezi(driver:webdriver,biaoti,zhengwen,picture,ba_name,topic):
        time.sleep(15)
        #刷新
        TouchAction(driver).tap(x=104, y=1856).perform()
        time.sleep(4)


        TouchAction(driver).tap(x=535, y=1862).perform()
        time.sleep(4)
        TouchAction(driver).tap(x=283, y=208).perform()
        time.sleep(4)
        TouchAction(driver).tap(x=208, y=225).perform()
        time.sleep(8)
        # biaoti = "这是帖子标题"
        # zengwen="这是帖子正文哈哈哈哈哈哈哈哈哈哈哈"
        try:
            el2 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText")
            el2.send_keys(biaoti)
        except NoSuchElementException:
            el2 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText")

            el2.send_keys(biaoti)
        time.sleep(6)
        TouchAction(driver).tap(x=151, y=378).perform()
        try:
            el2 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText")
            el2.send_keys(zhengwen)
        except NoSuchElementException:
            el2 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText")
            el2.send_keys(zhengwen)

        if picture=="yes":
            # 发图片
            TouchAction(driver).tap(x=190, y=853).perform()
            time.sleep(6)
            TouchAction(driver).tap(x=509, y=221).perform()
            time.sleep(6)
            el2 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.View")
            el2.click()
            time.sleep(6)

        #选择吧
        time.sleep(6)
        TouchAction(driver).tap(x=771, y=1163).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=208, y=317).perform()
        time.sleep(8)
        try:
            el1 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText")
            el1.send_keys(ba_name)
        except NoSuchElementException:
            el1 = driver.find_element(by=AppiumBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText")
            el1.send_keys(ba_name)
        # "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText"

        time.sleep(8)
        TouchAction(driver).tap(x=104, y=538).perform()
        time.sleep(6)

        # 选择话题
        TouchAction(driver).tap(x=375, y=1395).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=659, y=1522).perform()
        time.sleep(6)

        el1 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.EditText")
        el1.click()
        time.sleep(6)
        el1.send_keys(topic)
        time.sleep(6)


        try:
            el2 = driver.find_element(by=MobileBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
            el2.click()
            time.sleep(6)
        except NoSuchElementException:
            TouchAction(driver).tap(x=158, y=245).perform()
            time.sleep(6)
        time.sleep(6)

        #默认同步到主页
        tongbu=False
        if  tongbu==False:
            TouchAction(driver).tap(x=46, y=1797).perform()
            time.sleep(6)
        #发帖子
        TouchAction(driver).tap(x=983, y=97).perform()
        time.sleep(6)



    def pinlun(driver:webdriver,dianzan,content,picture):
        time.sleep(15)
        # 刷新
        TouchAction(driver).tap(x=104, y=1856).perform()
        time.sleep(6)

        try:
            el1 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView")
            print(11111)
            el1.click()
        except NoSuchElementException :
            try:

                el1 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]")
                print(22222)
                el1.click()
            except NoSuchElementException:

                el1 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]")
                print("33333")
                el1.click()
        time.sleep(6)

        if dianzan=="yes":
            time.sleep(6)
            TouchAction(driver).tap(x=955, y=1868).perform()
            time.sleep(6)
        el1 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.TextView")
        el1.click()
        time.sleep(6)



        if picture =="yes":
            TouchAction(driver).tap(x=104, y=1864).perform()
            time.sleep(6)
            TouchAction(driver).tap(x=505, y=221).perform()
            time.sleep(6)
            el1 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.View")
            el1.click()
            time.sleep(6)
            el2 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView")
            el2.click()
            time.sleep(6)
            TouchAction(driver).tap(x=154, y=267).perform()
            time.sleep(6)
            el4 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText")
            el4.send_keys(str(content))
            time.sleep(6)
            el5 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView")
            el5.click()
            time.sleep(6)
        else:
            el2 = driver.find_element(by=MobileBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
            el2.send_keys(str(content))
            time.sleep(6)
            TouchAction(driver).tap(x=1005, y=1789).perform()
        time.sleep(6)






