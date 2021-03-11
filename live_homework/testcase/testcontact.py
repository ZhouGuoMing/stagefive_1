# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : testcontact.py

import pytest
import yaml

from live_homework.page.login_page import LoginPage
from live_homework.page.base_page import BasePage
from time import sleep

# 使用yaml文件数据驱动
with open("./wechat.yaml",) as f:
    datas = yaml.safe_load(f)['wechat']
    add_member_datas=datas['addmemberdatas']
    myid = datas['myid']

@pytest.fixture(params=add_member_datas,ids=myid)
def get_add_member_datas(request):
    data=request.param
    print(f"测试数据为：{data}")
    yield data

class TestContact:
    def setup(self):
        self.loginpage = LoginPage()
    def teardown(self):
        self.loginpage.quit_driver()

    def test_addmember(self,get_add_member_datas):
        login = self.loginpage.login_cookies()
        page = login.goto_add_member()
        page.add_member(get_add_member_datas[0], get_add_member_datas[1], get_add_member_datas[2])
        names = page.get_member()
        print(names)
        username=str(get_add_member_datas[0])
        assert username in names

    # def test_cookies(self):
    #     self.basepage=BasePage()
    #     self.basepage.get_url("https://work.weixin.qq.com/wework_admin/frame#index")
    #     sleep(20)
    #     此时扫码登录
    #     cookies = self.basepage.driver.get_cookies()
    #     print(cookies)


