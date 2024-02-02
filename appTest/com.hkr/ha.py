import time
import pandas as pd
import pytest
from appium import webdriver
from urllib3.exceptions import ProtocolError
from hahaha import APP



class Test_APP:

    data1=pd.read_excel("1.xlsx",sheet_name="Sheet1")

    @pytest.fixture
    def driver(self):
        app_dict = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "Huawei",
            "appPackage": "com.baidu.tieba",
            "appActivity": "com.baidu.tieba.tblauncher.MainTabActivity",
            "noReset": True
        }
        i=0
        while i==0:
            try:
                driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", app_dict)

                i = 1
                yield driver
                driver.quit()
            except Exception:
                time.sleep(15)

    @pytest.mark.parametrize("id,biaoti,zhengwen,picture,ba_name,topic",data1.values)
    def test_fatiezi(self,driver,id,biaoti,zhengwen,picture,ba_name,topic):
        # biaoti="这是帖子标题"
        # zhengwen="这是帖子正文哈哈哈哈哈哈哈哈哈哈哈"
        # ba_name="哈哈哈"
        # topic="哈哈哈哈"
        APP.fatiezi(driver,biaoti,zhengwen,picture,ba_name,topic)
        time.sleep(10)
        if "发布帖子" in driver.page_source:
            print("发布失败")
            assert "发布帖子" in driver.page_source
        elif "关注" in driver.page_source and "推荐" in driver.page_source and "热门" in driver.page_source:
            print("发帖成功")
            assert "关注" in driver.page_source and "推荐" in driver.page_source and "热门" in driver.page_source
        time.sleep(10)



    data2=pd.read_excel("1.xlsx",sheet_name="Sheet2")
    @pytest.mark.parametrize("id,dianzan,content,picture",data2.values)
    def test_pinlun(self,driver,id,dianzan,content,picture):
        # dianzan="yes"
        # content="66666666"
        # picture="no"
        if pd.isna(content):
            content=""
        APP.pinlun(driver,dianzan,content,picture)
        time.sleep(10)
        time.sleep(2)
        assert content in driver.page_source