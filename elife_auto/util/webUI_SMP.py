import sys
sys.path.append('elife_auto')
import selenium.webdriver
import selenium.webdriver.edge.service
import selenium.webdriver.common.by as By
import selenium.webdriver.support.ui as UI
import util.cfg
import time

class SMP_UI:
    def __init__(self):
        self.wd = selenium.webdriver.Edge(service=selenium.webdriver.edge.service.Service("D:\workhome\github\zhangsan\selenium_demo\msEdgeDriver.exe"))
        self.wd.implicitly_wait(10)        
    
    def login(self,username,password):
        self.wd.get(util.cfg.SMP_URL_Login)
        
        time.sleep(1)
        
        if username is not None: 
            self.wd.find_element(By.By.ID,'username').send_keys(username)
        if password is not None: 
            self.wd.find_element(By.By.ID,'password').send_keys(password)
        
        time.sleep(1)
        
        self.wd.find_element(By.By.ID,'loginBtn').click()
        
    def add_device_model(self,devType,name,desc):
        #创建Select对象
        select = UI.Select(self.wd.find_element(By.By.ID,'device-type'))
        
        select.select_by_visible_text(devType)
        
        ele = self.wd.find_element(By.By.ID,'device-model')
        ele.clear()
        ele.send_keys(name)
        
        ele = self.wd.find_element(By.By.ID,'device-model-desc')
        ele.clear()
        ele.send_keys(desc)
        
        self.wd.find_element(By.By.CSS_SELECTOR,'body > main > div.add-one-area > div > div.add-one-submit-btn-div > span').click()
        
    def get_first_page_device_model(self):
        values = self.wd.find_elements(By.By.CSS_SELECTOR,'.field-value')
        self.wd.implicitly_wait(10) 
        deviceModels=[]
        for idx,value in enumerate(values):
            if (idx+1) % 3 ==0:
                deviceModels.append([values[idx-2].text,values[idx-1].text,values[idx].text])
        return deviceModels
    
    def del_first_item(self):
        delBtn = self.wd.find_elements(By.By.CSS_SELECTOR,
                                      '.result-list-item:first-child .result-list-item-btn-bar span:first-child')
        self.wd.implicitly_wait(10) 
        if not delBtn:
            return False
        
        time.sleep(2)
        delBtn[0].click()
        
        self.wd.switch_to.alert.accept()
        
        return True
    
    def add_svc_rule(self,ruleType,ruleName,minFee,estFee,desc):
        els = self.wd.find_element(By.By.CSS_SELECTOR,'body > main > div.add-one-area > div > div:nth-child(1) > input')
        ele.clear()
        ele.send_keys(ruleName)
        
        #创建Select对象
        select = UI.Select(self.wd.find_element(By.By.ID,'rule-type-id'))
        
        select.select_by_visible_text(ruleType)
        
        if ruleType != '后付费-上报业务量':
            ele = self.wd.find_element(By.By.CSS_SELECTOR,'body > main > div.add-one-area > div > div:nth-child(3) > input[type=number]')
            ele.clear()
            if minFee:
                ele.send_keys(minFee)
        
            ele = self.wd.find_element(By.By.CSS_SELECTOR,'body > main > div.add-one-area > div > div:nth-child(4) > input[type=number]')
            ele.clear()
            if estFee:
                ele.send_keys(estFee)
        if desc:
            ele = self.wd.find_element(By.By.XPATH,'/html/body/main/div[1]/div/div[4]/input')
            ele.clear() 
            ele.send_keys(desc)
            
        if ruleType == '预付费-下发费用':
            pass
        
        elif ruleType == '后付费-上报业务量':
            self.wd.implicitly_wait(0)
            
                
smpUI=SMP_UI()