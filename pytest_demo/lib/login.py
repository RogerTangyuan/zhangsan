
import selenium.webdriver
import selenium.webdriver.edge.service
import selenium.webdriver.common.by
import time


def loginAndCheck(username,password,num):    
    wb = selenium.webdriver.Edge(service=selenium.webdriver.edge.service.Service("selenium_demo/msEdgeDriver.exe"))
    wb.implicitly_wait(10)
    
    wb.get("http://192.168.137.40/mgr/sign.html")
    if username is not None:
        wb.find_element(selenium.webdriver.common.by.By.ID,"username").send_keys(username)
    
    if password is not None:
        wb.find_element(selenium.webdriver.common.by.By.ID,"password").send_keys(password)
    
    wb.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,"[type='submit']").click()
    
    time.sleep(1)
    if num != True:
        alertText = wb.switch_to.alert.text 
        print(alertText)
    
        return alertText
    
    return wb