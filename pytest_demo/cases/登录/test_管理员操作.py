from pytest_demo.lib.login import loginAndCheck
import selenium.webdriver.common.by
import time

class Test_adminManage():
    def test_UI_0101(self):
        print("\n用例 UI_0101")
        
        wb = loginAndCheck("byhy","88888888",True)
        wb.implicitly_wait(10)
        
        
        a1 = wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,"#root > aside > section > ul > li:nth-child(2) > a > span")
        a2 = wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,"#root > aside > section > ul > li:nth-child(3) > a > span")
        a3 = wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,"#root > aside > section > ul > li:nth-child(4) > a > span")
        
        #assert a1.text == "客户"
        #assert a2.text == "药品" 
        #assert a3.text == "订单"
        assert [a1.text,a2.text,a3.text] == ["客户","药品","订单"]
        
    def test_UI_0102(self):
        print("\n用例 UI_0102")
        
        wb = loginAndCheck("byhy","88888888",True)
        
        wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,'#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > button').click()
        wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,'#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > div.col-lg-8.col-md-8.col-sm-8 > div:nth-child(1) > input').send_keys('南京中医院')
        wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,'#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > div.col-lg-8.col-md-8.col-sm-8 > div:nth-child(2) > input').send_keys('12345678')        
        wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,'#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > div.col-lg-8.col-md-8.col-sm-8 > div:nth-child(3) > textarea').send_keys('南京市秦淮区光华路')       
        wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,'#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > div.col-lg-12.col-md-12.col-sm-12 > button:nth-child(1)').click()
        
        time.sleep(2)
        a1 = wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,'#root > div > section.content.container-fluid > div:nth-child(3) > div:nth-child(1) > span:nth-child(2)')
        a2 = wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,'#root > div > section.content.container-fluid > div:nth-child(3) > div:nth-child(2) > span:nth-child(2)')       
        a3 = wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,'#root > div > section.content.container-fluid > div:nth-child(3) > div:nth-child(3) > span:nth-child(2)')
        wb.quit()
        assert [a1.text,a2.text,a3.text] == ["南京中医院","12345678","南京市秦淮区光华路"]
        