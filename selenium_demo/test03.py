import selenium.webdriver
import selenium.webdriver.edge.service
import selenium.webdriver.common.by

wd = selenium.webdriver.Edge(service=selenium.webdriver.edge.service.Service("selenium_demo/msEdgeDriver.exe"))
wd.implicitly_wait(10)

wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")

#elements = wd.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR,".animal")
#elements = wd.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR,"span")   
elements = wd.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR,"#container div")
for element in elements:
    print("------------")
    print(element.get_attribute("outerHTML"))
    
wd.quit()
