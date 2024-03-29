# coding=utf-8
import random
import re
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode
from utils.datachoice import credit_code, nice
from utils.screenshort import get_screenshort


class ZnZzTest(MyTestCase):
    """智能注册测试集"""

    def test_znzz_1(self):
        """智能注册_企业测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条
        suiji = random.randint(2, 45)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()

        print("选择了第{}类商标分类!".format(suiji))

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        time.sleep(3)
        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector("#ssq").click()
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child({})".format(
                random.randint(1, 5))).click()
        time.sleep(2)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        # 解决弹框
        # self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        # time.sleep(1)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "15624992489")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys(
            "132132@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "03515978787")
        time.sleep(2)
        # 解决常用申请人弹框，点击空白处
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        # time.sleep(1)
        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_1.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过!")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_znzz_2(self):
        """智能注册_个体测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()

        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条
        suiji = random.randint(2, 46)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()

        print("选择了第{}类商标分类!".format(suiji))

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        time.sleep(3)
        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        self.driver.find_element_by_link_text("个体工商户").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))

        # 添加社会信用代码
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-gsh > tr:nth-child(2) > td.td-content > input").send_keys(
            credit_code("credit_code.txt"))

        self.driver.find_element_by_css_selector("#geren-idCard").send_keys("140121198906133513")
        time.sleep(1)
        self.driver.find_element_by_css_selector("#personalssq").click()
        self.driver.find_element_by_css_selector(
            "#personalistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector(
            "#personalistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#geren-postcode").clear()
        self.driver.find_element_by_css_selector("#geren-postcode").send_keys("102200")
        self.driver.find_element_by_css_selector("#geren-street").clear()
        self.driver.find_element_by_css_selector("#geren-street").send_keys("北京市昌平区")

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(1) > td.td-content > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(2) > td.td-content > input").send_keys(
            "15122311456")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(3) > td.td-content > input").send_keys(
            "123313@qq.com")

        # 解决常用申请人弹框，点击空白处
        # self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_2.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_znzz_3(self):
        """智能注册_企业测试_历史订单"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(2)").click()

        """商标类别导入历史订单"""
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-right > h3 > div > a.btn.showHistoryOrder").click()
        time.sleep(2)
        history_number = random.randint(2, 10)
        info = self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number)).text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        time.sleep(3)
        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector("#ssq").click()
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child({})".format(
                random.randint(1, 5))).click()
        time.sleep(2)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        # 解决弹框
        # self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        # time.sleep(1)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "15624992489")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys(
            "132132@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "03515978787")
        time.sleep(2)
        # 解决常用申请人弹框，点击空白处
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        # time.sleep(1)
        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_3.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_znzz_4(self):
        """智能注册_个体测试_历史订单"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()

        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(2)").click()

        """商标类别导入历史订单"""
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-right > h3 > div > a.btn.showHistoryOrder").click()
        time.sleep(2)
        history_number = random.randint(2, 10)
        info = self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number)).text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        time.sleep(3)
        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        self.driver.find_element_by_link_text("个体工商户").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))

        # 添加社会信用代码
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-gsh > tr:nth-child(2) > td.td-content > input").send_keys(
            credit_code("credit_code.txt"))

        self.driver.find_element_by_css_selector("#geren-idCard").send_keys("140121198906133513")
        time.sleep(1)
        self.driver.find_element_by_css_selector("#personalssq").click()
        self.driver.find_element_by_css_selector(
            "#personalistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector(
            "#personalistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#geren-postcode").clear()
        self.driver.find_element_by_css_selector("#geren-postcode").send_keys("102200")
        self.driver.find_element_by_css_selector("#geren-street").clear()
        self.driver.find_element_by_css_selector("#geren-street").send_keys("北京市昌平区")

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(1) > td.td-content > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(2) > td.td-content > input").send_keys(
            "15122311456")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(3) > td.td-content > input").send_keys(
            "123313@qq.com")

        # 解决常用申请人弹框，点击空白处
        # self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_4.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_znzz_5(self):
        """个人订单修改测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(2)
        try:
            self.driver.find_elements_by_css_selector(".modal-body > .close")[0].click()
        except Exception:
            pass
        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()
        time.sleep(2)
        self.assertIn("权大师_我的商标", self.driver.title)
        print(self.driver.title)

        time.sleep(2)
        # 切换成下单时间
        self.driver.find_element_by_class_name("order-time").click()
        time.sleep(2)
        # 选择修改的订单号
        print("订单编号:" + self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span").text)
        # 查看详情
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(8) > div > a.t-href").click()
        time.sleep(3)

        """修改商标名字"""
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(4) > h2 > a").click()
        # self.driver.find_element_by_css_selector("#modal-brand > div.modal-button > a.button.save").click()
        print("商标名字修改成功!")

        time.sleep(1)

        """修改尼斯分类"""
        self.driver.execute_script("window.scrollBy(0,4200)")  # 滑动滚动条
        suiji = random.randint(2, 46)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.order-categories > h2 > a").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-right > div > div > h4 > div.header-right > a > i").click()
        time.sleep(2)
        # self.driver.find_element_by_css_selector("#section-selfchoice > div > div.group-left.scroll > ul > li:nth-child({}) > span".format(suiji)).click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li:nth-child(3) > span".format(suiji)).click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()

        self.driver.find_element_by_css_selector("#edit-category > div.modal-button > a.button.save").click()

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        time.sleep(2)
        print("尼斯分类修改为第{}类!".format(suiji - 1))
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0,9200)")  # 滑动滚动条

        """申请人信息"""

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.applicant-info > h2 > a").click()
        #
        # self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > table > thead > tr:nth-child(1) > td.td-content > a.btn-choice.fownertype.active").click()
        # self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > div > div > div > table > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()
        # self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > div > div > div > table > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys("田伟")
        # self.driver.find_element_by_css_selector("#geren-idCard").clear()
        # self.driver.find_element_by_css_selector("#geren-idCard").send_keys("130184198908191520")
        # self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-button > a.button.save").click()
        print("申请人信息修改成功!")

        """订单联系人"""

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(8) > div > h2 > a").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").clear()
        self.driver.find_element_by_css_selector(
            "#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
            "大西瓜")
        self.driver.find_element_by_name("ftelephone").clear()
        self.driver.find_element_by_name("ftelephone").send_keys("0351-5925212")
        self.driver.find_element_by_css_selector("#change-contact-info > div.modal-button > a.button.save").click()
        print("订单联系人修改成功!")
        time.sleep(1)
        get_screenshort(self.driver, "test_personal_modify.png")

        print("订单修改测试通过!")

    def test_znzz_6(self):
        """智能注册_新版智能推荐测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label.label.checked").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条

        """智能推荐"""
        self.driver.find_element_by_css_selector("#selectBusiness > div").click()
        industry = random.randint(1, 12)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry))).perform()
        ly = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry)).text
        time.sleep(2)
        sz = random.randint(1, 2)
        hy = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).text
        self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).click()
        ActionChains(self.driver).release()

        print("选择所在领域:" + ly + "_" + hy + "_" + "行业精准推荐")
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()
        time.sleep(2)

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        """申请人信息"""
        time.sleep(3)
        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector("#ssq").click()
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child({})".format(
                random.randint(1, 5))).click()
        time.sleep(2)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        # 解决弹框
        # self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        # time.sleep(1)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "15624992489")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys(
            "132132@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "03515978787")
        time.sleep(2)
        # 解决常用申请人弹框，点击空白处
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        # time.sleep(1)
        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_6.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过!")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_znzz_7(self):
        """智能注册_全类保护测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称:{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        """全类保护"""
        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(3)").click()
        time.sleep(20)
        print("类别:全类保护")

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()
        time.sleep(2)
        """不足10小项确认提交"""
        self.driver.find_element_by_link_text("确认").click()

        time.sleep(10)
        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        """申请人信息"""

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector("#ssq").click()
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child({})".format(
                random.randint(1, 5))).click()
        time.sleep(2)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        # 解决弹框
        # self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        # time.sleep(1)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "15624992489")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys(
            "132132@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "03515978787")
        time.sleep(2)
        # 解决常用申请人弹框，点击空白处
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        # time.sleep(1)
        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_7.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功,应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过!")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_znzz_8(self):
        """智能注册_添加类别测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label.label.checked").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条

        """智能推荐"""
        self.driver.find_element_by_css_selector("#selectBusiness > div").click()
        industry = random.randint(1, 12)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry))).perform()
        ly = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry)).text
        time.sleep(2)
        sz = random.randint(1, 2)
        hy = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).text
        self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).click()
        ActionChains(self.driver).release()

        print("选择所在领域:" + ly + "_" + hy + "_" + "行业精准推荐")
        time.sleep(5)

        # 推荐的类别信息
        list_name = self.driver.find_element_by_css_selector(
            "#section-recommend > div.category-recommend-scroll-box > div > div > div.crs-left.scroll").text

        # s_1 = re.findall(r"\d+",list_name)
        # s_2 = ['01','02','03','04','05','06','07','08','09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20' ,'21', '22' ,'23' ,'24' ,'25', '26' ,'27', '28', '29', '30' ,'31' ,'32' ,'33' ,'34' ,'35' ,'36', '37', '38', '39' ,'40' ,'41', '42', '43' ,'44','45']
        #
        # # s_2中有而s_1中没有的
        # s_3 = random.choice(list(set(s_2).difference(set(s_1))))

        s_3 = nice(list_name)

        # 点击添加类别

        self.driver.execute_script("window.scrollBy(0,5200)")  # 滑动滚动条
        self.driver.find_element_by_link_text("+ 添加类别").click()
        # 选择类别
        add = self.driver.find_element_by_css_selector(
            "#section-recommend > div > div.add-first-category > ul > li:nth-child({})".format(s_3)).text

        self.driver.find_element_by_css_selector(
            "#section-recommend > div > div.add-first-category > ul > li:nth-child({})".format(s_3)).click()
        # 点击添加小项
        self.driver.find_element_by_css_selector("#first{} > div.category-recommend-groups-box > a".format(s_3)).click()
        # 选择小项
        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > ul > li:nth-child(1)".format(s_3)).click()

        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(1)".format(s_3)).click()
        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(2)".format(s_3)).click()
        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(3)".format(s_3)).click()
        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(4)".format(s_3)).click()
        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(5)".format(s_3)).click()

        print("添加类别:" + add)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()
        time.sleep(2)

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        """申请人信息"""
        time.sleep(3)
        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector("#ssq").click()
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child({})".format(
                random.randint(1, 5))).click()
        time.sleep(2)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        # 解决弹框
        # self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        # time.sleep(1)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "15624992489")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys(
            "132132@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "03515978787")
        time.sleep(2)
        # 解决常用申请人弹框，点击空白处
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        # time.sleep(1)
        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_8.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过!")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_znzz_9(self):

        """智能商标注册_添加类别（金额校验）"""
        dl = DengLuPage(self.driver)
        self.driver.get("https://www.quandashi.com/product-buy/PC10003.html")
        dl.refresh()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        time.sleep(2)

        """填写商标信息"""
        try:
            self.driver.find_elements_by_css_selector(".modal-body > .close")[0].click()
        except Exception:
            pass
        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_link_text("生成黑白图样").click()
        print("商标名称填写成功!")

        time.sleep(5)
        self.driver.find_element_by_css_selector("#selectCategoryType > label.label.checked").click()
        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

        """智能推荐"""
        self.driver.find_element_by_css_selector("#selectBusiness > div").click()
        industry = random.randint(1, 12)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry))).perform()
        ly = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry)).text
        time.sleep(2)
        sz = random.randint(1, 2)
        hy = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).text
        self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).click()
        ActionChains(self.driver).release()

        print("选择所在领域:" + ly + "_" + hy + "_" + "行业精准推荐")

        time.sleep(15)

        number_1 = self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-sense > em > i").text

        number_2 = re.sub(r"\D", "", number_1)

        number_3 = int(number_2) + 0
        print(number_3)

        # 推荐的类别信息
        list_name = self.driver.find_element_by_css_selector(
            "#section-recommend > div.category-recommend-scroll-box > div > div > div.crs-left.scroll").text

        # s_1 = re.findall(r"\d+",list_name)
        # s_2 = ['01','02','03','04','05','06','07','08','09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20' ,'21', '22' ,'23' ,'24' ,'25', '26' ,'27', '28', '29', '30' ,'31' ,'32' ,'33' ,'34' ,'35' ,'36', '37', '38', '39' ,'40' ,'41', '42', '43' ,'44','45']
        #
        # # s_2中有而s_1中没有的
        # s_3 = random.choice(list(set(s_2).difference(set(s_1))))

        s_3 = nice(list_name)

        # 点击添加类别

        self.driver.execute_script("window.scrollBy(0,5200)")  # 滑动滚动条
        self.driver.find_element_by_link_text("+ 添加类别").click()
        time.sleep(3)
        # 选择类别
        add = self.driver.find_element_by_css_selector(
            "#section-recommend > div > div.add-first-category > ul > li:nth-child({})".format(s_3)).text

        self.driver.find_element_by_css_selector(
            "#section-recommend > div > div.add-first-category > ul > li:nth-child({})".format(s_3)).click()
        # 点击添加小项
        self.driver.find_element_by_css_selector("#first{} > div.category-recommend-groups-box > a".format(s_3)).click()
        # 选择小项
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > ul > li:nth-child(1)".format(s_3)).click()
        #
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(1)".format(s_3)).click()
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(2)".format(s_3)).click()
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(3)".format(s_3)).click()
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(4)".format(s_3)).click()
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(5)".format(s_3)).click()

        print("添加类别:" + add)
        time.sleep(5)

        number_4 = self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-sense > em > i").text

        number_5 = re.sub(r"\D", "", number_4)

        number_6 = int(number_5) + 0
        print(number_6)

        self.assertEqual(number_3, number_6, "价格异常请及时查看!")

        print("智能商标注册_添加类别（金额校验）,测试通过!")

    def test_znzz_10(self):
        """智能注册_图形"""

        print("涉及上传文件需要在有界面浏览器测试请执行 uploadtest.py 进行测试!")

        # # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        # #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        # #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        # dl = DengLuPage(self.driver)
        # # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # # self.driver.find_element_by_id()
        # # self.driver.find_element()
        # dl.login()
        # time.sleep(2)
        # ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
        #     "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        # time.sleep(2)
        # ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
        #     "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        # ActionChains(self.driver).release()
        # self.driver.find_element_by_css_selector(
        #     "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # # 获取打开的多个窗口句柄
        # windows = self.driver.window_handles
        # # 切换到当前最新打开的窗口
        # self.driver.switch_to.window(windows[-1])
        # time.sleep(2)
        # self.driver.set_window_size(1920, 1080)
        # self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        # print(self.driver.title)
        # self.driver.find_element_by_css_selector(
        #     "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()
        #
        # for a in self.driver.find_elements_by_css_selector("#total-price"):
        #     print("费用总计:"+a.text)
        #     # aa=a.text
        #
        # self.driver.find_element_by_css_selector(
        #     "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        # time.sleep(2)
        # self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # # body > div.recommend-help > i
        #
        #
        # self.driver.find_element_by_css_selector("#selectBrandType > label:nth-child(2)").click()
        # self.driver.find_element_by_css_selector("body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.form-wrap.show3 > ul > li.brand-upload > div > div.brand-upload-wrap > div.shoudong-create > ul > li > div > div > div.photo-box.btnuploadtuyang > div").click()
        #
        # """上传商标图片"""
        # path = driver_path + "\\" + "Upload_files.exe"
        # os.system(path)
        #
        # print("商标图形:小鸡图片")
        # time.sleep(5)
        #
        # self.driver.find_element_by_css_selector(
        #     "#selectCategoryType > label:nth-child(2)").click()
        # self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条
        # suiji = random.randint(2, 45)
        # time.sleep(2)
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()
        #
        # time.sleep(2)
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()
        #
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        #
        #
        # print("选择了第{}类商标分类!".format(suiji))
        #
        # print(1)
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()
        # print(2)
        #
        # try:
        #     self.driver.find_element(By.LINK_TEXT, "确认")
        #     a = True
        # except:
        #     a = False
        # if a is True:
        #     """不足10小项确认提交"""
        #     self.driver.find_element_by_link_text("确认").click()
        # elif a is False:
        #     pass
        #
        # time.sleep(3)
        #
        # # 获取打开的多个窗口句柄
        # windows = self.driver.window_handles
        # # 切换到当前最新打开的窗口
        # self.driver.switch_to.window(windows[-1])
        # time.sleep(2)
        #
        #
        # # self.driver.execute_script("document.getElementByName('fname').length = 0;")
        #
        # # self.driver.find_element_by_css_selector(
        # #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()
        #
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
        #     "{}".format(unicode()))
        # self.driver.find_element_by_css_selector("#ssq").click()
        # self.driver.find_element_by_css_selector(
        #     "#companylistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        # time.sleep(2)
        # self.driver.find_element_by_css_selector(
        #     "#companylistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child({})".format(random.randint(1,5))).click()
        # time.sleep(2)
        #
        # # 添加社会信用代码
        # self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))
        #
        # # 解决弹框
        # # self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        # # time.sleep(1)
        #
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
        #     "{}".format(unicode()))
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
        #     "15624992489")
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys(
        #     "132132@qq.com")
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys("03515978787")
        # time.sleep(2)
        # # 解决常用申请人弹框，点击空白处
        # self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > h2").click()
        #
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        # time.sleep(1)
        # # self.driver.find_element_by_css_selector(
        # #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        # # time.sleep(1)
        # """订单备注"""
        # self.driver.find_element_by_css_selector(
        #     "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
        #     time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")
        #
        # get_screenshort(self.driver, "test_znzz_1.png")
        #
        # for i in self.driver.find_elements_by_css_selector("body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
        #
        #     print("总价:"+i.text)
        #     ii = i.text
        #
        # # self.assertIn(aa,ii)
        # # print("测试通过")
        # # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        # self.driver.find_element_by_css_selector("body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        # for o in self.driver.find_elements_by_class_name("payable"):
        #     print("订单提交成功，应付金额:"+o.text)
        #     oo = o.text
        #
        # self.assertIn(oo,ii)
        #
        # print("测试通过!")
        #
        # self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_smart_nice_search(self):
        """尼斯分类搜索(智能注册)"""

        dl = DengLuPage(self.driver)
        self.driver.get("https://www.quandashi.com/product-buy/PC10003.html")
        dl.refresh()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        time.sleep(2)
        try:
            self.driver.find_elements_by_css_selector(".modal-body > .close")[0].click()
        except Exception:
            pass
        self.driver.find_element_by_css_selector("#selectCategoryType > label:nth-child(2)").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > div > div > input").send_keys("摩托车")
        self.driver.find_element_by_css_selector("#btn-search > i").click()
        time.sleep(3)

        number_1 = self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > div > li:nth-child(1) > span").text

        number_2 = re.sub(r"\D", "", number_1)

        number_3 = int(number_2) + 0

        self.assertEqual(number_3, 7, "尼斯分类搜索结果异常!")

        print("智能商标注册尼斯分类搜索结果正常!")
