import selenium.webdriver
import selenium.webdriver.edge.service
import selenium.webdriver.common.by

wd = selenium.webdriver.Edge(service=selenium.webdriver.edge.service.Service("selenium_demo/msEdgeDriver.exe"))
wd.implicitly_wait(10)

wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")

elements = wd.find_elements(selenium.webdriver.common.by.By.CLASS_NAME,"animal")

for element in elements:
    print(element.text)
    
spans = wd.find_elements(selenium.webdriver.common.by.By.TAG_NAME,"span")

for span in spans:
    print(span.text)

pass