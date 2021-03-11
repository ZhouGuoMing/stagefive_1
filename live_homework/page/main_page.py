# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : main_page.py

from selenium.webdriver.common.by import By
from live_homework.page.add_member_page import AddMemberPage
from live_homework.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        '''
        添加成员
        :return:
        '''
        # click add member
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # return AddMemberPage()
        return AddMemberPage(self.driver)



