import selenium.webdriver
import selenium.webdriver.edge.service
import selenium.webdriver.common.by

wd = selenium.webdriver.Edge(service=selenium.webdriver.edge.service.Service("selenium_demo/msEdgeDriver.exe"))
wd.implicitly_wait(10)


wd.get("https://www.byhy.net/_files/stock1.html")

element = wd.find_element(selenium.webdriver.common.by.By.ID,"kw")
#element.send_keys("电子\n")
element.send_keys("电子")
element.clear()

element = wd.find_element(selenium.webdriver.common.by.By.ID,"go")
element.click()



element = wd.find_element(selenium.webdriver.common.by.By.ID,"1")
print(element.text)


wd.quit()
pass